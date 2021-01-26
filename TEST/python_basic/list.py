name = ["张一","张二"]
name.append("张三")
name.append("张三")

if "张三" in name:
    name_index=name.index("张三")
    name[name_index]="张八八八"
print(name)

name.insert(2,"张五")
print(name)

name.pop(1)
print(name)

name.clear()
print(name)

#不知道元素在列表位置的情况下，如何修改
#先判断是否存在列表，item in list
#取索引，item_index=name.index("aa")
#去修改，list[item_index]=”bbb“


n = ['张一',['张二', '张五'], '张二', '张五', '张八八八', '张三']
print(n[:2])
print(n[0:-1:3])
print(n[0::3])
n = ['张一',['张二', '张五'], '张二', '张五', '张八八八', '张三']
n.remove(n[1])
print(n)
n.sort()
print(n)
n.reverse()
print(n)

for i in enumerate(n):
    print(i[0],i[1])
