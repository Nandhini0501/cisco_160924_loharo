names_list=input("enter student name (separated by spaces):").split()
names_set =set(names_list)
names_fset= frozenset(names_set)
names_dict ={ name:len(name) for name in names_fset}
print(f'original list:(names_list)')
print(f'set(no duplicates : {names_set})')
print(f'frozen set:{names_fset}')
print(f'dictionary of name lengths : {names_dict}')

import json
with open('qstn02_data_json','w') as names_db:
    json.dump(names_dict,names_db)
print('dictionary written to json file.')

with open('qstn02_data_json','r') as names_db:
    names_dict2 = json.load(names_db)
    print(f'reading from json file...\n{names_dict2}')

