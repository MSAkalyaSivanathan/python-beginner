s=int(input("Enter the starting range:"))
e=int(input("enter the end range:"))
print("Prime number in the range",s,"to",e)
for i in range(s,e+1):
    flag=0
    for j in range(2,i):
        if(i % j == 0):
            flag=1
            break
        if(flag==0):
           print(i,end=' ')


