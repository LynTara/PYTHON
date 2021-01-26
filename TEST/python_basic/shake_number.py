#允许用户选3次
#每次放出20个车牌供用户选择
#京【A-Z】-【xxxxx】,数字和字母组合

# random.choice()
# random.sample()
# random.randint()
#随机数 random()  string() join()
import random
import string

count  = 0
while count < 3:
    car_num = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_letters+string.digits,5))
        c_num = (f"京{n1}.{n2}")
        car_num.append(c_num)
        print(c_num)
    choice = input("输入你喜欢的号").strip()#strip会把空格和换行都去掉
    if choice in car_num:
        print("恭喜你选择新车牌")
        exit("good lucks")
    else:
        print("不合法的选择....")
    count +=  1







