from pydantic import BaseModel
from datetime import datetime

class FootballNews(BaseModel):
    title: str
    url: str
    source: str
    content: str
    scraped_at: datetime = datetime.now()