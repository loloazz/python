

fp = open("F:\\pythonProject\\文件的合并\\2020年数据源 .txt", "r",encoding="utf-8")



tp = open("F:\\pythonProject\\文件的合并\\2021数据集.txt", "r",encoding="utf-8")

lp = open("F:\\pythonProject\\文件的合并\\2020-2021数据集.txt", "w",encoding="utf-8")

lines = fp.readlines()

for line in lines:
    lp.write(line)

print("文件一写入成功！！")


lines2=tp.readlines()


for line in lines2:
    lp.write(line)

print("文件写入成功")


tp.close()
fp.close()
lp.close()