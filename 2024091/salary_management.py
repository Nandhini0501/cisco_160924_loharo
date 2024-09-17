salaries=[10,20,30,50,70]
def salary_add(salary):
    global salaries
    salaries.append(salary)
    
def salary_delete(salary):
    global salaries
    try:
        salaries.remove(salary)
    except ValueError as err:
        print('no such salary')
    
def salary_sum():
    global salaries
    s=0
    for salary in salaries:
        s+=salary
    return s

    
def salary_avg():
    global salaries
    s=sum(salaries)
    count=len(salaries)
    avg=s/count
    return avg
def salary_max():
    global salaries
    return max(salaries)
def salary_min():
    global salaries
    return min(salaries)


def menu():
    choice =int(input('''
                     1-add
                     2-delete
                     3-sum
                     4-avg
                     5-min
                     6-max
                     7-end
                     8-enter your choice:
                    '''))
                    
        
    

    if choice ==1:
        salary=float(input("enter salary:"))
        salary_add(salary)
        print(salaries)
    elif choice==2:
        salary=float(input('enter salary:'))
        salary_delete(salary)
        print(salaries)
    elif choice==3:
        s=salary_sum()
        print(s)
    elif choice==4:
        avg=salary_avg()
        print(avg)
    elif choice==5:
        min=salary_min()
        print(min)
    elif choice==6:
        max=salary_max()
        print(max)
    return choice

def menus():
    choice=menu()
    while choice !=7:
        choice=menu()
    print('app ended')

menus()
