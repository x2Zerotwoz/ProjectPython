def abc(num):
    sum = 0
    for i in range(num):
        p = int(input("รับค่าราคาชิ้นที่ %d = " % (i+1)))
        sum += p
    return sum

def tax(sum):
    vat = sum * 7/100
    return vat

def total(a,b):
    t = a+b
    return t

num = int(input("จำนวนสินค้า = "))
sum = abc(num)
print(f"ราคารวม = {sum:.2f}")
print(f"ภาษี = {tax(sum):.2f}")
print(total(sum, tax(sum)))