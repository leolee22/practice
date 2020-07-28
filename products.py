products = []
#---------------------------------------------------
while True:
    name = input("請輸入商品名稱:")
    if name =="q":
        break
    price = input("請輸入商品價格:")
    price = int(price)
    products.append([name,price])
print(products)

#---------------------------------------------------
for p in products:
    print(p[0],"價格是",p[1])

#---------------------------------------------------
with open("products.csv","w") as f:
    for g in products:
        f.write(g[0] + "," + str(g[1]) + "\n")    