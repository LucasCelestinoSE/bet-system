import httpx
import asyncio
from bs4 import BeautifulSoup

class FbrScrapper:
    def __init__(self):
        # Agora a url pertence à instância da classe
        self.url = "https://fbref.com/en/comps/9/history/Premier-League-Seasons"
        
    async def get_premier_league_soup(self):
        async with httpx.AsyncClient() as client:
            headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",}
            
            response = await client.get(self.url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            with open("saida_formatada.html", "w", encoding='utf-8') as file:
                file.write(soup.prettify())
            return soup
