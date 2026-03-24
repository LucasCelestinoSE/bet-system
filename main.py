from fastapi import FastAPI, File, UploadFile
from fastapi import BackgroundTasks
from app.api import ai_routes
from app.services.gemini_service import GeminiService


app = FastAPI(title="BetMonitor & AI Predictor API")



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


# main => Adapters => gemini_service => 