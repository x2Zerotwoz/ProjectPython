def cal_circle(rad):
    pi = 22/7
    area = pi*(rad**2)
    return area

rad = float(input("ใส่รัศมี : "))
area = cal_circle(rad)
print(f"พื้นที่วงกลม = {area:.2f}")