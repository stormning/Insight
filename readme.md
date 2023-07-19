# 洞见（Insight）
洞悉市场行情，把握市场热点
## 财务分析指标:市盈率、市净率、市销率
Price 股票价格
### 市盈率 df["PE"] = df["Price"] / df["EPS"]
EPS一般指每股收益
### 市净率 df["PB"] = df["Price"] / df["Book Value"]
Book Value股票账面价值，是指按照会计核算的原理和方法反映计量的企业价值
### 市销率 df["PS"] = df["Price"] / df["Sales"]
Sales公司主营业务收入
### 板块流动性指数
df["Liquidity"] = df["Volume"] / df["Market Cap"]
成交量/总市值

