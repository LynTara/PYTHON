a = "lyntara"

print(a.center(50,"-"))
print(a.count("a"))
print(a.count("a",0,5))

print(a.endswith("a"))
print("-----------------------------")
if a.startswith("a"):
    print("true")
print("false")
print("-----------------------------")

print(a.find("n"))#查不到返回-1 查到了返回字符索引

print(a.isdigit())
print("23",a.isdigit())

l = ["a","bbb","cc"]
print("-".join(l))


print(a.replace("a","p",1))#字符串替换

a = "lyntara   "
print(a.strip())


