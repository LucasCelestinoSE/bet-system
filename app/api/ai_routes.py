from fastapi import APIRouter, Depends
from app.services.gemini_service import GeminiService

router = APIRouter()

# 2. Criamos uma função para gerenciar a instância do serviço
def get_gemini_service():
    return GeminiService()

@router.get("/ask-ai/")
async def ask_gemini(prompt: str, service: GeminiService = Depends(get_gemini_service)):
    # 3. A rota agora é assíncrona
    resposta = await service.ask_ai(prompt)
    return {
        "status": "sucesso",
        "pergunta": prompt,
        "resposta_ia": resposta
    }