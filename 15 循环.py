# while
# for

# break
# continue

# i = 0
# while i < 10:
#     print(f"嘻嘻{i}")
#     i += 1


import random

# def guess_number_game():

print("欢迎来到猜数字游戏！")
print("我已经想了一个1~100之间的数字，请猜出它是什么。")
print("没有次数限制，直到猜对为止！")
print("-" * 40)

num = random.randint(1, 100)
print(num)

attempts = 0

while True:
    attempts += 1
    print(f"\n 第 {attempts} 次尝试")

    guessNumber = int(input("请输入你猜的数字（1-100）："))

    try:
        if guessNumber < 1 or guessNumber > 100:
            print("数字不对，请输入1~10之间的数字！")
            continue

        if guessNumber == num:
            print(f"🎉 恭喜你！猜对了！数字就是 {num}！")
            print(f"你用了 {attempts} 次尝试猜中了这个数字！")
            break
        elif guessNumber < num:
            print(f"❌ 猜错了！数字比 {guessNumber} 大，请再试一次")
        else:
            print(f"❌ 猜错了！数字比 {guessNumber} 小，请再试一次")
    except ValueError:
        print("请输入有效数字")

print("\n游戏结束！感谢游玩！")


# if __name__ = "_main_":
#     guess_number_game()