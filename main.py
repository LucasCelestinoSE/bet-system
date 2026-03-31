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


@app.get("/seasons")
async def get_seasons(page: Optional[int] = None, page_size: Optional[int] = None):
    try:
        # 1. Criamos o cursor de busca (ainda não puxou do banco)
        cursor = db_mongo.db.seasons.find({})

        # 2. Lógica de Paginação (Só aplica se AMBOS existirem)
        if page is not None and page_size is not None:
            # Cálculo: Pula os itens das páginas anteriores e limita ao tamanho da página
            skip = (page - 1) * page_size
            cursor = cursor.skip(skip).limit(page_size)

        # 3. Converte o cursor em uma lista
        results = await cursor.to_list(length=1000) # Limite de segurança para não travar a RAM

        # 4. TRUQUE: O MongoDB retorna o '_id' como um objeto, o JSON não aceita.
        # Vamos converter o _id para string em cada item.
        for item in results:
            item["_id"] = str(item["_id"])

        return {
            "total_na_pagina": len(results),
            "data": results
        }
        
    except Exception as e:
        return {"error": str(e)}, 500

# main => Adapters => gemini_service => 