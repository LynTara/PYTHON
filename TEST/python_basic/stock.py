f = open("stock_data_2","r",encoding='utf-8')

company = {

}
#把txt转为dict格式，存取比较方便
for line in f:
    line = line.strip().split(',')
    company[line[0]] = line
print(company)

#通过股票名模糊查询股票信息
comp_info = input("enter you company info").strip()
#这种方法只能精确查询，不能模糊查询
# if comp_info not in company:
#     print("not in data")
# else:
#     print(company[comp_info])
#模糊查询改善
#定位到具体company_name
for item,val in company.items():
    if comp_info in val:
        print(f"股票代码:{item}  股票信息:{val}")
        break
        # print(company[item][2])
    else:
        print("未查询到相关股票的信息")



#根据股票价格，涨跌幅，换手率这几列进行信息筛选，比如输入价格>50，不用判断等于
#尝试写根据股票价格的筛选
# price > 50

select1 = input("输入你的筛选条件")
select = select1.strip().split('>', 1)
select_info = select[0] #价格
select_num = select[1]  #50
dict = ["股票价格","涨跌幅","换手率"]
# print(f"price>{select_num}的股票：")
#进入大于判断
while True:
    if select_info not in dict:
        print("筛选条件不正确")
        break
    else:
        for item,val in company.items():
            if ">" in select1:
                if select_info == dict[0]:
                    if company[item][2] > select_num:
                        print(f"股票代码:{item}  股票信息:{val}")
                        continue
                if select_info == dict[1]:
                    if company[item][3] > select_num:
                        print(f"股票代码:{item}  股票信息:{val}")
                        break
                else:
                    if select_info == dict[2]:
                        if company[item][8] > select_num:
                            print(f"股票代码:{item}  股票信息:{val}")
                            break
            else:
                if select_info == dict[0]:
                    if company[item][2] < select_num:
                        print(f"股票代码:{item}  股票信息:{val}")
                        break
                if select_info == dict[1]:
                    if company[item][3] < select_num:
                        print(f"股票代码:{item}  股票信息:{val}")
                        break
                else:
                    if select_info == dict[2]:
                        if company[item][8] < select_num:
                            print(f"股票代码:{item}  股票信息:{val}")
                            break




