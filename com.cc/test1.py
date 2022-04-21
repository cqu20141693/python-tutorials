for i in range(1, 10):
    for j in range(1, i + 1):
         mul = i * j
         if mul < 10:
             print(str(j) + "x" + str(i) + "=" + str(mul), end="   ")
         else:
             print(str(j) + "x" + str(i) + "=" + str(mul), end="  ")
    print()