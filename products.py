products = []
#---------------------------------------------------
with open("products.csv","r",encoding="utf-8") as f:
    for line in f:
        s = line.strip().split(",") 
        if "商品名稱,商品價格" in line: # 如果"商品名稱,商品價格" 存在 line
            continue # 跳過
        print(s)
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
with open("products.csv","w",encoding="utf-8") as f:
    f.write("商品名稱,商品價格\n")
    for g in products:
        f.write(g[0] + "," + str(g[1]) + "\n")    