import httpx
from bs4 import BeautifulSoup
from app.schemas.news import FootballNews

class NewsService:
    async def fetch_ge_news(self):
        url = "https://ge.globo.com/futebol/"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            articles = []
            # Exemplo simplificado de seletor do GE
            for item in soup.select('.feed-post-body')[:5]: 
                title = item.select_one('.feed-post-link').text
                link = item.select_one('.feed-post-link')['href']
                articles.append(FootballNews(title=title, url=link, source="GE", content=""))
            
            return articles