def bmi(weight,high):
    total = weight/(high**2)
    return total

def rb(b):
    if b < 18.5:
        print("น้ำหนักต่ำกว่าเกณฑ์")
    elif b >= 18.5 and b <= 22.90:
        print("ปกติ")
    elif b >= 23 and b <= 24.90:
        print("ท้วม/โรคอ้วนระดับ1")
    elif b >= 25 and b <= 29.90:
        print("อ้วน/โรคอ้วนระดับ2")
    elif b > 30:
        print("อ้วนมาก/โรคอ้วนระดับ3")

w = float(input("น้ำหนัก(Kg) = "))
h = float(input("ส่วนสูง(M) = "))
#total = bmi(w,h)
#print(f"Bmi = {total:.2f}")
print("Bmi = %.2f" % bmi(w,h))
rb(bmi(w,h))