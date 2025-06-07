
n = 0
str = ""
m,n = eval(input())
for i in range(m,n+1):
    flag = 1
    for j in range(2,i//2+1):
        if i%j == 0:
            flag = 0
            break
    if flag == 1:
        n+=1
        str = str +"%-2d "%(i)
        if n % 10 == 0:
            print(str)
            str=""
print(str)