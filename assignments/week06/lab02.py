""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:

รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """
def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    area = round(area, 2)
    circumference = round(circumference, 2)
    return {
        "area": area,
        "circumference": circumference
    }