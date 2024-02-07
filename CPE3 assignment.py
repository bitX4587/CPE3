display = []
space = " "

while True:
    firstName = input("What is your first name? ")
    if firstName == "":
        print("Please enter something!\n")
    else:
        display.append("First Name:"+space+firstName)
        print("Registered!\n")
        break

while True:
    lastName = input("What is your last name? ")
    if lastName == "":
        print("Please enter something!\n")
    else:
        display.append("Last Name:"+space+lastName)
        print("Registered!\n")
        break

while True:
    location = input("What is your location? ")
    if location == "":
        print("Please enter something!\n")
    else:
        display.append("Location:"+space+location)
        print("Registered!\n")
        break

while True:
    age = input("How old are you? ")

    if age.isdigit():
        age = int(age)
        if 0 < age <= 1:
            display.append("Age:"+space+str(age)+space+"year old")
            print("Registered!\n")
            break
        elif 0 < age <= 90:
            display.append("Age:"+space+str(age)+space+"years old")
            print("Registered!\n")
            break
        else:
            print("Please enter a valid age between 1 and 90!\n")
    else:
        print("Please enter a valid age between 1 and 90!\n")

for context in display:
    print(context)