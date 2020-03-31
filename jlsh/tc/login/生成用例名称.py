#coding:'utf-8'
#测试用例名称从商品添加00001-商品添加00098
file = open(r"D:\API\jlsh\arg.txt",'w')
for a in range(1,12):
   file.write("--test*%05d"%a+"\n")
file.close()


# --pythonpath .
# --name 主流程测试
# --test *添加成功
# --test *商品
# tc/login/username.robot