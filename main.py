from src.extractor import get_data
from src.utils import capitals_brazil
import pandas as pd
import os
from datetime import datetime

def main():
    dfs = []

    for city, state in capitals_brazil:
        try:
            df = get_data(city, state)
            dfs.append(df)
        except Exception as e:
            print(f"Error in {city}/{state}: {e}")

    df_final = pd.concat(dfs, ignore_index=True)

    df_final.to_csv(r'C:\projects\api-weather-forecast-data\data\arquivo.csv', index=False)

if __name__ == "__main__":
    main()