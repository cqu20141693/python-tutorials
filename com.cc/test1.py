import random
names = [input('请输入11个人的姓名：')]
names = str(names)
names = names.rstrip("'")
names = names.lstrip("'")
print(names)
print(len(names))