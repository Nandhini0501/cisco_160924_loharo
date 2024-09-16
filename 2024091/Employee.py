class Employee:
    def __init__(self,name,code,salary):
            self.name=name
            self.code=code
            self.salary=salary

    def __str__(self):
             return f'{self.name},{self.code},{self.salary}'


nandhini=Employee('nandhini','PYABC2001',200000)
print(nandhini)

