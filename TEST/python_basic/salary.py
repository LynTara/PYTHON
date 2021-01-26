salary = int(input("enter your salary:"))

if salary < 5000:
    print("钱太少")
else:
    if salary >= 10000 and salary < 20000:
        print("还行")
    else:
        print("中产了呀")