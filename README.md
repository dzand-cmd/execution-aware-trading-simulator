# Execution-Aware Backtesting Framework

**Author:** dzand-cmd  
**Project Type:** Quantitative Research / Algorithmic Trading  
**Language:** Python  
**Status:** Complete 

---

## Overview

This project implements an execution-aware backtesting engine in Python that evaluates trading strategies using historical market data. Unlike basic backtests, this system incorporates real-world trading frictions such as slippage and commissions, providing a more realistic view of strategy performance.

The backtester uses a simple moving average crossover strategy to generate signals and simulates trade execution while tracking portfolio value over time.

---

## Features

* Historical market data retrieval using Yahoo Finance
* Signal generation via moving average crossover (SMA10 vs SMA50)
* Execution-aware trade simulation
* Slippage and commission modeling
* Portfolio value tracking over time
* Visualization of price vs portfolio performance

---

## System Design

The system is structured around three core components:

* **Data Layer**: Fetches historical price data using `yfinance`
* **Signal Engine**: Generates buy/sell signals based on SMA crossover
* **Execution Engine**: Simulates trades with slippage and transaction costs while updating cash and positions

---

## Strategy Logic

* Compute:

  * 10-day moving average (SMA10)
  * 50-day moving average (SMA50)

* Generate signals:

  * **Buy (1)** when SMA10 > SMA50
  * **Sell (-1)** when SMA10 ≤ SMA50

* Execution assumptions:

  * All-in / all-out position sizing
  * Slippage applied to execution price
  * Fixed commission per trade

---

## Example Workflow

1. Fetch historical price data for a given ticker
2. Compute technical indicators (SMA10, SMA50)
3. Generate trading signals
4. Execute trades with slippage and commission
5. Track portfolio value over time
6. Visualize results

---

## How to Run

1. Install dependencies:

   ```bash
   pip install yfinance pandas numpy matplotlib
   ```

2. Run the script:

   ```bash
   python execution_aware_backtester.py
   ```

---

## Output

* Tabular view of recent data including:

  * Price
  * Indicators (SMA10, SMA50)
  * Signals
  * Portfolio value

* Plot showing:

  * Asset price
  * Portfolio performance over time

---

## Why This Matters

Most basic backtests ignore execution costs, leading to overly optimistic results. This project introduces realistic trading frictions such as slippage and commissions, making performance evaluation more aligned with real-world trading conditions.

It demonstrates key concepts in quantitative finance:

* Strategy evaluation
* Execution modeling
* Portfolio tracking

---

## Limitations

* Uses simple all-in / all-out position sizing
* No risk management or position scaling
* Limited to a single asset
* No intraday or high-frequency modeling
* No transaction latency

---

## Future Improvements

* Add position sizing and risk management
* Support multi-asset portfolios
* Introduce event-driven architecture
* Incorporate more advanced execution models
* Add performance metrics (Sharpe ratio, drawdown)
* Optimize for speed and scalability

---

## Key Takeaway

This project highlights the importance of incorporating execution costs into backtesting. By modeling slippage and commissions, it provides a more realistic framework for evaluating trading strategies and serves as a strong foundation for building more advanced quantitative trading systems.
