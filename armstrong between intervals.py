N,k=map(int,input().split())
for i in range(N,k+1):
    summ=0
    t=i
    while t>0:
        digit=t%10
        summ+=digit**3
        t=t//10
        if i==summ:
            print(i,end=" ")
