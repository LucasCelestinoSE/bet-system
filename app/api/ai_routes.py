from fastapi import APIRouter
from app.services.gemini_service import GeminiService
# ... imports ...
geminiService = GeminiService()
router = APIRouter()

@router.get("/ask-ai/")
def ask_gemini(prompt: str):
    resposta = geminiService.ask_ai(prompt)
    return {
        "status": "sucesso",
        "pergunta": prompt,
        "resposta_ia": resposta
    }

