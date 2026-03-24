from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.services.gemini_service import GeminiService
from typing import Optional

router = APIRouter()

# Função auxiliar para instanciar o serviço
def get_gemini_service():
    return GeminiService()

@router.post("/ask-ai/")
async def ask_gemini(
    prompt: str = Form(...), 
    file: Optional[UploadFile] = File(None),
    # Adicionando o Depends aqui:
    gemini_service: GeminiService = Depends(get_gemini_service)
):
    # Agora você pode usar o serviço injetado
    # Exemplo hipotético:
    resposta = await gemini_service.ask_ai(prompt, file)
    
    return {
        "pergunta1": prompt,
        "file": file.filename if file else None,
        "resposta_ia": resposta
    }