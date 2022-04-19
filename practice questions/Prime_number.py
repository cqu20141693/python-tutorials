# 请输入一百以内的素数
sum = 0
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
     print(i)
     sum=sum+1
print(sum)