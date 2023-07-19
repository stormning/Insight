# 洞见（Insight）
洞悉市场行情，把握市场热点
## 财务分析指标
Price 股票价格
### 市盈率
df["PE"] = df["Price"] / df["EPS"]
EPS一般指每股收益
### 市净率
df["PB"] = df["Price"] / df["Book Value"]
Book Value股票账面价值，是指按照会计核算的原理和方法反映计量的企业价值
### 市销率
df["PS"] = df["Price"] / df["Sales"]
Sales公司主营业务收入
### 流动性指数
df["Liquidity"] = df["Volume"] / df["Market Cap"]
成交量/总市值
### 投资价值指数
PE、PB、PS 均值，TODO 更科学的算法
df["Investment Value"] = (df["PE_Rank"] + df["PB_Rank"] + df["PS_Rank"]) / 3
### 估值具有投资价值
df = df[df["Investment Value"] <= 0.75]
### 筛选出流动性较好的
df = df[df["Liquidity"] >= 0.05]
### 根据技术指标过滤
MACD>0  RSI<70
### 综合得分
df["Score"] = df["Investment Value"] * df["Liquidity"] * df["MACD"] * df["RSI"]




