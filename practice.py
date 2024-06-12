# Recursion
def sum(A,B):
    if B==0:
        return A
    else:
        return sum(A+1,B-1)
A=10
B=20
result=sum(A,B)
print(result)
# Two Sum
x=10
y=20
print(x+y)
#nxt
x=int(input("Enter you number:"))
y=int(input("Enter you number:"))
print(x+y)
# nxt
x=int(input("Enter you number:"))
y=int(input("Enter you number:"))
sum=x+y
print("The sum is:",sum)
#nxt"
num1=input("Enter first number:")
num2=input("enter second number:")
sum=float(num1)+float(num2)
print("The sum is{0} and {1} is {2}",format(sum))
# add() method
import operator
A=10
B=20
sum=operator.add(A,B)
print(sum)
# nxt def
def fun(x,y):
    return x+y
A=10
B=20
sum=fun(A,B)
print(sum)
# in build sum()
a=[20,30]
result=sum(a)
print(result)
# class  two num
class num:
    def __init__(self,A,B):
        self.A=A
        self.B=B
        def sum(self):
            return self.A+self.B
value=num(10,20)
result=sum(num)
print(result)
        
