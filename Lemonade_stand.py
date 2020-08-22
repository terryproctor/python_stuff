sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
sales_w2_6= int(input('Sales for Sunday week 2: '))
sales_w2.append(sales_w2_6)
sales = sales_w1 + sales_w2

print(sorted(sales))

print(f"max sales: {max(sales)}")
print(f"max sales: {min(sales)}")