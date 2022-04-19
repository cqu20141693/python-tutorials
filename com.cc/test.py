f = open('name1.txt', 'w')
f.write('诸恶量|wux|wuxi|wod|pop|pip|www')
f.close()

with open('name1.txt') as f:
    for line in f:
        print(line.split('|'))
        for a in line.split('|'):
            print(a)


f = open('name1.txt')
date = f.read()  # data读取到的是整个文件
print(date.split('|'))  # 以'|'作为分割 返回一个由字符串组成的列表

f1 = open('name2.txt', 'w')
f1.write('123\n456\n789\n741\n852\n963\n520\n')
f1.close()

f1 = open('name2.txt')
i = 1
for line in f1.readlines():
    print(line.split('\n'))
    i += 1


with open('name1.txt') as f:
    for line in f:
        print(line.split('|'))
        for a in line.split('|'):
            print(a)