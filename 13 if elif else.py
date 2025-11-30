print("Hello World")

height = int(input("请输入身高（cm）："))

vip_level = int(input("请输入vip等级（1-5）"))

if height < 120:
    print("身高小于120，可以免费玩")
elif vip_level > 3:
    print("vip大于3 可以免费玩")
else:
    print("不好意思 需购票10元")
print("玩的愉快")


