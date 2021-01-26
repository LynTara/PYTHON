f = open("user","r")
account = {

}

for line in f:
    line = line.strip().split(',')#转成列表
    account[line[0]] = line#转成字典
print(account)

while True:
    #判断用户名是否存在，如果不存在提醒未注册
    username = input("enter your username:  ").strip()
    if username not in account:
        print("not signed".center(10,'-'))
    #校验用户名是否锁定
    elif account[username][2] == "1":
        print("locked".center(10,"-"))
        continue
    else:
        # 判断密码是否输入正确
        count = 0 #输入次数限制
        while count < 3:
            password = input("enter your passwprd:  ").strip()
            if password == account[username][1]:
                print(f"welcome,{username}".center(10,"-"))
                exit("bye")
            else:
                print("wrong password".center(10,"-"))
            count += 1

        if count == 3:#次数超限，用户锁定
            print(f"{username} will be locked".center(10,"-"))
            #更改用户锁定状态
            account[username][2] = "1"#需输入字符格式的“1”,出错问题很难找

            #写入文件,以源文件形式
            f1 = open("user","w")
            for item,val in account.items():#转成列表
                line = ",".join(val)#列表转字符
                f1.write(line)
            f1.close()
        exit("byebye")





