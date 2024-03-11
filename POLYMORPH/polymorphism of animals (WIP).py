#Parent Class
class Animal:
    def __init__(self) -> None:
        pass

    def polyAnimal(self):
        print("\nThis is considered as an animal.")

    def printAnimals(self):
        print("\n****************************************")
        print("Choices:")
        print("\t1) Mammal")
        print("\t2) Amphibian")
        print("\t3) Fish")
        print("\t4) Birds")
        print("\t5) Reptiles")
        print("\t6) Exit")
        print("\n****************************************")

#Child Class Mammal
class Mammal(Animal):
    def __init__(self) -> None:
        pass
    def show(self):
        print("""
              \tMammal:

                A warm-blooded vertebrate animal of a class 
                that is distinguished by the possession of hair
                or fur,the secretion of milk by females for the
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
        
#Child Class Amphibian
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

class Snakes(Amphibian):
    def __init__(self) -> None:
        pass
    def act(self):
        print("\nthe snake is crawling!")
        print("\nHISS! HISS! HISS!")

#Child Class Fish
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

#Child Class Birds
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
"""     
class AtlanticBlueMarlin(Birds):
    def __init__(self) -> None:
        pass
    def act(self):
        print("\nthe Atlantic Blue Marlin is eating small fishes!")
        print("\GLUB! GLUB! GLUB!")

class Garfish(Birds):
    def __init__(self) -> None:
        pass
    def act(self):
        print("\nthe Garfish is breathing in the water!")
        print("\GULP! GULP! GULP!")
"""
#Child Class Reptiles
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

"""
class AtlanticBlueMarlin(Birds):
    def __init__(self) -> None:
        pass
    def act(self):
        print("\nthe Atlantic Blue Marlin is eating small fishes!")
        print("\GLUB! GLUB! GLUB!")

class Garfish(Birds):
    def __init__(self) -> None:
        pass
    def act(self):
        print("\nthe Garfish is breathing in the water!")
        print("\GULP! GULP! GULP!")
"""
showAnimals = Animal()

mammal = Mammal()
dog = Dogs()
cat = Cats()

amphibian = Amphibian()
frog = Frogs()
snake = Snakes()

fish = Fish()
atlanticblueMarlin = AtlanticBlueMarlin()
garfish = Garfish()

birds = Birds()

reptiles = Reptiles()


while True:
    showAnimals.printAnimals()
    user_input = input("\nWhat animal do you want to know? ")
    if user_input == "":
        print("\nPlease enter something!")
    elif user_input == "1":
        showAnimals.polyAnimal()
        mammal.show()
        dog.alive()
        dog.act()
        cat.alive()
        cat.act()
        print("\nYes it works!")
    elif user_input == "2":
        showAnimals.polyAnimal()
        amphibian.show()
        frog.alive()
        frog.act()
        snake.alive()
        snake.act()
        print("\nYes it works!")
    elif user_input == "3":
        showAnimals.polyAnimal()
        fish.show()
        atlanticblueMarlin.alive()
        atlanticblueMarlin.act()
        garfish.alive()
        garfish.act()
        print("\nYes it works!")
    elif user_input == "4":
        showAnimals.polyAnimal()
        birds.show()
        print("\nYes it works!")
    elif user_input == "5":
        showAnimals.polyAnimal()
        reptiles.show()
        print("\nYes it works!")
    elif user_input == "6":
        print("\n\nThanks Bye!")
        break
    else:
        print("\nPlease enter a valid choice!")