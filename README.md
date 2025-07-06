# ⛅ Weather Forecast BR

Projeto de portfólio para praticar conceitos de coleta, armazenamento, agendamento e visualização de dados.

## 💡 Visão Geral

Este projeto coleta diariamente dados de previsão do tempo para todas as capitais do Brasil, utilizando a [API da Visual Crossing](https://www.visualcrossing.com/). Os dados são salvos em um banco PostgreSQL hospedado no Render, e posteriormente visualizados em um aplicativo feito com Streamlit.

Além disso, a coleta é automatizada com o uso de **GitHub Actions**, garantindo uma rotina de atualização diária.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: linguagem principal do projeto  
- **Requests / Pandas**: extração e tratamento dos dados  
- **Dotenv**: para ocultar informações sensíveis (API Key, credenciais do banco)  
- **PostgreSQL (Render)**: banco de dados gratuito onde os dados são armazenados  
- **SQLAlchemy**: conexão e escrita no banco de forma prática  
- **Streamlit**: visualização interativa dos dados  
- **GitHub Actions**: agendamento do processo diariamente às 08h (UTC-3)

---

## 🔁 Fluxo do Projeto

1. Coleta os dados da previsão dos próximos 7 dias para cada capital do Brasil  
2. **Substitui os dados anteriores no banco (estratégia overwrite)** para manter apenas os dados mais recentes  
3. Visualiza os dados via Streamlit, com filtros por estado/cidade/data e gráficos interativos  
4. Atualiza automaticamente todos os dias via GitHub Actions

---

## 📊 Visualização

A visualização pode ser executada localmente com o Streamlit e permite:

- Filtrar por estado e cidade
- Ver temperaturas máxima e mínima em gráfico interativo
- Destaques com o dia mais quente e mais frio
- Tabela com todos os dados de previsão dos próximos 7 dias

---

## ▶️ Como executar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/api-weather-forecast-data.git
cd api-weather-forecast-data
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo .env com suas credenciais:
```env
API_KEY=your_visualcrossing_api_key
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=your_db_host
POSTGRES_PORT=5432
POSTGRES_DB=your_db_name
```

5. Rode o script de extração de dados:
```bash
python main.py
```

6. Inicie o app de visualização:
```bash
streamlit run app.py
```