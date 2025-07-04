from src.extractor import get_data

def main():
    df = get_data("São Paulo")
    print(df.head())

if __name__ == "__main__":
    main()