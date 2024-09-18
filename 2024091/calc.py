def find_calc(first:int,second:int)->int:
    sum=first+second
    diff=first-second
    product=first*second
    quotient=first//second
    return sum,diff,product,quotient
s,d,p,q=find_calc(20,6)
print(s,d,p,q)

a=10
b=20
a,b=b,a