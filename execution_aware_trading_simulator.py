import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TICKER = "AAPL"
PERIOD = "2y"
INITIAL_CAPITAL = 100000
SLIPPAGE_BPS = 5     
COMMISSION = 1.0
LATENCY = 1    


def fetch_data(ticker, period="2y"):
    data = yf.Ticker(ticker).history(period=period)
    if data.empty:
        raise ValueError("No data fetched")

    return data

def generate_signals(data):
    data = data.copy()
    data["SMA10"] = data["Close"].rolling(10).mean()
    data["SMA50"] = data["Close"].rolling(50).mean()
    data["signal_raw"] = np.where(data["SMA10"] > data["SMA50"],1,-1)
    data["signal"] = data["signal_raw"].shift(LATENCY)
    data["signal"] = data["signal"].fillna(0)

    return data

def execute_backtest(data):
    cash = INITIAL_CAPITAL
    position = 0
    portfolio = []
    trades = []

    for i in range(len(data)):
        price = data["Close"].iloc[i]
        signal = data["signal"].iloc[i]
        slippage = SLIPPAGE_BPS / 10000

        # -------------------------
        # BUY SIGNAL
        # -------------------------
        if signal == 1 and cash > 0:
            exec_price = price * (1 + slippage)
            shares = cash // exec_price
            if shares > 0:
                cost = shares * exec_price + COMMISSION
                cash -= cost
                position += shares

                trades.append({
                    "type": "BUY",
                    "price": exec_price,
                    "shares": shares,
                    "cash": cash
                })

        # -------------------------
        # SELL SIGNAL
        # -------------------------
        elif signal == -1 and position > 0:
            exec_price = price * (1 - slippage)
            proceeds = position * exec_price - COMMISSION
            cash += proceeds

            trades.append({
                "type": "SELL",
                "price": exec_price,
                "shares": position,
                "cash": cash
            })

            position = 0

        portfolio_value = cash + position * price
        portfolio.append(portfolio_value)

    data["portfolio"] = portfolio

    return data, pd.DataFrame(trades)

def performance_metrics(portfolio):
    returns = portfolio.pct_change().dropna()
    sharpe = np.sqrt(252) * returns.mean() / returns.std()
    cumulative = (1 + returns).cumprod()
    drawdown = cumulative / cumulative.cummax() - 1
    max_dd = drawdown.min()

    return {
        "Sharpe": sharpe,
        "Max Drawdown": max_dd,
        "Final Value": portfolio.iloc[-1]
    }

def plot_results(data):
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data["Close"], label="Price")
    plt.plot(data.index, data["portfolio"], label="Portfolio")
    plt.title("Execution-Aware Backtest (Improved)")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    data = fetch_data(TICKER)
    data = generate_signals(data)
    data, trades = execute_backtest(data)
    metrics = performance_metrics(data["portfolio"])

    print("\nPERFORMANCE METRICS:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    print("\nLAST TRADES:")
    print(trades.tail())

    plot_results(data)


if __name__ == "__main__":
    main()