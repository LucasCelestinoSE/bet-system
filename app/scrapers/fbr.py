import pandas as pd
from bs4 import BeautifulSoup
from seleniumbase import SB
import requests

import os
import re

class FbrScrapper:
    def __init__(self):
        self.url_history = "https://fbref.com/en/comps/9/history/Premier-League-Seasons"
        
    def extract_data_from_url(self, url):
        with SB(uc=True) as sb:
            sb.uc_open_with_reconnect(url, 4)
            sb.uc_gui_click_captcha()
            dict_data = {}
            # Usamos outerHTML para manter a tag <tbody>, facilitando o parse do Pandas
            script_js = """
                const seasons = document.getElementById("seasons");
                const ths = seasons.querySelectorAll("th")
                return Array.from(ths).map(th => th.outerHTML);
            """
            ths = sb.execute_script(script_js)
            script_js2 = """
                const tds = seasons.querySelectorAll("td")
                return Array.from(tds).map(td => td.outerHTML);
            """
            tds = sb.execute_script(script_js2)
            dict_data["ths"] = ths
            dict_data["tds"] = tds
        print(f"Encontrei {len(ths)} ths válidos via JavaScript!")
        print(f"Encontrei {len(tds)} tds válidos via JavaScript!")
        return dict_data # <-- Este retorno é o "combustível" do próximo método

    def parse_data(self, dict_data):
        ths = dict_data["ths"]
        tds = dict_data["tds"]
        soup_ths = list(map(lambda x: BeautifulSoup(x, 'html.parser'), ths))
        soup_tds = list(map(lambda x: BeautifulSoup(x, 'html.parser'), tds))

        data = {
            "seasons": [],
            "link_season": [],
            "Competition Name": [],
            "squads": [],
            "Champion": [],
            "Top Scorer": []
        }

        pattern = re.compile(r"\d{4}-\d{4}")
        for th in soup_ths:
            text = th.get_text().strip()
            if pattern.fullmatch(text):
                data["seasons"].append(text)
                data["link_season"].append(th.find("a")["href"])
        for i in range(0, len(tds), 4):
            data["Competition Name"].append(tds[i])
        for i in range(1,len(tds), 4):
            data["squads"].append(tds[i])
        for i in range(2,len(tds), 4):
            data["Champion"].append(tds[i])
        for i in range(3,len(tds), 4):
            data["Top Scorer"].append(tds[i])
        return data
    def executar(self):
        """MÉTODO COORDENADOR: Cria a dependência entre os dois"""
        # 1. Pega os dados brutos (Passo A)
        dados_brutos = self.extract_data_from_url(self.url_history)
        data = self.parse_data(dados_brutos)
        df = pd.DataFrame(data)
        dados_formatados = df.to_dict(orient="records")
        
        response = requests.post("http://localhost:8000/save", json=dados_formatados)
        #df.to_json("premier_league_history.json", orient="records", indent=4)

FbrScrapper().executar()