from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
class AiRequests(BaseModel):
    prompt1: str 
    file: File