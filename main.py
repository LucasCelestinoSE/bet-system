from fastapi import FastAPI, File, UploadFile
from fastapi import BackgroundTasks
from app.api import ai_routes
from typing import List, Optional
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from app.services.gemini_service import GeminiService


app = FastAPI(title="BetMonitor & AI Predictor API")

# 1. Objeto Global (vazio no início)
class DB:
    client = None
    db = None

db_mongo = DB()

# 2. O "Interruptor" (Lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Liga o banco
    db_mongo.client = AsyncIOMotorClient("mongodb://mongodb:27017")
    db_mongo.db = db_mongo.client.bet_intelligence_db
    print("🚀 Banco Conectado!")
    
    yield # O App fica "vivo" aqui
    
    # Desliga o banco
    db_mongo.client.close()
    print("💤 Banco Desconectado!")

# 3. Cria o App usando o Lifespan
app = FastAPI(lifespan=lifespan)

# 4. Exemplo de Rota usando o banco global
@app.post("/save")
async def save_data(item: List[dict]):
    await db_mongo.db.seasons.insert_many(item)
    return {"status": "salvo no mongo!"}

app.include_router(ai_routes.router)

@app.get("/")
async def read_root():
    return {"message": "soup"}

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file}


from typing import Optional
# Armazenou dados das temporadas , temporada ano , link, times, Campeões,
@app.get("/seasons")
async def get_seasons(
    page: Optional[int] = None, 
    page_size: Optional[int] = None,
    seasons: Optional[str] = None,       # Filtro opcional por temporada
    link_season: Optional[str] = None    # Filtro opcional por link
):
    try:
        # 1. Construir o Filtro Dinâmico (Query do MongoDB)
        query_filter = {}
        
        if seasons:
            # Usamos regex 'i' para busca case-insensitive (não importa se é 2025 ou 2025-2026)
            query_filter["seasons"] = {"$regex": seasons, "$options": "i"}
            
        if link_season:
            query_filter["link_season"] = link_season

        # 2. Criar o cursor com o filtro aplicado
        cursor = db_mongo.db.seasons.find(query_filter)

        # 3. Lógica de Paginação (Mantida)
        if page is not None and page_size is not None:
            skip = (page - 1) * page_size
            cursor = cursor.skip(skip).limit(page_size)

        # 4. Executar a busca
        results = await cursor.to_list(length=1000)

        # 5. Converter ObjectID para String para o JSON não quebrar
        for item in results:
            item["_id"] = str(item["_id"])

        return results
        
    except Exception as e:
        print(f"Erro na busca: {e}")
        return {"error": "Falha interna ao buscar dados"}, 500

# main => Adapters => gemini_service => 