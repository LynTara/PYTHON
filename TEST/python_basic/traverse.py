
f=open("联系方式",mode="r",encoding="utf-8")
# print(f.readlines()) #可以看到每一行都有换行符
for line in f:
    # print(line,end="")#end=''去除换行符
    line = line.split()
    height = line[3]
    weight = line[4]
    if int(height) >= 170 and int(weight) < 50:
        print(line)
    # continue 这个无关紧要


#怎么每一行转成列表  使用split()
#字段值可以在取值时转int或者判断的时候加int强制转
#如果文件中存在空行，取值时取不到也会出现报错
