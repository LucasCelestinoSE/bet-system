import os

def criar_pagina(caminho, titulo, links):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>{titulo}</title></head>
    <body>
        <h1>{titulo}</h1>
        <ul>
            {"".join([f'<li><a href="{l}">Link para {l}</a></li>' for l in links])}
        </ul>
        <p>Conteúdo da página: Dados simulados de {titulo}.</p>
    </body>
    </html>
    """
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(html_content)

# Configuração da estrutura
base_dir = "site_teste"
os.makedirs(base_dir, exist_ok=True)

# 1. Criar a Home (Nível 0)
ligas = ["premier_league", "la_liga", "serie_a"]
criar_pagina(f"{base_dir}/index.html", "Home - Lista de Ligas", [f"{l}/index.html" for l in ligas])

for liga in ligas:
    liga_path = os.path.join(base_dir, liga)
    os.makedirs(liga_path, exist_ok=True)
    
    # 2. Criar Página da Liga (Nível 1)
    times = [f"time_{i}" for i in range(1, 4)]
    criar_pagina(f"{liga_path}/index.html", f"Liga: {liga}", [f"{t}/index.html" for t in times])
    
    for time in times:
        time_path = os.path.join(liga_path, time)
        os.makedirs(time_path, exist_ok=True)
        
        # 3. Criar Página do Time (Nível 2)
        jogadores = [f"jogador_{j}.html" for j in range(1, 4)]
        criar_pagina(f"{time_path}/index.html", f"Time: {time}", jogadores)
        
        # 4. Criar Página do Jogador (Nível 3 - Fim do Ramo/Folha)
        for jogador in jogadores:
            criar_pagina(f"{time_path}/{jogador}", f"Estatísticas: {jogador}", [])

print(f"Estrutura criada com sucesso na pasta '{base_dir}'!")