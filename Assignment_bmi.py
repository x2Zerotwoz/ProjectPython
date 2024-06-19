print("โปรแกรมคำนวณค่าดัชนีมวลกาย(BMI)")
weight = int(input("น้ำหนัก(กิโลกรัม) : "))
high = int(input("ส่วนสูง(เซนติเมตร) : "))
bmi = weight/(high/100)**2
if bmi < 18.50:
    print("น้ำหนักน้อย")
elif bmi >= 18.50 and bmi <= 22.90:
    print("ปกติ(สุขภาพดี)")
elif bmi >= 23 and bmi <= 24.90:
    print("ท้วม/โรคอ้วนระดับ1")
elif bmi >= 25 and bmi <= 29.90:
    print("อ้วน/โรคอ้วนระดับ2")
elif bmi > 30:
    print("อ้วนมาก/โรคอ้วนระดับ3")