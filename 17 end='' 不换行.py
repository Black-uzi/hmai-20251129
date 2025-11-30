print("Hello ", end='')
print("World", end='')
print("")

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j:2d}", end='    ')
        j += 1
    print()
    i += 1
