# Exploratory Data Analysis on financial datasets


## Data Source

For this project, the following tickers (symbols) of financial instruments related to **artificial intelligence and technology** were selected:

- **NVDA**: NVIDIA Corporation
- **MSFT**: Microsoft Corporation
- **GOOGL**: Alphabet Inc. (Google)
- **BOTZ**: Global X Robotics & Artificial Intelligence ETF
- **ARKQ**: ARK Autonomous Technology & Robotics ETF

### Date Range

The historical data downloaded covers the following time period:

- **Start Date**: 2015-04-20
- **End Date**: 2025-04-20

### Data Source

The data was obtained using the **`yfinance`** library and the **`download_data.py`** script. This script downloaded the historical price and volume data for the selected tickers from Yahoo Finance.

**Script used**: `scripts/download_data.py`

---

## Data Cleaning and Preprocessing

Data cleaning and preprocessing were performed in the notebook **`01_data_acquisition_cleaning_exploration.ipynb`**, which performed the following tasks:

1. **Handling Null Values**: Null values were handled using the **forward fill** (`ffill()`) technique, where missing values were replaced with the most recent available value in the time series.

2. **Processed Data Storage**: After cleaning, the processed data was saved in the file **`ai_stocks_historical_data_cleaned.parquet`**, located in the **`data/processed/`** subfolder. This file contains the cleaned data, ready for future analysis.

**Processed data saved in**: `data/processed/ai_stocks_historical_data_cleaned.parquet`

---

## Project Overview

The goal of this project is to conduct an exploratory data analysis (EDA) on stocks from leading companies in the **artificial intelligence (AI)** and technology sectors. The historical price data for the selected tickers will be analyzed using visualization and statistical tools to find patterns, trends, and correlations between the assets.
