def clear_screen():
    print('\n' * 100)  # Adjust the number based on your console size
# Parent Class
class Animal:
    def __init__(self) -> None:
        pass

    def polyAnimal(self):
        print("\nThis is considered as an animal.")

    def printAnimals(self):
        print("\n****************************************")
        print("Choices:")
        print("\tMammal")
        print("\tAmphibian")
        print("\tFish")
        print("\tBird")
        print("\tReptile")
        print("\tExit")
        print("\n****************************************")


# Child Class Mammal
class Mammal(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
              \tMammal:

                A warm-blooded vertebrate animal of a class 
                that is distinguished by the possession of hair
                or fur, the secretion of milk by females for the
                nourishment of the young, and (typically) the 
                birth of live young.
              """)

    def alive(self):
        print("\nThis animal is alive!")


class Dogs(Mammal):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe dog is eating!")
        print("\nWOOF! WOOF! WOOF!")


class Cats(Mammal):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe cat is eating!")
        print("\nMEOW! MEOW! MEOW!")


# Child Class Amphibian
class Amphibian(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
              \tAmphibian:

                A cold-blooded vertebrate animal of a class 
                that comprises the frogs, toads, newts, and 
                salamanders. They are distinguished by having 
                an aquatic gill-breathing larval stage followed 
                (typically) by a terrestrial lung-breathing adult stage.
              """)

    def alive(self):
        print("\nThis animal is alive!")


class Frogs(Amphibian):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe frog is hopping!")
        print("\nKOKAK! KOKAK! KOKAK!")


class Salamander(Amphibian):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Salamander is crawling!")
        print("\nFRIK! FRIK! FRIK!")


# Child Class Fish
class Fish(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
              \tFish:

                A limbless cold-blooded vertebrate animal with gills
                and fins and living wholly in water.
              """)

    def alive(self):
        print("\nThis animal is alive!")


class AtlanticBlueMarlin(Fish):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Atlantic Blue Marlin is eating small fishes!")
        print("\nGLUB! GLUB! GLUB!")


class Garfish(Fish):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Garfish is breathing in the water!")
        print("\nGULP! GULP! GULP!")


# Child Class Birds
class Birds(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
              \tBirds:

                A warm-blooded egg-laying vertebrate distinguished 
                by the possession of feathers, wings, and a beak and 
                (typically) by being able to fly.
              """)

    def alive(self):
        print("\nThis animal is alive!")


class Parrot(Birds):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Parrot is speaking!")
        print("\nWITWIW! WITWIW! WITWIW!")


class Dove(Birds):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Dove is flying!")
        print("\nKROO! KROO! KROO!")


# Child Class Reptiles
class Reptiles(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
              \tReptiles:

                A vertebrate animal of a class that includes snakes, 
                lizards, crocodiles, turtles, and tortoises. They are 
                distinguished by having a dry scaly skin and typically 
                laying soft-shelled eggs on land.
              """)

    def alive(self):
        print("\nThis animal is alive!")


class Snake(Reptiles):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Snake is eating an egg!")
        print("\nHISS! HISS! HISS!")


class Crocodile(Reptiles):
    def __init__(self) -> None:
        pass

    def act(self):
        print("\nthe Crocodile is jaw-eating the deer!")
        print("\nARGH! ARGH! ARGH!")

def Choices(animalChoice):
    print("\n****************************************")
    print("Choices:")
    if animalChoice == "mammal":
        print("\tDog")
        print("\tCat")
    elif animalChoice == "amphibian":
        print("\tFrog")
        print("\tSalamander")
    elif animalChoice == "fish":
        print("\tAtlantic Blue Marlin")
        print("\tGarfish")
    elif animalChoice == "bird":
        print("\tParrot")
        print("\tDove")
    elif animalChoice == "reptile":
        print("\tSnake")
        print("\tCrocodile")
    print("\n****************************************")

def Options(animal):
    while True:
        Choices(animal)
        user_input = input("\nWhat {} do you want to know? ".format(animal))
        if user_input == "":
            print("\nPlease enter something!")
        elif user_input == "dog":
            dog.alive()
            dog.act()
            break
        elif user_input == "cat":
            cat.alive()
            cat.act()
            break
        elif user_input == "frog":
            frog.alive()
            frog.act()
            break
        elif user_input == "salamander":
            salamander.alive()
            salamander.act()
            break
        elif user_input == "atlantic blue marlin":
            atlanticblueMarlin.alive()
            atlanticblueMarlin.act()
            break
        elif user_input == "garfish":
            garfish.alive()
            garfish.act()
            break
        elif user_input == "parrot":
            parrot.alive()
            parrot.act()
            break
        elif user_input == "dove":
            dove.alive()
            dove.act()
            break
        elif user_input == "snake":
            snake.alive()
            snake.act()
            break
        elif user_input == "crocodile":
            crocodile.alive()
            crocodile.act()
            break
        else:
            print("\nPlease enter a valid choice!")

showAnimals = Animal()

mammal = Mammal()
dog = Dogs()
cat = Cats()

amphibian = Amphibian()
frog = Frogs()
salamander = Salamander()

fish = Fish()
atlanticblueMarlin = AtlanticBlueMarlin()
garfish = Garfish()

bird = Birds()
parrot = Parrot()
dove = Dove()

reptile = Reptiles()
snake = Snake()
crocodile = Crocodile()

while True:
    showAnimals.printAnimals()
    user_input = input("\nWhat animal do you want to know? ")
    if user_input == "":
        clear_screen()
        print("\nPlease enter something!")
    elif user_input == "mammal":
        clear_screen()
        showAnimals.polyAnimal()
        mammal.show()
        Options(user_input)
    elif user_input == "amphibian":
        clear_screen()
        showAnimals.polyAnimal()
        amphibian.show()
        Options(user_input)
    elif user_input == "fish":
        clear_screen()
        showAnimals.polyAnimal()
        fish.show()
        Options(user_input)
    elif user_input == "bird":
        clear_screen()
        showAnimals.polyAnimal()
        bird.show()
        Options(user_input)
    elif user_input == "reptile":
        clear_screen()
        showAnimals.polyAnimal()
        reptile.show()
        Options(user_input)
    elif user_input == "exit":
        clear_screen()
        print("\n\nThanks Bye!")
        break
    else:
        print("\nPlease enter a valid choice!")

