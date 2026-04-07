from bs4 import BeautifulSoup
from typing import Union

def table_to_dict(html: Union[str, BeautifulSoup]) -> list[dict]:
    """
    Converte uma tabela HTML em lista de dicionários.
    
    Exemplo de saída:
    [
        {'Pos': '1', 'Time': 'Arsenal', 'Pts': '30'},
        {'Pos': '2', 'Time': 'Man City', 'Pts': '28'},
    ]
    """
    if isinstance(html, str):
        soup = BeautifulSoup(html, 'html.parser')
    else:
        soup = html if hasattr(html, 'find') else BeautifulSoup(str(html), 'html.parser')
    
    # Extrair cabeçalhos do <thead>
    thead = soup.find('thead')
    headers = []
    if thead:
        header_row = thead.find('tr')
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
    
    if not headers:
        return []
    
    # Extrair dados do <tbody>
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr') if tbody else []
    
    resultado = []
    for row in rows:
        cells = row.find_all(['td', 'th'])
        valores = [cell.get_text(strip=True) for cell in cells]
        
        # Criar dicionário combinando headers com valores
        dict_linha = {}
        for i, header in enumerate(headers):
            dict_linha[header] = valores[i] if i < len(valores) else ''
        
        resultado.append(dict_linha)
    
    return resultado


def extract_all_tables(html: str) -> list[list[dict]]:
    """
    Extrai todas as tabelas de um HTML e retorna lista de tabelas,
    onde cada tabela é uma lista de dicionários.
    """
    soup = BeautifulSoup(html, 'html.parser')
    tabelas = soup.find_all('table')
    
    return [table_to_dict(tabela) for tabela in tabelas]
