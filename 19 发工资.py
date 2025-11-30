# 某公司，账户余额有1W元，给20名员工发工资。
# 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
# 领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
# 如果工资发完了，结束发工资。


import random

money = 10000
for i in range(1,21):
    if money <= 0:
        print("工资发完了")
        break
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i} 绩效分{num} 不发工资")
    else:
        money -= 1000
        print(f"向员工{i}发放工资1000元 账户余额{money}元")


