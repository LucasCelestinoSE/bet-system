import asyncio
from bs4 import BeautifulSoup
import pandas as pd
class FbrScrapper:
    def __init__(self):
        # Agora a url pertence à instância da classe
        self.file_path = "../../temp_2025-2026_Premier_League_Stats_tabelas.html"

    def extract_info_files(self):
        with open(self.file_path) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        return soup
data = []
list_header = [] 
fbrScrapper = FbrScrapper()
html = fbrScrapper.extract_info_files()
header = html.find_all("table")[0].find("tr")
HTML_data = html.find_all("table")[0].find_all("tr")[1:]

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)
dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.to_json('dados_de_jogos.json')   