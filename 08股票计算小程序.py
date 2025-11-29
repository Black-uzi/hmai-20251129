name = "传智播客"
# 当前股价
stock_price = 19.99
# 股票代码
stock_code = "003032"
#股票每日增长系数 浮点数类型 1.2
spdgf = 1.2
#增长天数
growth_days = 7
# 最终股价 当前股价 * 增长系数 ** 增长天数， 用来计算最终股价哦
final_stock_price = stock_price * spdgf ** growth_days

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f"% (spdgf,growth_days,final_stock_price))
