# libs
import requests
import pandas as pd
from datetime import datetime, timedelta
from src.config import API_KEY, BASE_URL
from src.utils import moon_phase_case

# functions
def generate_dates():
    today = datetime.today()
    final_day = today + timedelta(days=7)
    return today.strftime('%Y-%m-%d'), final_day.strftime('%Y-%m-%d')

def create_url(location: str, start_date: str, end_date: str) -> str:
    return f"{BASE_URL}/{location}/{start_date}/{end_date}"

def get_data(city: str, state: str) -> pd.DataFrame:
    start_date, end_date = generate_dates()
    url = create_url(city, start_date, end_date)

    params = {
        'unitGroup': 'metric',
        'include': 'days',
        'key': API_KEY,
        'contentType': 'json'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['days'])

        # select columns
        df = df[[
            'datetime',
            'tempmax',
            'tempmin',
            'feelslikemax', 
            'feelslikemin',
            'humidity',
            'moonphase',
            'conditions',
            'description'
        ]]
        
        # adjusting column
        df['moonphase'] = df['moonphase'].apply(moon_phase_case)

        # add metadata
        df['city'] = city
        df['state'] = state
        df['ingestion_date'] = datetime.today().strftime('%Y-%m-%d')

        return df
    else:
        raise Exception(f"Erro {response.status_code}: {response.text}")