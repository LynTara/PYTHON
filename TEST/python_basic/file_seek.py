f=open("file_seek_write","w")
f.write("aaaaa\n")
f.write("bbbbb\n")
print("当前所在位置",f.tell())
f.write("ccccc\n")
print("当前所在位置",f.tell())
f.seek(14)
f.write("*****")