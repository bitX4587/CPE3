import os

def clearScreen():
    print('\n' * 50)

class PersonalData:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def printStudent(self):
        print("\nMy name is " + self.name)
        print("I am " + str(self.age) + " years old")
        print("My course is " + self.course)

def GetPersonalData():
    while True:
        name = input("\nWhat is your name? ")
        if name == "":
            print("\nPlease enter something!")
        else:
            print("\nRegistered!")
            break

    while True:
        age_input = input("\nHow old are you? ")

        if age_input.isdigit():
            age = int(age_input)
            if 1 <= age <= 90:
                print("\nRegistered!")
                break
            else:
                print("\nPlease enter a valid age between 1 and 90!")
        else:
            print("\nPlease enter a valid age between 1 and 90!")

    while True:
        course = input("\nWhat is your course? ")
        if course == "":
            print("\nPlease enter something!")
        else:
            print("\nRegistered!")
            break

    return PersonalData(name, age, course)

studentRecords = []

print("*******************")
print("  Student Record")
print("*******************")

while True:
    AllPersonalData = GetPersonalData()
    studentRecords.append(AllPersonalData)

    user_input = input("\nDo you want to create another set of data? (enter 'new data' to add more or enter 'exit' to stop): ")

    while user_input != "new data":
        if user_input.lower() == 'exit':
            break
        elif user_input == "new data":
            AllPersonalData = GetPersonalData()
            studentRecords.append(AllPersonalData)
            user_input = input("\nDo you want to create another set of data? (enter 'new data' to add more or enter 'exit' to stop): ")
        else:
            user_input = input("\nDo you want to create another set of data? (enter 'new data' to add more or enter 'exit' to stop): ")

    if user_input.lower() == 'exit':
        break

clearScreen()

for students in studentRecords:
    students.printStudent()
