# password = "a123456"
# i=3
# while True:
#     pw=input("entry your password:")
#     if pw == password:
#         print("success")
#         break
#     else:
#         i = i-1
#         print("password error, you have ",i,"chance")
#         if  i==0:
#             print("lock your account!")
#             break

import random
start=input("start number:")
end=input("end number")
start = int(start)
end = int(end)
r=random.randint(start,end)
count = 0


while True:
    count = count + 1
    num = input("enter your number:")
    num = int(num)
    if num == r:
        print("You've got it")
        print(count,"times")
        break
    elif num > r :
        print("it is bigger than random number")
    elif num < r :
        print("it is smaller than random number")
    print(count,"times")