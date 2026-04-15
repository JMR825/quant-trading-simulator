import numpy as np

# STEP 1: Data
prices = np.array([100, 102, 101, 105, 110, 108])

# STEP 2: Returns
returns = np.diff(prices) / prices[:-1]

# STEP 3: Signals (simple momentum)
signals = np.where(returns > 0, 1, -1)
signals = np.insert(signals, 0, 0)

# STEP 4: Volatility (simple proxy)
vol = np.std(returns)
size = 1 / vol

# STEP 5: Position
position = signals * size

# STEP 6: PnL
pnl = position[1:] * returns

# STEP 7: Equity
equity = np.exp(np.cumsum(pnl))

# STEP 8: Metrics
sharpe = np.mean(pnl) / np.std(pnl)
win_rate = np.sum(pnl > 0) / len(pnl)
profit_factor = np.sum(pnl[pnl > 0]) / abs(np.sum(pnl[pnl < 0]))

print("PnL:", pnl)
print("Equity:", equity)
print("Sharpe:", sharpe)
print("Win Rate:", win_rate)
print("Profit Factor:", profit_factor)