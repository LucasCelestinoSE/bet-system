import google.genai as genai
import os
from dotenv import load_dotenv
from google.genai import errors
load_dotenv()

class GeminiService:
    def __init__(self):
        # Usamos o getenv com um aviso caso falte a chave
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Chave GEMINI_API_KEY não encontrada no .env")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-3-flash-preview" 

    async def ask_ai(self, prompt: str):
        try:
            response =  await self.client.aio.models.generate_content(
                model=self.model_name, 
                contents=prompt
            )
            return response.text
        
        except errors.ClientError as e:
            print(f"Erro de Cliente (API): {e}")
            return f"Erro na API do Gemini: {e.message}"
            
        except Exception as e:
            print(f" Erro inesperado: {type(e).__name__} - {e}")
            return "Ocorreu um erro interno ao processar sua solicitação."