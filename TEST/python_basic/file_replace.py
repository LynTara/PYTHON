import sys
#argv可以执行脚本时传任何参数

old_str = sys.argv[1]
new_str = sys.argv[2]
file_name = sys.argv[3]

f = open(file_name,"r+")
data = f.read()
old_str_count = data.count(old_str)
print(old_str_count)
new_data = data.replace(old_str,new_str)

f.seek(0)
# f.truncate()

f.write(new_data)
f.close()


print(f"成功替换{old_str} to {new_str},共计{old_str_count}处")