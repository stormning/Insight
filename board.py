import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 获取A股各大板块的行情数据
df = pd.read_csv("https://raw.githubusercontent.com/quantopian/sample-data/master/stocks/stocks.csv")

# 计算各大板块的市盈率、市净率和市销率
df["PE"] = df["Price"] / df["EPS"]
df["PB"] = df["Price"] / df["Book Value"]
df["PS"] = df["Price"] / df["Sales"]

# 计算各大板块的估值分位数
df["PE_Rank"] = df["PE"].rank(pct=True)
df["PB_Rank"] = df["PB"].rank(pct=True)
df["PS_Rank"] = df["PS"].rank(pct=True)

# 计算各大板块的投资价值指数
df["Investment Value"] = (df["PE_Rank"] + df["PB_Rank"] + df["PS_Rank"]) / 3

# 筛选出估值具有投资价值的板块
df = df[df["Investment Value"] <= 0.75]

# 计算各大板块的流动性指数
df["Liquidity"] = df["Volume"] / df["Market Cap"]

# 筛选出流动性较好的板块
df = df[df["Liquidity"] >= 0.05]

# 计算各大板块的技术指标
df["MACD"] = pd.DataFrame(df["Close"].ewm(span=12, min_periods=12).mean() - pd.DataFrame(df["Close"].ewm(span=26, min_periods=26).mean()))
df["RSI"] = pd.DataFrame(df["Close"].rolling(14).apply(lambda x: np.mean(np.power(x - x.mean(), 2)) / np.var(x)))

# 筛选出技术指标良好的板块
df = df[df["MACD"] > 0]
df = df[df["RSI"] < 70]

# 计算各大板块的综合得分
df["Score"] = df["Investment Value"] * df["Liquidity"] * df["MACD"] * df["RSI"]

# 对各大板块进行排序
df = df.sort_values("Score", ascending=False)

# 输出前十名的板块
df.head(10)