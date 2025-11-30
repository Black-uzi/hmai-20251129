num = 100

def testA():
    print(num)

def testB():
    global num
    num = 200
    print(num)

testA()
testB()

print(num)