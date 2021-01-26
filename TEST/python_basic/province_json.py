# province=[]
# city=[]
dict=[
['王*龙', '北京市海淀区苏州街大恒科技大厦南座4层'],
['庞*飞', '北京市昌平区汇德商厦四楼403'],
['顾*锐', '江苏省扬州市三垛镇工业集中区扬州市立华畜禽有限公司'],
['王*飞', '上海市徐汇区上海市徐汇区H88越虹广场B座5E'],
['华*升', '北京市海淀区杰睿大厦']
]
pro_json=[]
city_json=[]
#首先把dict内地址取出来
for aa in enumerate(dict):
    dic = aa[1]
    address = dic[1]
    # print(address)
    if "省" in address:
        # province.append(address)
        add = address.split('省',1)
        pro_json.append(add[0])
        continue
    else:
        # city.append(address)
        add = address.split('市', 1)
        city_json.append(add[0])
#取出列表内所有的省市
pro_list=list(set(pro_json))
# print(pro_list)

pro_list = ['宁夏银川', '湖北', '天津', '山西', '内蒙古呼和浩特', '新疆乌鲁木齐', '河南', '青海', '陕西', '海南', '辽宁', '甘肃', '吉林', '河北', '上海', '北京', '山东', '江苏', '黑龙江', '浙江', '安徽']
# 拿出每个省份去对比查询地址，分类存放
