import random
#先列举一个300的列表，代表300名员工
num = []
for i in range(3):
    for j in range(100):
        if j < 10:
            num.append(f"{i}0{j}")
        else:
            num.append(f"{i}{j}")
print(num)
n3 = random.sample(num,30)
print("三等奖获得者分别是:")
for a in range(30):
    print(f"{n3[a]}",end=" \n")
    num.remove(n3[a])
n2 = random.sample(num,6)
print("二等奖获得者分别是:")
for a in range(6):
    print(f"{n2[a]}", end=" \n")
    num.remove(n2[a])
n1 = random.sample(num,3)
print("一等奖获得者分别是:")
for a in range(3):
    print(f"{n1[a]}", end=" \n")
    num.remove(n1[a])










