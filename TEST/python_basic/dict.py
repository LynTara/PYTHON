dict = {'lin1': ['lin1', '111', '1'], 'lin2': ['lin2', '111', '1'], 'lin3': ['lin3', '111', '1'], 'lin4': ['lin4', '111', '0'], 'lin5': ['lin5', '111', '0']}


# for item,val in dict.items():
#     # print(item)
#     print(dict[item][2])
#
#     info = input("enter some info")
#     if info in val:
#         print(f"item:{item}   val:{val}")
#     break
# #     # print(val)
# #     print(dict[item][1])
# #     # lin = ",".join(val)
# #     # print(lin)

# select_price_info = input("输入你的筛选条件").strip()
# price = select_price_info.split('>')
# print(price[0],price[1])

price = "价格 > 50"
if ">" in price:
    print(price)
else:
    print("mpomooo")
