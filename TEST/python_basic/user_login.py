f=open("user",'r')

#确定数据存储信息格式
#账号数据读到内存，为了方便可以改成list，不过字段更为方便
account={
    #lin1:[lin1,000000,1]
}
for line in f:
    line = line.strip().split(",")
    # print(line[0],line[1])
    account[line[0]] = line #这种列表转字典的写法要学习一下
print(account)
#
# #通过循环去判断信息准确性,count主要是控制密码输错的次数
while True:
    username = input("enter your username").strip()
    if username not in account:
        print("not sign".center(10,"-"))
    elif account[username][2] == "1":
        print("lock".center(20,"-"))
        continue

    else:
        count = 0
        while count < 3:#控制密码输错次数
            password = input("enter your password").strip()
            if password == account[username][1]:
                print(f"welcome {username}登录成功.....")
                break
            else:
                print("wrong password")
            count += 1


        if count == 3:
            print(f"输错了{count}次密码，需要锁定账号{username}....")
            #先修改内存中dict的数据
            #再按照原格式写入源文件
            account[username][2] = "1"
            f2 = open("user","w")
            for username,val in account.items():
                line = ",".join(val)+'\n'#把列表再转成字符
                # print(line)
                f2.write(line)
            f2.close()
        # break
        exit("bye")


