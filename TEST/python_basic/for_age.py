age = 20
for i in range(3):
    guess = int(input("enter a age: "))
    if guess > age:
        print("太大啦太大啦")
    elif guess < age:
        print("太小啦太小啦")
    else:
        exit("yesyesyes")
        #最后一个可以用exit