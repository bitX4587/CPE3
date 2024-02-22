def clearScreen():
    print('\n' * 50)

class PersonalData:
    def __init__(self, name, age, address, course):
        self.name = name
        self.age = age
        self.address = address
        self.course = course

    def printStudent(self):
        print("\nMy name is " + self.name)
        print("I am " + str(self.age) + " YEARS OLD")
        print("I lived in " + self.address + ", CALBAYOG CITY, SAMAR")
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

        if age_input == "":
            print("\nPlease enter something!")
        elif age_input.isdigit():
            age = int(age_input)
            if 18 <= age <= 90:
                print("\nRegistered!")
                break
            else:
                print("\nPlease enter a valid age between 18 and 90!")
        else:
            print("\nPlease enter a valid age between 18 and 90!")

    calbayogBarangays = [
        "barangay agaasan",
        "barangay aguinaldo",
        "barangay alvares",
        "barangay amampacang",
        "barangay amancosiling norte",
        "barangay amancosiling sur",
        "barangay anislag",
        "barangay ba-os",
        "barangay bacay",
        "barangay balud",
        "barangay banga",
        "barangay bangon",
        "barangay batuan",
        "barangay bayo",
        "barangay binanggaran",
        "barangay biter",
        "barangay cabacungan",
        "barangay cabcaban",
        "barangay cabicahan",
        "barangay cabigan",
        "barangay cabugawan",
        "barangay cag-anahaw",
        "barangay cag-anibong",
        "barangay cagbalogo",
        "barangay cagsalaosao",
        "barangay cagumayang",
        "barangay cagutian",
        "barangay cal-igang",
        "barangay canbalogo",
        "barangay canlanggas",
        "barangay capoocan",
        "barangay carayman",
        "barangay casulgan",
        "barangay cawang",
        "barangay cawayan",
        "barangay cogon",
        "barangay cojopan",
        "barangay crystal",
        "barangay dagum",
        "barangay dalid",
        "barangay darahuway dangulaan",
        "barangay divinubo",
        "barangay doongan",
        "barangay dujali",
        "barangay dulacac",
        "barangay dumarag",
        "barangay esperanza",
        "barangay hamorawon",
        "barangay hanopol",
        "barangay hipgasan",
        "barangay homestead",
        "barangay kag-irong",
        "barangay kalaklan i",
        "barangay kalaklan ii",
        "barangay kawit",
        "barangay kilijao",
        "barangay libas",
        "barangay longsob",
        "barangay lungsob",
        "barangay macatingog",
        "barangay macatingog proper",
        "barangay maclang",
        "barangay mag-ubay",
        "barangay magsaysay",
        "barangay mahanud",
        "barangay malaga",
        "barangay malajog",
        "barangay mali-id",
        "barangay mamawan",
        "barangay manlangit",
        "barangay mansanas",
        "barangay mantaong",
        "barangay mapuyo",
        "barangay margen",
        "barangay maybog",
        "barangay mckinley",
        "barangay militar",
        "barangay mirador",
        "barangay mondragon",
        "barangay morada",
        "barangay motoom",
        "barangay nasangculan",
        "barangay nebab",
        "barangay new mahayag",
        "barangay nijaga",
        "barangay nijaga-an",
        "barangay pahug",
        "barangay palanog",
        "barangay panalarmahan",
        "barangay pangdan",
        "barangay parasan",
        "barangay patria",
        "barangay penro",
        "barangay polambato",
        "barangay polangi",
        "barangay poonbato",
        "barangay pozorrubio",
        "barangay progreso",
        "barangay quibarato",
        "barangay quibarato island",
        "barangay quilit-isan",
        "barangay ragay",
        "barangay ramos",
        "barangay rebe",
        "barangay rinawasan",
        "barangay rizal",
        "barangay roces",
        "barangay rock",
        "barangay rosario",
        "barangay roy",
        "barangay sabang dalakit",
        "barangay sabang daguitan",
        "barangay sabang san roque",
        "barangay sagkahan",
        "barangay sagsagat",
        "barangay saguma-a",
        "barangay saljag",
        "barangay sambog",
        "barangay santo nino",
        "barangay santome",
        "barangay sawang",
        "barangay sinantan",
        "barangay sixto ampopoy",
        "barangay so-ong",
        "barangay songco",
        "barangay somoroy",
        "barangay songculan",
        "barangay suba",
        "barangay sugod",
        "barangay tabawan",
        "barangay tagbayaon",
        "barangay tagoytoy",
        "barangay talahib",
        "barangay talubang",
        "barangay talustusan",
        "barangay tandang batu",
        "barangay tarug",
        "barangay tayud",
        "barangay tebaldo",
        "barangay tinaplacan",
        "barangay tingob",
        "barangay tipolo",
        "barangay torbang",
        "barangay torbay",
        "barangay tominamos",
        "barangay tomoc",
        "barangay tomoktok",
        "barangay trinidad",
        "barangay tulay",
        "barangay tumalum",
        "barangay tupana",
        "barangay tupolahan",
        "barangay ubo",
        "barangay villahermosa",
        "barangay vimapor",
        "barangay watangan",
        "barangay wagas",
        "barangay yabon",
        "barangay yanan",
        "barangay yangco",
        "barangay yatal",
        "barangay yuagan",
        "barangay yukon",
        "barangay zapanta",
        "barangay zonrox"
    ]

    while True:
        address = input("\nWhere do you live (e.g. Barangay Hamorawon)? ").lower()
        if address == "":
            print("\nPlease enter something!")
        elif address in calbayogBarangays:
            print("\nRegistered!")
            break
        else:
            print("\nPlease enter a valid address!")

    courses = [
        "bs accountancy",
        "bs advertising",
        "bs agriculture",
        "bs agronomy",
        "bs agribusiness",
        "bs agricultural and biosystems engineering",
        "bs agricultural chemistry",
        "bs agricultural economics",
        "bs agricultural engineering",
        "bs agricultural technology",
        "bs agriculture",
        "bs agro-industrial technology",
        "bs agronomy",
        "bs animal husbandry",
        "bs animal science",
        "bs applied physics",
        "bs applied mathematics",
        "bs applied physics",
        "bs applied statistics",
        "bs architecture",
        "bs biochemistry",
        "bs biological science",
        "bs biology",
        "bs biotechnology",
        "bs broadcasting",
        "bs building construction",
        "bs business administration",
        "bs ceramics engineering",
        "bs chemical engineering",
        "bs chemistry",
        "bs civil engineering",
        "bs clothing technology",
        "bs coe-computer engineering",
        "bs coe-electronics engineering",
        "bs commerce",
        "bs communication",
        "bs community development",
        "bs computer engineering",
        "bs computer science",
        "bs cooperative",
        "bs criminology",
        "bs crop science",
        "bs customs administration",
        "bs development communication",
        "bs economics",
        "bs education",
        "bs educational administration",
        "bs electrical engineering",
        "bs electronics and communications engineering",
        "bs electronics engineering",
        "bs elementary education",
        "bs engineering",
        "bs environmental science",
        "bs entrepreneurship",
        "bs environmental management",
        "bs environmental science",
        "bs extension education",
        "bs family and consumer science",
        "bs family life and child development",
        "bs fashion design and merchandising",
        "bs fisheries",
        "bs food technology",
        "bs forestry",
        "bs geography",
        "bs geodetic engineering",
        "bs geology",
        "bs guidance counseling",
        "bs horticulture",
        "bs hotel and restaurant management",
        "bs human ecology",
        "bs human kinetics",
        "bs human resource development management",
        "bs industrial education",
        "bs industrial engineering",
        "bs information technology",
        "bs information management",
        "bs interior design",
        "bs international relations",
        "bs journalism",
        "bs landscape architecture",
        "bs legal management",
        "bs library and information science",
        "bs literature",
        "bs management",
        "bs manufacturing engineering",
        "bs marine biology",
        "bs marine engineering",
        "bs marketing",
        "bs mass communication",
        "bs mathematics",
        "bs mechanical engineering",
        "bs medical technology",
        "bs metallurgical engineering",
        "bs meteorology",
        "bs microbiology",
        "bs mining engineering",
        "bs molecular biology",
        "bs music",
        "bs nursing",
        "bs nutrition",
        "bs occupational therapy",
        "bs office administration",
        "bs pharmacy",
        "bs philosophy",
        "bs physical education",
        "bs physical therapy",
        "bs physics",
        "bs political science",
        "bs polymer engineering",
        "bs psychology",
        "bs public administration",
        "bs public health",
        "bs public relations",
        "bs radiologic technology",
        "bs real estate management",
        "bs recreation and sports management",
        "bs refrigeration and air-conditioning technology",
        "bs religious education",
        "bs remote sensing",
        "bs research and development management",
        "bs respiratory therapy",
        "bs rural development",
        "bs science communication",
        "bs secondary education",
        "bs social work",
        "bs sociology",
        "bs software engineering",
        "bs special education",
        "bs sports science",
        "bs statistics",
        "bs tourism",
        "bs veterinary medicine",
        "bs veterinary technology",
        "bs vocational education",
        "bs wildlife",
        "bs zoology"
    ]

    while True:
        course = input("\nWhat is your course (e.g. BS Computer Engineering)? ").lower()
        if course == "":
            print("\nPlease enter something!")
        elif course in courses:
            print("\nRegistered!")
            break
        else:
            print("\nPlease enter a valid course!")

    return PersonalData(name.upper(), age, address.upper(), course.upper())

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

for student in studentRecords:
    student.printStudent()

while True:
    question = input("\nFrom @pogingprogrammer: Can I get a LIKE and a FOLLOW (Yes, No)? ").lower()
    if question == "":
        print("\nPlease enter something!")
    elif question == "yes":
        print("\nThank you pogi and Godbless......")
        break
    elif question == "no":
        print("\nSorry for bothering......")
        break
    else:
        print("\nPlease enter a valid answer!")
