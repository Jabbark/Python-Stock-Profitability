import yfinance as yf
from pyfinance.ols import OLS
import numpy as np
import pandas as pd
import datetime as dt

# Risk-free rate (for example, 5% annual)
risk_free_rate = 0.05

def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

def calculate_returns(data):
    data['Return'] = data['Close'].pct_change()
    return data.dropna()

def calculate_metrics(data):
    mean_return = data['Return'].mean() * 252  # annualized
    volatility = data['Return'].std() * np.sqrt(252)  # annualized
    sharpe_ratio = (mean_return - risk_free_rate) / volatility
    return mean_return, volatility, sharpe_ratio

def calculate_beta(stock_returns, market_returns):
    regression = OLS(stock_returns, market_returns)
    beta = regression.beta[1]  # 1 is the slope coefficient
    return beta

def main():
    user_ticker = input("Enter stock ticker symbol (e.g., AAPL): ").upper()
    market_ticker = "^GSPC"  # S&P 500 as market proxy

    print(f"Fetching data for {user_ticker} and {market_ticker}...")
    stock_data = get_stock_data(user_ticker)
    market_data = get_stock_data(market_ticker)

    stock_data = calculate_returns(stock_data)
    market_data = calculate_returns(market_data)

    combined = pd.concat([stock_data['Return'], market_data['Return']], axis=1)
    combined.columns = ['Stock_Return', 'Market_Return']
    combined.dropna(inplace=True)

    mean_return, volatility, sharpe_ratio = calculate_metrics(combined)
    beta = calculate_beta(combined['Stock_Return'], combined['Market_Return'])

    print(f"\nFinancial Metrics for {user_ticker}:")
    print(f"Annualized Mean Return: {mean_return:.2%}")
    print(f"Annualized Volatility: {volatility:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Beta vs S&P 500: {beta:.2f}")

    if sharpe_ratio > 1 and mean_return > risk_free_rate:
        print(f"\n{user_ticker} appears to be a profitable investment based on Sharpe ratio and return.")
    else:
        print(f"\n{user_ticker} may not be a highly profitable investment based on current data.")

if __name__ == "__main__":
    main()
