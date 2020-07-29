import os

products = []
products2 = []

#檢查檔案是否存在
if os.path.isfile("products.csv"):
    print("找到了檔案")
#讀取已寫入的檔案
    with open("products.csv","r",encoding="utf-8") as f:
        for line in f:
            name,price = line.strip().split(",") 
            if "商品名稱,商品價格" in line: # 如果"商品名稱,商品價格" 存在 line
                continue # 跳過
            products2.append([name,price])
    print(products2)
else:
    print("找不到了檔案")
        
#讓使用者輸入
while True:
    name = input("請輸入商品名稱:")
    if name =="q":
        break
    price = input("請輸入商品價格:")
    price = int(price)
    products.append([name,price])
print(products)

#印出所有購買記錄
for p in products:
    print(p[0],"價格是",p[1])

#寫入檔案
with open("products.csv","w",encoding="utf-8") as f:
    f.write("商品名稱,商品價格\n")
    for g in products:
        f.write(g[0] + "," + str(g[1]) + "\n")    