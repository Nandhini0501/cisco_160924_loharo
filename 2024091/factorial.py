def find_fact(N):
    fact=1
    for i in range(N,1,-1):
        fact = fact*i
    return fact
f1= find_fact(5)
f2=find_fact(4)
print(f1)
print(f2)

