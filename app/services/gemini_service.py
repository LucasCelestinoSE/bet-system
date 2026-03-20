import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        # Usamos o getenv com um aviso caso falte a chave
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Chave GEMINI_API_KEY não encontrada no .env")
        
        self.client = genai.Client(api_key=api_key)
        # 1.5-flash é mais estável para cotas gratuitas
        self.model_name = "gemini-1.5-flash" 

    async def ask_ai(self, prompt: str):
        # Usamos await para não bloquear o worker do FastAPI
        response = await self.client.models.generate_content(
            model=self.model_name, 
            contents=prompt
        )
        return response.text