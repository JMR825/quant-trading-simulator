import numpy as np
import matplotlib.pyplot as plt

initial_capital = 10000

# STEP 1: Data
prices = np.array([120,29,399,12,222,35,290,110,286,190,219])

# STEP 2: Returns
returns = np.diff(prices) / prices[:-1]

# STEP 3: Signals (simple momentum)
signals = np.where(returns > 0, 1, -1)
signals = np.insert(signals, 0, 0)

# STEP 4: Volatility (simple proxy)
vol = np.std(returns)
size = 1 / vol

# STEP 5: Position
position = signals[-1] * size

# STEP 6: PnL
pnl = position * returns

# STEP 7: Equity
equity_curve = initial_capital * np.exp(np.cumsum(pnl))

# STEP 8: Metrics
sharpe = np.mean(pnl) / np.std(pnl)
win_rate = np.sum(pnl > 0) / len(pnl)
loss_sum = abs(np.sum(pnl[pnl < 0]))
profit_factor = np.sum(pnl[pnl > 0]) / loss_sum if loss_sum != 0 else float('inf')
print("PnL:", pnl)
print("Equity:", equity_curve)
print("Sharpe:", sharpe)
print("Win Rate:", win_rate)
print("Profit Factor:", profit_factor)

# STEP 9: EQuity Graph
plt.figure()
plt.plot(equity_curve)
plt.title("Equity Curve - Momentum Strategy")
plt.xlabel("Time")
plt.ylabel("Portfolio Value")
plt.grid()

plt.savefig("equity_curve.png")  # Upload this to LinkedIn
plt.show()