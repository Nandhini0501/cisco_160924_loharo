my_list=(input("enter atleast 5 integer (separated by space) ")).split()
int_list=(int(n) for n in my_list)
my_tuple=tuple(my_list)
my_set=set(my_list)
my_fset=frozenset(my_set)
my_dict={key:key*2 for key in int_list}
print(my_dict)