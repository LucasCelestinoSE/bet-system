from bs4 import BeautifulSoup, Tag
from typing import Union

def html_table_to_dict(html: Union[str, Tag]) -> list[dict]:
    """
    Converte HTML table(s) para lista de dicionarios.

    Retorna lista onde cada item representa uma <tr> do <tbody>,
    com chaves vindas do <thead>.
    """
    if isinstance(html, str):
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all('table')
    else:
        tables = [html] if html.name == 'table' else html.find_all('table')

    results = []

    for table in tables:
        caption = table.find('caption')
        titulo = caption.get_text(strip=True) if caption else None

        thead = table.find('thead')
        tbody = table.find('tbody')

        if not thead or not tbody:
            continue

        # extrai colunas do header
        headers = [th.get_text(strip=True) for th in thead.find_all(['th', 'td'])]

        # extrai linhas do body
        for tr in tbody.find_all('tr'):
            cells = tr.find_all(['td', 'th'])
            row = {'caption': titulo} if titulo else {}
            for i, header in enumerate(headers):
                value = cells[i].get_text(strip=True) if i < len(cells) else None
                row[header] = value
            results.append(row)

    return results


# --- atalho rapido ---
if __name__ == '__main__':
    exemplo = """
    <table>
      <caption>Times - Premier League</caption>
      <thead>
        <tr><th>Time</th><th>P</th><th>V</th><th>E</th><th>D</th></tr>
      </thead>
      <tbody>
        <tr><td>Arsenal</td><td>30</td><td>25</td><td>3</td><td>2</td></tr>
        <tr><td>Chelsea</td><td>28</td><td>22</td><td>4</td><td>4</td></tr>
      </tbody>
    </table>
    """
    import json
    for row in html_table_to_dict(exemplo):
        print(json.dumps(row, indent=2))
