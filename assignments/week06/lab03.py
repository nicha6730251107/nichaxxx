""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"
"""
def create_user_profile(username, age=18, premium= False):
    user_type = "Premium User" if premium else "Standard User"
    return f"{username} (age: {age}) - {user_type}"
print(create_user_profile("gg"))
print(create_user_profile("Bob", 25))
print(create_user_profile("Charis",premium=True))
