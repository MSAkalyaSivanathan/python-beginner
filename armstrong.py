n=int(input("enter a number:"))
sum=0
num=n
while(n>0):
    r=n%10
    sum=sum+r**3
    n=n//10
if(num==sum):
    print("It is armstrong")
else:
    print("not armstrong")
