# 🏟️ Bet-System: Data Intelligence Lab

> **Aviso de Natureza do Projeto:** Este é um projeto de fins estritamente acadêmicos e de estudo pessoal. O foco principal é a exploração de engenharia de dados, inteligência artificial e arquiteturas distribuídas aplicadas ao cenário esportivo. **Não possui fins comerciais.**

O **Bet-System** é um ecossistema em construção focado na extração, monitoramento e predição de dados de futebol. O projeto nasceu da necessidade de explorar a transição tecnológica entre **Crawlers Determinísticos** (regras estruturadas) e **Agentes Autônomos** (IA interpretativa).

---

## 🚀 Visão Geral e Objetivos

O projeto funciona como um laboratório de exploração para:

- **Crawlers Híbridos:** Desenvolvimento de scrapers determinísticos e, futuramente, agentes agênticos com LLMs.
- **Preditor de Partidas:** Utilização de estatísticas avançadas (xG - Expected Goals) e ML.
- **Monitoramento de Odds:** Identificação de variações de mercado em tempo real.
- **Engenharia de Dados:** Testes comparativos de performance entre **NoSQL (MongoDB)** e **SQL (PostgreSQL)**.

---

## 🏗️ Arquitetura de Exploração

O sistema é orquestrado via Docker, garantindo que o ambiente seja idêntico em qualquer máquina.

| Componente    | Tecnologia     | Responsabilidade                                       |
| :------------ | :------------- | :----------------------------------------------------- |
| **Backend**   | FastAPI        | Ingestão assíncrona e roteamento de dados.             |
| **Frontend**  | Streamlit      | Dashboard de visualização e controle dos crawlers.     |
| **Banco NoSQL** | MongoDB      | Armazenamento de JSONs brutos e dados não estruturados.|
| **Banco SQL** | PostgreSQL     | Armazenamento de dados processados e modelos de treino.|
| **Container** | Docker Compose | Orquestração e isolamento de serviços.                 |

---

## 🛠️ Guia de Operação

### Instalação e Build

Se for a primeira vez ou se houver alterações no `Dockerfile` ou `requirements.txt`:

```bash
sudo docker-compose up --build
```

### Ciclo de Desenvolvimento

**Para desligar o PC** — Para os containers mantendo os dados salvos:

```bash
sudo docker compose stop
```

**Para voltar aos estudos** — Liga tudo de novo em segundos:

```bash
sudo docker compose start
```

---

## 📈 Roadmap de Desenvolvimento

### Fase 1: Infraestrutura e Ingestão (Atual)

| Etapa              | Descrição                                  | Status         | Requisitos Adicionais          |
| :----------------- | :----------------------------------------- | :------------- | :----------------------------- |
| Setup Docker       | Configuração de API, UI e Bancos.          | ✅ Concluído   | Volumes para persistência.     |
| Mongo Integration  | Ingestão em massa (Bulk Insert) via API.   | ✅ Concluído   | Driver Motor (Async).          |
| History Scraper    | Extração determinística do FBref.          | 🚧 Em Progresso | Bypass de Cloudflare.         |

### Fase 2: Inteligência e Processamento

| Etapa          | Descrição                              | Status       | Requisitos Adicionais        |
| :------------- | :------------------------------------- | :----------- | :--------------------------- |
| Data Cleaning  | Limpeza de tags HTML via regex/IA.     | ⏳ Pendente  | BeautifulSoup / Regex.       |
| xG Analysis    | Cálculo de médias e correlações.       | ⏳ Pendente  | Biblioteca Pandas/Numpy.     |
| News Crawler   | Scraper de portais de notícias.        | ⏳ Pendente  | —                            |

### Fase 3: IA e Predição (Roadmap Futuro)

| Etapa             | Descrição                                      | Status      | Requisitos Adicionais        |
| :---------------- | :--------------------------------------------- | :---------- | :--------------------------- |
| Agentic Crawlers  | Scraping guiado por LLMs (LangChain).          | ⏳ Pendente | API Keys (Gemini/OpenAI).    |
| ML Models         | Treinamento de modelos de predição.            | ⏳ Pendente | Scikit-learn / PyTorch.      |
| Deep Learning     | Redes neurais para predição de placar.         | ⏳ Pendente | —                            |

---

## 📋 Endpoints Principais (Local)

| Serviço             | Endereço                        |
| :------------------ | :------------------------------ |
| Documentação API    | http://localhost:8000/docs      |
| Interface UI        | http://localhost:8501           |
| Conexão MongoDB     | mongodb://localhost:27017       |

---

*Desenvolvido por **Lucas Celestino***  
*Explorando a fronteira entre engenharia de software e análise de dados esportivos.*