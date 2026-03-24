import google.genai as genai, types
import os
from dotenv import load_dotenv
from google.genai import errors
from fastapi import File, UploadFile
from typing import Optional
import shutil
load_dotenv()

class GeminiService:
    def __init__(self):
        # Usamos o getenv com um aviso caso falte a chave
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Chave GEMINI_API_KEY não encontrada no .env")
        self.data = [];
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-3-flash-preview" 

    async def ask_ai(self, prompt: str, file: UploadFile = None):
        temp_path = None
        try:
            contents = [prompt]

            if file:
                # 1. Criamos um caminho real no disco
                temp_path = f"temp_{file.filename}"
                
                # 2. Escrevemos os bytes do UploadFile para esse caminho
                with open(temp_path, "wb") as buffer:
                    shutil.copyfileobj(file.file, buffer)
                
                print(f"📤 Fazendo upload do arquivo para o Gemini: {temp_path}")
                
                # 3. Agora passamos o CAMINHO (string) para o Gemini
                uploaded_file = self.client.files.upload(file=temp_path)
                contents.append(uploaded_file)

            response = await self.client.aio.models.generate_content(
                model=self.model_name,
                contents=contents
            )
            return response.text

        except Exception as e:
            print(f"🔥 Erro Multimodal: {e}")
            return f"Erro ao processar conteúdo: {str(e)}"
        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)
        
        

        

