# libs
import requests
import pandas as pd
from datetime import datetime, timedelta
from src.config import API_KEY, BASE_URL

# functions
def generate_dates():
    today = datetime.today()
    final_day = today + timedelta(days=7)
    return today.strftime('%Y-%m-%d'), final_day.strftime('%Y-%m-%d')

def create_url(location: str, start_date: str, end_date: str) -> str:
    return f"{BASE_URL}/{location}/{start_date}/{end_date}"

def get_data(location: str) -> pd.DataFrame:
    start_date, end_date = generate_dates()
    url = create_url(location, start_date, end_date)

    params = {
        'unitGroup': 'metric',
        'include': 'days',
        'key': API_KEY,
        'contentType': 'json'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data['days'])
    else:
        raise Exception(f"Erro {response.status_code}: {response.text}")