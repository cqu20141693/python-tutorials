# 请输入一百以内的素数
sum = 0
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        sum = sum + 1
print(sum)

# 题目：判断101-200之间有多少个素数，并输出所有素数
tep = 0
for i in range(101, 200):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        tep += 1
print(tep)
