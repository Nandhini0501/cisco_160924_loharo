from patient_entity import Patient

patients= {} #dict()


def patient_add(id,name):
    global patients
    patient= Patient(id,name)
    patients[patient.id] = patient #patients.append(patient)
    print('patient created successfully')
def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient == None:
            print(f'no such id{id}')
            return
            
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
        del patients[id] #patients.remove(patient)
        print('Patient deleted successfully')
            
def patient_display():
    global patients
    for id in patients:#for patients in patients: for list
        print(patients[id]) #print(patient) for list

def patient_display_byid(id):
    global patients
    patient = patients.get(id)#in patients:
    if patient== None:
           print(f'no such id {id}')
           return
    print(patient)
    
def patient_update(id):
    global patients
    patient = patients.get(id)#in patients:
    if patient== None:
           print(f'no such id {id}')
           return
    print(patient)
    
    name=input(f'enter new name({patient.name}):')
    patient.name = name
    print('Patient uodated successfully')


