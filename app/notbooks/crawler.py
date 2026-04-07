# CORREÇÃO 1: Passe os argumentos necessários para a função
def return_links_from_href(hrefs, base):
    arr = []
    for a in hrefs:
        # Garanta que não está duplicando barras
        link_completo = base + a['href']
        arr.append(link_completo)
    return arr

import nest_asyncio
nest_asyncio.apply()  # Essencial para não travar o Kernel do Jupyter

from seleniumbase import SB
from collections import deque
from urllib.parse import urljoin
from time import sleep
# Configurações de caminho e URL
# Certifique-se de que o Live Server (porta 5500) está rodando no VS Code
base_url = "http://127.0.0.1:5500/app/notbooks/site_teste/"                                                                
index = "index.html"
initial_page = base_url + index

# Inicialização de controle (fora do loop)
verificados = set()




with SB(browser='chrome', headless=False, headed=True) as sb:
    sb.open(initial_page)
    # Função interna para pegar links da página ATUAL
    def get_links_da_pagina_atual(driver):
        soup = driver.get_beautiful_soup()
        hrefs = soup.find_all('a', href=True)
        links_completos = []
        for a in hrefs:
            # urljoin resolve o link relativo baseado na URL em que o navegador está agora
            # Ex: se está em site_teste/la_liga/ e o link é 'index.html', 
            # ele gera site_teste/la_liga/index.html corretamente.
            url_completa = urljoin(driver.get_current_url(), a['href'])
            links_completos.append(url_completa)
        return links_completos

    # Inicializa a fila
    fila_de_pesquisa = deque(get_links_da_pagina_atual(sb))
    verificados.add(initial_page)

    while fila_de_pesquisa:
        new_tab = fila_de_pesquisa.popleft()
        sleep(0.5)
        # Limpeza simples para evitar âncoras (ex: index.html#topo)
        new_tab = new_tab.split('#')[0]

        if new_tab not in verificados:
            print(f"Navegando para: {new_tab}")
            verificados.add(new_tab)
            
            try:
                sb.open(new_tab)
                # Pega os links da nova página e adiciona na fila
                novos_links = get_links_da_pagina_atual(sb)
                fila_de_pesquisa.extend(novos_links)
    
            except Exception as e:
                print(f"Erro ao abrir {new_tab}: {e}")
    input("presseione enteter pra parar")

