# Execution-Aware Trading Simulator

**Author:** Dzandu Selorm(dzand-cmd)  
**Project Type:** Quantitative Trading  
**Language:** Python  
**Status:** Complete 

---


## Overview

This project implements an execution-aware trading simulator that models how trading strategies behave under realistic market execution constraints. It simulates order placement, partial fills, slippage, and execution delays to bridge the gap between theoretical signals and real-world trading performance.

The objective is to evaluate how execution frictions impact strategy profitability and risk-adjusted returns.

---


## Project Structure

execution-aware-trading-simulator/
│
├── src/
│   ├── execution_aware_trading_simulator.py      # Core execution simulation loop
├── README.md            # Project documentation


## Features

- Historical market data retrieval using Yahoo Finance
- Signal generation via moving average crossover (SMA10 vs SMA50)
- Execution-aware trade simulation
- Slippage and commission modeling
- Portfolio value tracking over time
- Visualization of price vs portfolio performance

---


## Core Features

- Order lifecycle simulation:
 - Order creation
 - Submission
 - Execution
 - Completion / cancellation
- Execution modeling:
 - Partial fills
 - Slippage modeling
 - Fill probability approximation
 - Market impact estimation
- Strategy integration:
 - Signal-driven order generation
 - Strategy plug-in structure
- Performance metrics:
 - PnL tracking
 - Sharpe ratio
 - Execution cost analysis
 - Fill ratio 


## Methodology

This simulator bridges strategy signals with real-world execution constraints:

- A trading signal is generated
- The strategy converts it into an order
- Orders are submitted to the simulator
- Execution logic determines:
- Fill timing
- Fill quantity
- Execution price (including slippage)
- Portfolio performance is updated over time

## Key idea:

A profitable signal can become unprofitable after realistic execution cost


## How To Run 

git clone https://github.com/dzand-cmd/execution-aware-trading-simulator.git
cd execution-aware-trading-simulator
python execution_aware_trading_simulator.py




