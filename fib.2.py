def fibonacci(n):
    num= [0, 1]       
    for i in range(2, n):
        num.append(num[-1] + num[-2])

    return num


n = 10  
print(fibonacci(n))
