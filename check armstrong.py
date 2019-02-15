num=int(input())
order=len(str(num))
summ=0
temp=num
while temp>0:
    digit=temp%10
    summ+=digit**order
    temp//=10
if num==summ:
    print("yes")
else:
    print("no")
