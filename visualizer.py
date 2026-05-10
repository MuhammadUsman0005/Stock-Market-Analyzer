import numpy as np
import matplotlib.pyplot as plt
def generate_signals(close_price, ma7, ma20):
    min_len = min(len(ma7), len(ma20))
    ma7_trim  = ma7[-min_len:]
    ma20_trim = ma20[-min_len:]
    signal = np.where(ma7_trim > ma20_trim, 1, -1)
    return signal, ma7_trim, ma20_trim
def plot_price_and_ma(close_price, ma7, ma20, ma50):
    plt.figure(figsize=(14, 8))
    plt.subplot(2, 1, 1)
    plt.plot(close_price, label='Close Price',
             color='black', linewidth=1.5)
    plt.plot(range(6,  len(ma7)+6),  ma7,
             label='7-Day MA',  color='blue')
    plt.plot(range(19, len(ma20)+19), ma20,
             label='20-Day MA', color='orange')
    plt.plot(range(49, len(ma50)+49), ma50,
             label='50-Day MA', color='red')
    plt.title('Stock Price + Moving Averages')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.subplot(2, 1, 2)
    returns = np.diff(close_price) / close_price[:-1] * 100
    colors = np.where(returns >= 0, 'green', 'red')
    plt.bar(range(len(returns)), returns, color=colors)
    plt.title('Daily Returns %')
    plt.axhline(y=0, color='black', linewidth=0.8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('stock_analysis.png', dpi=150)
    plt.show()
    print("Chart saved as stock_analysis.png")