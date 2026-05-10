import numpy as np
def load_stock_data(filepath):
    data = np.genfromtxt(
        filepath,
        delimiter=',',
        skip_header=1,
        usecols=(1, 2, 3, 4, 5)
    )
    return data
def extract_columns(data):
    open_price  = data[:, 0]
    high_price  = data[:, 1]
    low_price   = data[:, 2]
    close_price = data[:, 3]
    volume      = data[:, 4]
    return open_price, high_price, low_price, close_price, volume
def clean_data(data):
    nan_mask = np.isnan(data).any(axis=1)
    clean = data[~nan_mask]
    print(f"Removed {nan_mask.sum()} bad rows.")
    return clean

def moving_average(prices, window):
    kernel = np.ones(window) / window
    ma = np.convolve(prices, kernel, mode='valid')
    return ma
def calculate_all_averages(close_price):
    ma7  = moving_average(close_price, 7)
    ma20 = moving_average(close_price, 20)
    ma50 = moving_average(close_price, 50)
    return ma7, ma20, ma50
def print_averages(close_price, ma7, ma20):
    print(f"Latest Close Price : ${close_price[-1]:.2f}")
    print(f"7-Day  Moving Avg  : ${ma7[-1]:.2f}")
    print(f"20-Day Moving Avg  : ${ma20[-1]:.2f}")

def calculate_daily_returns(close_price):
    returns = np.diff(close_price) / close_price[:-1]
    returns_pct = returns * 100
    return returns_pct
def calculate_volatility(returns):
    daily_vol  = np.std(returns)
    annual_vol = daily_vol * np.sqrt(252)
    return daily_vol, annual_vol
def calculate_stats(close_price, returns):
    stats = {
        'max_price'    : np.max(close_price),
        'min_price'    : np.min(close_price),
        'avg_price'    : np.mean(close_price),
        'best_day'     : np.max(returns),
        'worst_day'    : np.min(returns),
        'positive_days': np.sum(returns > 0),
        'negative_days': np.sum(returns < 0)
    }
    return stats
def print_stats(stats, daily_vol, annual_vol):
    print("\n===== STOCK ANALYSIS REPORT =====")  
    print(f"Max Price     : ${stats['max_price']:.2f}")
    print(f"Min Price     : ${stats['min_price']:.2f}")
    print(f"Avg Price     : ${stats['avg_price']:.2f}")
    print(f"Best Day      : +{stats['best_day']:.2f}%")
    print(f"Worst Day     : {stats['worst_day']:.2f}%")
    print(f"Positive Days : {stats['positive_days']}")
    print(f"Negative Days : {stats['negative_days']}")
    print(f"Daily Volatility  : {daily_vol:.2f}%")
    print(f"Annual Volatility : {annual_vol:.2f}%")

