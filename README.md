# Crypto Price ETL Pipeline

A simple Python ETL mini project that extracts live cryptocurrency market data from the CoinGecko API, transforms it into a clean table using Pandas, and loads it into a local SQLite database.

This project was built as a beginner data engineering project to practice the core ETL flow:

**Extract → Transform → Load**

---

## Project Overview

This pipeline:

- Extracts live crypto data from the CoinGecko API
- Transforms the raw JSON into a structured Pandas DataFrame
- Loads the cleaned data into a local SQLite database
- Allows viewing the stored data using a separate Python script

Coins used in this project:

- Bitcoin
- Ethereum
- Solana

---

## Tech Stack

- Python
- Requests
- Pandas
- SQLite

---

## Project Structure

```bash
crypto-price-etl/
│
├── etl_pipeline.py      # Main ETL pipeline
├── db.py                # Display data stored in SQLite database
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── crypto_prices.db     # SQLite database created after running the pipeline
