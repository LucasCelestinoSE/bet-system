from extract_table import table_to_dict, extract_all_tables

# Exemplo de uso com HTML de string
html_exemplo = """
<table>
    <thead>
        <tr>
            <th>Pos</th>
            <th>Time</th>
            <th>P</th>
            <th>V</th>
            <th>E</th>
            <th>D</th>
            <th>Pts</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Arsenal</td>
            <td>12</td>
            <td>10</td>
            <td>1</td>
            <td>1</td>
            <td>31</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Man City</td>
            <td>12</td>
            <td>9</td>
            <td>2</td>
            <td>1</td>
            <td>29</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Liverpool</td>
            <td>12</td>
            <td>8</td>
            <td>3</td>
            <td>1</td>
            <td>27</td>
        </tr>
    </tbody>
</table>
"""

# Testando com uma tabela
resultado = table_to_dict(html_exemplo)
for linha in resultado:
    print(linha)

print("\n" + "="*50 + "\n")

# Testando com múltiplas tabelas
html_multiplas = f"""
<html>
<body>
    {html_exemplo}
    {html_exemplo}
</body>
</html>
"""

todas_tabelas = extract_all_tables(html_multiplas)
print(f"Encontradas {len(todas_tabelas)} tabelas")
print(f"Primeira tabela tem {len(todas_tabelas[0])} linhas")
