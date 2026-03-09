import sqlite3
import pandas as pd

conn = sqlite3.connect("crypto_prices.db")

df = pd.read_sql("SELECT * FROM crypto_prices", conn)

print(df)

conn.close()