#หาพื้นที่สามเหลี่ยม 1/2*ฐาน*สูง
def tringle(base, high):
    area = 1/2*base*high
    #print("พื้นที่สามเหลี่ยม %.2f" % area)
    return area  
#print(tringle(2,3))
print("พื้นที่สามเหลี่ยม %.2f" % tringle(4,5))