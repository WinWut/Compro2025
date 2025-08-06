txt=str(input("ป้อนรหัสลับ: "))

sumn=0
num=""

for char in txt:

    if char.isdigit():
        num+=char
    else:
        if num:
            sumn+=int(num)
            num=""
if num:
    sumn+=int(num)
print("ผลลัพธ์:",sumn)