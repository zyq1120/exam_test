n = list(map(int,input("").split(' ')))
a = sum(n)/10
print(a)

for i in range(0,10):
    if n[i] < a:
        print("%d %d"%(i+1,n[i]))


        """"
        不考
        
        """