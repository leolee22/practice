import os


def user_read(filename):
    products = []
    #讀取已寫入的檔案
    with open(filename,"r",encoding="utf-8") as f:
        for line in f:
            if "商品名稱,商品價格" in line: # 如果"商品名稱,商品價格" 存在 line
                continue # 跳過
            name,price = line.strip().split(",") 
            products.append([name,price])
    return products

        
#讓使用者輸入
def user_input(products):
    while True:
        name = input("請輸入商品名稱:")
        if name =="q":
            break
        price = input("請輸入商品價格:")
        price = int(price)
        products.append([name,price])
    print(products)
    return products

#印出所有購買記錄
def user_print(products):
    for p in products:
        print(p[0],"價格是",p[1])

#寫入檔案
def user_write(filename,products):
    with open(filename,"w",encoding="utf-8") as f:
        f.write("商品名稱,商品價格\n")
        for g in products:
            f.write(g[0] + "," + str(g[1]) + "\n")    

def main():
    filename = "text.csv"
    if os.path.isfile(filename):
        print("找到了檔案")
        products = user_read(filename)
    else:
        print("找不到了檔案")    

    products = user_input(products)
    user_print(products)
    user_write("text.csv",products)

main()
