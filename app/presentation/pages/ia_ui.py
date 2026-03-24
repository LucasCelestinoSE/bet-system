import streamlit as st
import requests

st.title("Upload de Arquivo para API")

# Componente para selecionar o arquivo
uploaded_file = st.file_uploader("Escolha um arquivo de texto", type=['html'])

if uploaded_file is not None:
    if st.button("Enviar para API"):
        # Preparando o arquivo para o envio
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        
        try:
            # Substitua pela URL da sua rota
            response = requests.post("http://api:8000/ask-ai/", files=files)
            
            if response.status_code == 200:
                st.success("Arquivo enviado com sucesso!")
                st.json(response.json())
            else:
                st.error(f"Erro na API: {response.status_code}")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")