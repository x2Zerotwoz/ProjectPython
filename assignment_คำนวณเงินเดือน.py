def sal(s,t,l):
    to = s + (t * l)
    return to

name = str(input("ชื่อพนักงาน: "))
sala = float(input("เงินเดือนของคุณ: "))
time = int(input("ชั่วโมงล่วงเวลา: "))
l = 100

if time > 40:
    l = 150

print(name)
print(sala)
print(time)
print("total salary: %.2f" % sal(sala ,time, l))