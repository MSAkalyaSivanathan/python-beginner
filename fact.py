def fact(n):
    fact=1
    for i in range(n):
        fact*=i+1
        return fact
print(fact(5))
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print("factorial of a number:",fact)
i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
    print(fact)
        
