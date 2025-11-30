import random

number = random.randint(1, 10)

print(f"数字为{number}")

# print(number)
guess1 = int(input("请输入一个1-10数字"))

# 等于
if guess1 == number:
    print("第一次就猜对了")
    print(f"数字为{guess1}")

# 猜小了
elif guess1 < number:
    print("小了")
    print("还有两次机会")
    guess2 = int(input(f"请输入一个比{guess1}大的数字"))

    if guess2 == number:
        print("第二次就猜对了")
        print(f"数字为{guess2}")

    if guess2 < number:
        print("小了")
        print("还有一次机会")
        guess3 = int(input(f"请输入一个比{guess2}大的数字"))
        if guess3 == number:
            print("第三次猜对了")
            print(f"数字为{guess3}")
        else:
            print("没猜对")
            print(f"数字为{number}")

    if guess2 > number:
        print("大了")
        print("还有一次机会")
        guess3 = int(input(f"请输入一个比{guess2}小 比{guess1}大的数字"))
        if guess3 == number:
            print("第三次猜对了")
            print(f"数字为{guess3}")
        else:
            print("没猜对")
            print(f"数字为{number}")

# 猜大了
else:
    print("大了")
    print("还有两次机会")
    guess2 = int(input(f"请输入一个比{guess1}小的数字"))

    if guess2 == number:
        print("第二次就猜对了")
        print(f"数字为{guess2}")

    if guess2 < number:
        print("小了")
        print("还有一次机会")
        guess3 = int(input(f"请输入一个比{guess2}大 比{guess1}小的数字"))
        if guess3 == number:
            print("第三次猜对了")
            print(f"数字为{guess3}")
        else:
            print("没猜对")
            print(f"数字为{number}")

    if guess2 > number:
        print("大了")
        print("还有一次机会")
        guess3 = int(input(f"请输入一个比{guess2}小的数字"))
        if guess3 == number:
            print("第三次猜对了")
            print(f"数字为{guess3}")
        else:
            print("没猜对")
            print(f"数字为{number}")