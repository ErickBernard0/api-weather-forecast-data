from src.extractor import get_data
from src.utils import capitals_brazil
from src.database import get_engine, save_dataframe
import pandas as pd
import os
from datetime import datetime

def main():
    dfs = []

    for city, state in capitals_brazil:
        try:
            df = get_data(city, state)
            dfs.append(df)
            print(f"Collected: {city}/{state}")
        except Exception as e:
            print(f"Error in {city}/{state}: {e}")

    df_final = pd.concat(dfs, ignore_index=True)

    engine = get_engine()

    table_name = "weather_forecast"

    save_dataframe(df_final, engine, table_name)
    print("saved data")

if __name__ == "__main__":
    main()