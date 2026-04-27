# src/execution_backtester.py

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# PARAMETERS
# -----------------------------
TICKER = 'AAPL'
PERIOD = '2y'
INITIAL_CAPITAL = 100000
SLIPPAGE = 0.001   # 0.1% slippage
COMMISSION = 1     # $1 per trade

# -----------------------------
# FUNCTIONS
# -----------------------------
def fetch_data(ticker, period=PERIOD):
    data = yf.Ticker(ticker).history(period=period)
    if data.empty:
        raise ValueError("No data fetched")
    return data

def generate_signals(data):
    # Example: SMA crossover signal
    data['SMA10'] = data['Close'].rolling(10).mean()
    data['SMA50'] = data['Close'].rolling(50).mean()
    data['Signal'] = 0
    data['Signal'][10:] = np.where(data['SMA10'][10:] > data['SMA50'][10:], 1, -1)
    return data

def execute_trades(data, initial_capital=INITIAL_CAPITAL):
    """
    Execution-aware backtest:
    - Applies slippage and commission
    - Tracks cash, position, total portfolio value
    """
    cash = initial_capital
    position = 0
    portfolio_values = []

    for i in range(len(data)):
        price = data['Close'].iloc[i]
        signal = data['Signal'].iloc[i]

        # Determine trade size (all-in / all-out for simplicity)
        target_position = cash if signal == 1 else -position*price  # buy or sell

        # If we need to trade
        if signal == 1 and cash > 0:
            executed_price = price * (1 + SLIPPAGE)
            shares = cash // executed_price
            cost = shares * executed_price + COMMISSION
            cash -= cost
            position += shares
        elif signal == -1 and position > 0:
            executed_price = price * (1 - SLIPPAGE)
            proceeds = position * executed_price - COMMISSION
            cash += proceeds
            position = 0

        # Portfolio value
        portfolio_value = cash + position * price
        portfolio_values.append(portfolio_value)

    data['Portfolio'] = portfolio_values
    return data

def plot_results(data):
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Close'], label='Price')
    plt.plot(data.index, data['Portfolio'], label='Portfolio Value')
    plt.title(f'Execution-Aware Backtest: {TICKER}')
    plt.xlabel('Date')
    plt.ylabel('USD')
    plt.legend()
    plt.grid(True)
    plt.show()

# -----------------------------
# MAIN
# -----------------------------
def main():
    data = fetch_data(TICKER)
    data = generate_signals(data)
    data = execute_trades(data)
    print(data[['Close', 'SMA10', 'SMA50', 'Signal', 'Portfolio']].tail(10))
    plot_results(data)

if __name__ == "__main__":
    main()