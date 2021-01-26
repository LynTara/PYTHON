f = open("wb_file","wb")

s="猪宝"
print(s.encode("utf-8"))
f.write("文本无法写入，只能写入byte")
f.write(s.encode("utf-8"))#只是以字节形式写入，实质还是文本，文本会以utf-8形式打开