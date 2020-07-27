import random
start = input("start number:")
end = input("end number")
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0


while True:
    count = count + 1
    num = input("enter your number:")
    num = int(num)
    if num == r:
        print("You've got it")
        print(count, "times")
        break
    elif num > r:
        print("it is bigger than random number")
    elif num < r:
        print("it is smaller than random number")
    print(count, "times")
