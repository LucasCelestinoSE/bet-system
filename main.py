from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="BetMonitor & AI Predictor API")

# -- SCHEMAS (Contrato de dados entre você e seu amigo) --
class PredictionRequest(BaseModel):
    match_id: str
    league: str

class OddCheck(BaseModel):
    home_team: str
    away_team: str
    odds: dict # Ex: {"bet365": 1.90, "betano": 2.05}

# -- ROTAS DO SEU AMIGO (IA) --
@app.get("/predict/{match_id}")
async def get_ai_prediction(match_id: str):
    # Aqui ele vai importar a classe de ML dele
    return {"status": "success", "prediction": "Home Win", "confidence": 0.85}

# -- SUAS ROTAS (Monitor de Surebet) --
@app.post("/monitor/check-arbitrage")
async def check_surebet(data: OddCheck):
    # Aqui você implementa seu algoritmo de arbitragem
    return {"is_surebet": False, "profit_margin": "0.0%"}

@app.get("/")
def read_root():
    return {"message": "API Online - Sistema de Apostas Iniciado"}

@app.get("/olamundo")
def ola_mundo():
    return {"message:" "Olá mundo"}