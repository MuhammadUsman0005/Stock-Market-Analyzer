import numpy as np
from analyzer import (
    load_stock_data,
    extract_columns,
    clean_data,
    moving_average,
    calculate_all_averages,
    calculate_daily_returns,
    calculate_volatility,
    calculate_stats,
    print_stats,
    print_averages
)
from visualizer import generate_signals, plot_price_and_ma
def main():
    print("Loading data...")
    raw_data = load_stock_data('D:\Python Programms\stock-analyzer\Data\AAPL.csv')
    data     = clean_data(raw_data)
    open_p, high_p, low_p, close_p, vol = extract_columns(data)
    print("\nCalculating moving averages...")
    ma7, ma20, ma50 = calculate_all_averages(close_p)
    print_averages(close_p, ma7, ma20)
    print("\nRunning analysis...")
    returns              = calculate_daily_returns(close_p)
    daily_vol, annual_vol = calculate_volatility(returns)
    stats                = calculate_stats(close_p, returns)
    print_stats(stats, daily_vol, annual_vol)
    print("\nGenerating signals & charts...")
    signal, _, _ = generate_signals(close_p, ma7, ma20)
    buys  = np.sum(signal == 1)
    sells = np.sum(signal == -1)
    print(f"BUY  signals: {buys}")
    print(f"SELL signals: {sells}")
    plot_price_and_ma(close_p, ma7, ma20, ma50)
if __name__ == "__main__":
    main()