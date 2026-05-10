# 📈 Stock Market Analyzer — Pure NumPy

> A fully functional stock analysis tool built from scratch using **only NumPy and Matplotlib** — no Pandas, no shortcuts, no high-level abstractions.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557c?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

---

## 🧠 Why This Project?

Most developers jump straight to Pandas for data analysis. This project deliberately avoids it — every operation is implemented using **raw NumPy matrix logic**, giving a deep understanding of how data analysis libraries work under the hood.

This is the foundation for serious Data Science and ML engineering.

---

## ✨ Features

| Feature | Description | NumPy Concept |
|---|---|---|
| 📥 Data Loading | Load CSV stock data without Pandas | `np.genfromtxt` |
| 🧹 Data Cleaning | Detect and remove missing/NaN rows | `np.isnan`, Boolean Masking |
| 📊 Moving Averages | 7-day, 20-day, 50-day trend lines | `np.convolve` |
| 📉 Daily Returns | Percentage gain/loss per day | `np.diff`, Broadcasting |
| 🌊 Volatility | Daily & annualized risk metric | `np.std`, `np.sqrt` |
| 🎯 Buy/Sell Signals | MA crossover-based signal detection | `np.where` |
| 📈 Chart Export | Price chart + returns bar chart saved as PNG | Matplotlib |

---

## 📁 Project Structure

```
stock-analyzer/
│
├── data/
│   └── stock_data.csv        # Your stock data (CSV format)
│
├── analyzer.py               # Core NumPy logic (data + calculations)
├── visualizer.py             # Signal generation + Matplotlib charts
├── main.py                   # Entry point — runs everything
└── README.md
```

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/stock-market-analyzer.git
cd stock-market-analyzer
```

**2. Install dependencies**
```bash
pip install numpy matplotlib
```

**3. Add your stock data**

Place a CSV file in the `data/` folder with this structure:
```
Date,Open,High,Low,Close,Volume
2024-01-01,150.0,155.2,148.5,153.4,1200000
2024-01-02,153.4,158.0,152.1,157.2,1350000
...
```

> 💡 Free datasets available on [Kaggle](https://www.kaggle.com/datasets?search=stock+price+csv) — search "AAPL stock CSV"

**4. Run the analyzer**
```bash
python main.py
```

---

## 📊 Sample Output

```
Loading data...
Removed 0 bad rows.

Calculating moving averages...
Latest Close Price : $161.50
7-Day  Moving Avg  : $157.23
20-Day Moving Avg  : $153.80

===== STOCK ANALYSIS REPORT =====
Max Price     : $189.30
Min Price     : $142.10
Avg Price     : $163.45
Best Day      : +3.45%
Worst Day     : -2.10%
Positive Days : 142
Negative Days : 108
Daily Volatility  : 1.23%
Annual Volatility : 19.52%

Generating signals & charts...
BUY  signals: 34
SELL signals: 16
Chart saved as stock_analysis.png
```

---

## 🔬 Key NumPy Concepts Demonstrated

```python
# Moving Average using convolution — no loops needed
kernel = np.ones(window) / window
ma = np.convolve(prices, kernel, mode='valid')

# Daily returns — vectorized math on entire array at once
returns = np.diff(close_price) / close_price[:-1] * 100

# Buy/Sell signals — conditional logic across entire array
signal = np.where(ma7 > ma20, 1, -1)

# Count positive days — boolean masking + sum trick
positive_days = np.sum(returns > 0)
```

---

## 🗺️ Roadmap

- [x] CSV data loading without Pandas
- [x] Moving averages (7 / 20 / 50 day)
- [x] Daily returns & volatility calculation
- [x] Buy/Sell signal generation
- [x] Chart export (PNG)
- [ ] RSI (Relative Strength Index) indicator
- [ ] Portfolio comparison (multiple stocks)
- [ ] Interactive Matplotlib dashboard

---

## 🧱 Built With

- **Python 3.8+**
- **NumPy** — all data operations
- **Matplotlib** — visualization & chart export

---

## 📚 What I Learned

Building this project without Pandas forced me to understand:
- How 2D array slicing works in practice on real data
- Why `np.convolve` is a mathematically elegant way to compute sliding window operations
- How boolean masking replaces complex loops entirely
- The relationship between standard deviation and financial risk

---

## 👤 Author

**Usman** — BS Artificial Intelligence Student  
📍 Pakistan  
🔗 [GitHub](https://github.com/your-username) · [LinkedIn](https://www.linkedin.com/in/muhammad-usman-256364398/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B1Kv2P4ssT7KxKNe2YuXUBQ%3D%3D)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

> *"Understanding the matrix is understanding the machine."*
