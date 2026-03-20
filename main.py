from fastapi import FastAPI
from fastapi import BackgroundTasks
from app.api import ai_routes
app = FastAPI(title="BetMonitor & AI Predictor API")



app.include_router(ai_routes.router)

@app.get("/")
def read_root():
    return {"message": "API Online - Sistema de Apostas Iniciado"}



