
# 📈 Stock Profitability Checker

This is a beginner-friendly Python project that allows users to analyze whether a stock is potentially profitable using basic financial metrics.

The script uses real-time stock data from Yahoo Finance via the `yfinance` library, and calculates key metrics such as:

- ✅ Annualized return  
- ✅ Volatility  
- ✅ Sharpe Ratio  
- ✅ Beta (against the S&P 500)

The user just inputs a stock ticker (e.g., `AAPL`, `MSFT`, `GOOGL`) and the script fetches one year of data, performs financial analysis, and tells you whether the stock appears profitable based on the Sharpe ratio and return.

---

## 💡 Features

- Simple user input for stock symbol
- Real-time data pulled from Yahoo Finance
- Financial equations for performance analysis
- Console output with profitability assessment

---

## 📦 Requirements

Install required libraries using:

```bash
pip install -r requirements.txt
