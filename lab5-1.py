w = float(input("รับค่ากว้าง = "))
l = float(input("รับค่ายาว = "))

def rectangle(w,l):
    area = w*l
    return area

#area = rectangle(w,l)
print("Answer = %.2f" % rectangle(w,l))
#print(f"Answer = {area:.2f}")