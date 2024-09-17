""""
patients_name=[]

def add_patients(name):
    
    patients_name.append(name)
    
def delete_patients(name):
    
    try:
        patients_name.remove(name)
    except ValueError as err:
        print('no such name')

def main():
    choice =int(input('''
                     1-add
                     2-delete
                     3-end
                     4-enter your choice'''))
    
    if choice ==1:
        name=input("enter name:")
        add_patients(name)
        print(patients_name)
    elif choice==2:
        name=input('enter name:')
        delete_patients(name)
        print(patients_name)
    return choice


def menus():
    choice=main()
    while choice !=4:
        choice=main()
    print('app ended')

menus()
    
"""

class Patient :
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f'[id= {self.id} , name = {self.name}]'
    def __repr__(self):
        return self.__str__()


patients= []
def patient_add(id,name):
    global patients
    patient= Patient(id,name)
    patients.append(patient)
    print('patient created successfully')
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully')
            patients.remove(patient)
            return
    print(f'no such id{id}')
def patient_display():
    global patients
    for patient in patients:
        print(patient)

def patient_display_byid(id):
    global patients
    for patient in patients:
        if patient.id == id:
           print(patient)
           return
    print('invalid id')
def patient_update(id):
    global patients
    for patient in patients:
        if patient.id == id:
           print(patient)
           name=input(f'enter new name({patient.name})')



def menu():
    choice =int(input('''
                     1-add
                     2-delete by id
                     3-display all patient
                     4-display by id
                     5.update record by id
                     7-end
                     your choice : '''))
    
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('Enter patient name:')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to delete:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice == 4:
        id= int(input('enter patient id :'))
        patient_display_byid(id)

    elif choice == 5:
        id= int(input('enter patient id :'))
        patient_update(id)

        
    elif choice == 7:
        pass 
    else:
        print('Invalid menu')
    return choice

def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')

menus()

    
    




       

 
    
    
