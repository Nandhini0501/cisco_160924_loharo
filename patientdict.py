import json

class PatientManagementDict:
    def __init__(self):
        self.patients = {}

    def add_patient(self, id, name):
        if id not in self.patients:
            self.patients[id] = name
            print(f"Patient {name} with ID {id} added successfully.")
        else:
            print(f"Patient ID {id} already exists with name {self.patients[id]}.")

    def remove_patient(self, id):
        if id in self.patients:
            removed_name = self.patients.pop(id)
            print(f"Patient {removed_name} with ID {id} removed successfully.")
        else:
            print(f"Patient ID {id} does not exist.")

    def display_patients(self):
        if self.patients:
            print("Current list of patients:")
            for id, name in self.patients.items():
                print(f"ID: {id}, Name: {name}")
        else:
            print("No patients in the list.")

    def write_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.patients, file)
        print(f"Patient dict written to {filename}.")

def main_dict():
    management = PatientManagementDict()

    while True:
        print("\nPatient Management System (Dict)")
        print("1. Add patient")
        print("2. Remove patient")
        print("3. Display patients")
        print("4. Write to JSON")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter patient ID to add: ")
            name = input("Enter patient name to add: ")
            management.add_patient(id, name)
        elif choice == '2':
            id = input("Enter patient ID to remove: ")
            management.remove_patient(id)
        elif choice == '3':
            management.display_patients()
        elif choice == '4':
            filename = input("Enter the filename to write to (e.g., patients_dict.json): ")
            management.write_to_json(filename)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_dict()