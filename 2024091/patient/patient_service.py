from patient_entity import Patient

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


