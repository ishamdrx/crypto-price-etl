import requests
import pandas as pd
import sqlite3
from datetime import datetime

def run_pipeline():
    data = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets",
        params={"vs_currency": "usd", "ids": "bitcoin,ethereum,solana"}
    ).json()

    df = pd.DataFrame(data)[["id", "symbol", "current_price", "circulating_supply", "last_updated", "market_cap"]]
    df.columns = ["coin_id", "symbol", "price_usd", "circulating_supply", "api_last_updated", "market_cap_usd"]
    df["symbol"] = df["symbol"].str.upper()
    df["ingested_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect("crypto_prices.db") as conn:
        df.to_sql("crypto_prices", conn, if_exists="append", index=False)

    print(df)

run_pipeline()