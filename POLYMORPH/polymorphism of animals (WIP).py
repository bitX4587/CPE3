#imports
import time
import os

#clearscreen effect
def clear_screen():
    """
    print('\n' * 100)
    """
    if os.name == 'nt':
        _ = os.system('cls')
        # For Mac and Linux
    else:
        _ = os.system('clear')


# Parent Class Animal
class Animal:
    def __init__(self) -> None:
        pass

    #polymorphism
    def polyAnimal(self):
        print("\nThis is considered as an animal.")

    #MAIN CHOICES
    def printAnimals(self):
        print("\n****************************************")
        print("Choices:")
        print("\tMammal")
        print("\tAmphibian")
        print("\tFish")
        print("\tBird")
        print("\tReptile")
        print()
        print("\tExit")
        print("****************************************")


# Child Class Mammal
class Mammal(Animal):
    def __init__(self) -> None:
        pass

    #Mammal Show
    def show(self):
        print("""
Mammal:

    A mammal is a vertebrate animal of the class Mammalia. 
    Mammals are characterized by the presence of milk-producing
    mammary glands for feeding their young, a neocortex region
    of the brain, fur or hair, and three middle ear bones.
                """)

    def alive(self):
        print("\nThis animal is alive!")

#Child Class Dogs in Mammal
class Dogs(Mammal):
    def __init__(self) -> None:
        pass

    #Dog Show
    def act(self):
        print("""
Dog:
               
    The dog is a domesticated descendant of the wolf.
    Also called the domestic dog, it is derived from
    extinct gray wolves, and the gray wolf is the dog's
    closest living relative. The dog was the first species
    to be domesticated by humans.
                """)

#Child Class German Shepherd in Dogs from Mammal
class German_Shepherd(Dogs):
    def __init__(self) -> None:
        pass

    #German Shepherd Show
    def act(self):
        print("""
German Shepherd:

    The German Shepherd, also known in Britain as an Alsatian,
    is a German breed of working dog of medium to large size.
    The breed was developed by Max von Stephanitz using various
    traditional German herding dogs from 1899. It was originally
    bred as a herding dog, for herding sheep.
                """)

#Child Class Bulldog in Dogs from Mammal
class Bulldog(Dogs):
    def __init__(self) -> None:
        pass

    #Bulldog Show
    def act(self):
        print("""
Bulldog:

    The Bulldog is a British breed of dog of mastiff type.
    It may also be known as the English Bulldog or British Bulldog.
    It is a medium-sized, muscular dog of around 40–55 lb.
    They have large heads with thick folds of skin around the face
    and shoulders and a relatively flat face with a protruding
    lower jaw.
                """)

#Child Class Labrador Retriever in Dogs from Mammal
class Labrador_Retriever(Dogs):
    def __init__(self) -> None:
        pass

    #Labrador Retriever Show
    def act(self):
        print("""
Labrador Retriever:

    The Labrador Retriever or simply Labrador is a British breed
    of retriever gun dog. It was developed in the United Kingdom
    from St. John's water dogs imported from the colony of Newfoundland,
    and was named after the Labrador region of that colony.
                """)

#Child Class Golden Retriever in Dogs from Mammal
class Golden_Retriever(Dogs):
    def __init__(self) -> None:
        pass

    #Golden Retriever Show
    def act(self):
        print("""
Golden Retriever:

    The Golden Retriever is a Scottish breed of retriever dog
    of medium size. It is characterised by a gentle and affectionate
    nature and a striking golden coat. It is commonly kept as a pet
    and is among the most frequently registered breeds in several
    Western countries.
                """)

#Child Class French Bulldog in Dogs from Mammal
class French_Bulldog(Dogs):
    def __init__(self) -> None:
        pass

    #French Bulldog Show
    def act(self):
        print("""
French Bulldog:

    The French Bulldog, French: Bouledogue Français,
    is a French breed of companion dog or toy dog.
    It appeared in Paris in the mid-nineteenth century,
    apparently the result of cross-breeding of Toy Bulldogs
    imported from England and local Parisian ratters.
                """)

#Child Class Siberian Husky in Dogs from Mammal
class Siberian_Husky(Dogs):
    def __init__(self) -> None:
        pass

    #Siberian Husky Show
    def act(self):
        print("""
Siberian Husky:

    The Siberian Husky is a medium-sized working sled dog breed.
    The breed belongs to the Spitz genetic family.
    It is recognizable by its thickly furred double coat,
    erect triangular ears, and distinctive markings,
    and is smaller than the similar-looking Alaskan Malamute.
                """)

#Child Class Cats in Mammal
class Cats(Mammal):
    def __init__(self) -> None:
        pass

    def act(self):
        print("""
Cat:
            
    The cat, commonly referred to as the domestic cat or house cat,
    is the only domesticated species in the family Felidae.
    Recent advances in archaeology and genetics have shown that
    the domestication of the cat occurred in the Near East around 7500 BC.
                """)

#Child Class Siamese cat in Cats from Mammal
class Siamese_cat(Cats):
    def __init__(self) -> None:
        pass

    #Siamese cat Show
    def act(self):
        print("""
Siamese Cat:

    The Siamese cat is one of the first distinctly recognised
    breeds of Asian cat. Derived from the Wichianmat landrace,
    one of several varieties of cats native to Thailand,
    the original Siamese became one of the most popular breeds 
    in Europe and North America in the 19th century.
                """)

#Child Class British Shorthair in Cats from Mammal
class British_Shorthair(Cats):
    def __init__(self) -> None:
        pass

    #British Shorthair Show
    def act(self):
        print("""
British Shorthair:
        
    The British Shorthair is the pedigreed version of the traditional
    British domestic cat, with a distinctively stocky body,
    thick coat, and broad face. The most familiar colour variant
    is the "British Blue", with a solid grey-blue coat, pineapple eyes,
    and a medium-sized tail.
                """)

#Child Class Maine Coon in Cats from Mammal
class Maine_Coon(Cats):
    def __init__(self) -> None:
        pass

    #Maine Coon Show
    def act(self):
        print("""
Maine Coon:

    The Maine Coon is a large domesticated cat breed.
    It is one of the oldest natural breeds in North America.
    The breed originated in the U.S. state of Maine,
    where it is the official state cat.
                """)

#Child Class Persian cat in Cats from Mammal
class Persian_cat(Cats):
    def __init__(self) -> None:
        pass

    #Persian cat Show
    def act(self):
        print("""
Persian Cat:

    The Persian cat, also known as the Persian Longhair,
    is a long-haired breed of cat characterised by a
    round face and short muzzle. The first documented ancestors
    of Persian cats might have been imported into Italy from 
    Khorasan as early as around 1620, however, this has not
    been proven.
                """)

#Child Class Ragdoll in Cats from Mammal
class Ragdoll(Cats):
    def __init__(self) -> None:
        pass

    #Ragdoll Show
    def act(self):
        print("""
Ragdoll:

    The Ragdoll is a breed of cat with a distinct colorpoint coat
    and blue eyes. Its morphology is large and weighty,
    and it has a semi-long and silky soft coat.
    American breeder Ann Baker developed Ragdolls in the 1960s.
    They are best known for their docile, placid temperament and
    affectionate nature.
                """)

# Child Class Amphibian
class Amphibian(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
Amphibian:

    Amphibians are ectothermic, anamniotic, four-limbed vertebrate animals
    that constitute the class Amphibia. In its broadest sense it is
    a paraphyletic group encompassing all tetrapods, excluding the amniotes.
                """)

    def alive(self):
        print("\nThis animal is alive!")


class Frogs(Amphibian):
    def __init__(self) -> None:
        pass

    def act(self):
        print("""
Frog:
            
    A frog is any member of a diverse and largely carnivorous
    group of short-bodied, tailless amphibians composing the order Anura.
                """)

#Child Class True toad in Frogs from Amphibian
class True_toad(Frogs):
    def __init__(self) -> None:
        pass

    #True toad Show
    def act(self):
        print("""
True Toad:

    A true toad is any member of the family Bufonidae,
    in the order Anura. This is the only family of anurans
    in which all members are known as toads,
    although some may be called frogs. The bufonids now
    comprise more than 35 genera, Bufo being the best known.
                """)

#Child Class Glass frogs in Frogs from Amphibian
class Glass_frogs(Frogs):
    def __init__(self) -> None:
        pass

    #Glass frogs Show
    def act(self):
        print("""
Glass Frog:

    The glass frogs belong to the amphibian family Centrolenidae,
    native to the Central American Rainforests.
    The general background coloration of most glass frogs is
    primarily lime green, the abdominal skin of some members
    of this family is transparent and translucent,
    giving the glass frog its common name.
                """)

#Child Class American bullfrog in Frogs from Amphibian
class American_bullfrog(Frogs):
    def __init__(self) -> None:
        pass

    #American bullfrog Show
    def act(self):
        print("""
American Bullfrog:

    The American bullfrog, often simply known as the bullfrog
    in Canada and the United States, is a large true frog native
    to eastern North America. It typically inhabits large
    permanent water bodies such as swamps, ponds, and lakes.
                """)

#Child Class Desert rain frog in Frogs from Amphibian
class Desert_rain_frog(Frogs):
    def __init__(self) -> None:
        pass

    #Desert rain frog Show
    def act(self):
        print("""
Desert Rain Frog:

    The desert rain frog, web-footed rain frog, or Boulenger's
    short-headed frog is a species of frog in the family Brevicipitidae.
    It is found in Namibia and South Africa. Its natural habitat is the
    narrow strip of sandy shores between the sea and the sand dunes.
                """)

#Child Class South American horned frogs in Frogs from Amphibian
class South_American_horned_frogs(Frogs):
    def __init__(self) -> None:
        pass

    #South American horned frogs Show
    def act(self):
        print("""
South American Horned Frog:

    Ceratophrys is a genus of frogs in the family Ceratophryidae.
    They are also known as South American horned frogs as well
    as Pacman frogs due to their characteristic round shape and
    large mouth, reminiscent of the video game character Pac-Man.
                """)

class Salamander(Amphibian):
    def __init__(self) -> None:
        pass

    def act(self):
        print("""
Salamander:
            
    Salamanders are a group of amphibians typically characterized
    by their lizard-like appearance, with slender bodies,
    blunt snouts, short limbs projecting at right angles to the body,
    and the presence of a tail in both larvae and adults.
                """)

#Child Class South American horned frogs in Salamander from Amphibian
class Axolotl(Salamander):
    def __init__(self) -> None:
        pass

    #Axolotl Show
    def act(self):
        print("""
Axolotl:

    The axolotl is a paedomorphic salamander closely related to
    the tiger salamander. It is unusual among amphibians in that
    it reaches adulthood without undergoing metamorphosis.
    Instead of taking to the land, adults remain aquatic and gilled.
                """)

#Child Class South Newts in Salamander from Amphibian
class Newts(Salamander):
    def __init__(self) -> None:
        pass

    #Newts Show
    def act(self):
        print("""
Newt:

    A newt is a salamander in the subfamily Pleurodelinae.
    The terrestrial juvenile phase is called an eft.
    Unlike other members of the family Salamandridae,
    newts are semiaquatic, alternating between aquatic
    and terrestrial habitats. Not all aquatic salamanders
    are considered newts, however.
                """)

#Child Class Fire salamander in Salamander from Amphibian
class Fire_salamander(Salamander):
    def __init__(self) -> None:
        pass

    #Fire salamander Show
    def act(self):
        print("""
Fire salamander:

    The fire salamander is a common species of salamander
    found in Europe. It is black with yellow spots or stripes
    to a varying degree; some specimens can be nearly completely
    black while on others the yellow is dominant.
                """)

#Child Class Chinese giant salamander in Salamander from Amphibian
class Chinese_giant_salamander(Salamander):
    def __init__(self) -> None:
        pass

    #Chinese giant salamander Show
    def act(self):
        print("""
Chinese giant salamander:

    The Chinese giant salamander is one of the largest salamanders
    and one of the largest amphibians in the world. It is fully aquatic,
    and is endemic to rocky mountain streams and lakes in the Yangtze
    river basin of central China.
                """)

#Child Class Red salamander in Salamander from Amphibian
class Red_salamander(Salamander):
    def __init__(self) -> None:
        pass

    #Red salamander Show
    def act(self):
        print("""
Red salamander:

    The red salamander is a species of salamander in the family
    Plethodontidae endemic to the eastern United States.
    Its skin is orange/red with random black spots. Its habitats
    are temperate forests, small creeks, ponds, forests, temperate
    shrubland, rivers, intermittent rivers, freshwater, trees springs.
                """)

# Child Class Fish
class Fish(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
Fish:

    A fish is an aquatic, gill-bearing vertebrate animal with
    swimming fins and a hard skull, but lacking limbs with digits.
    Fish can be grouped into the more basal jawless fish and
    the more common jawed fish, the latter including all living
    cartilaginous and bony fish, as well as the extinct placoderms
    and acanthodians 
    
    3 types of fish:
    superclass Agnatha (jawless fishes),
    class Chondrichthyes (cartilaginous fishes),
    and superclass Osteichthyes (bony fishes).
                """)

    def alive(self):
        print("\nThis animal is alive!")

#Child Class Jawless fish in Fish
class Jawless_fish(Fish):
    def __init__(self) -> None:
        pass

    #Jawless fish Show
    def act(self):
        print("""
Jawless fish:

    Agnatha is an infraphylum of jawless fish in the phylum Chordata,
    subphylum Vertebrata, consisting of both living and extinct species.
    Among recent animals, cyclostomes are sister to all vertebrates with jaws,
    known as gnathostomes.
                """)

#Child Class Pteraspidomorphi in Jawless fish from Fish
class Pteraspidomorphi(Jawless_fish):
    def __init__(self) -> None:
        pass

    #Pteraspidomorphi Show
    def act(self):
        print("""
Pteraspidomorphi:

    Pteraspidomorphi is an extinct class of early jawless fish. 
    They have long been regarded as closely related or even ancestral
    to jawed vertebrates, but the few characteristics they share with
    the latter are now considered as basal traits for all vertebrates.
                """)

#Child Class Haikouichthys in Jawless fish from Fish
class Haikouichthys(Jawless_fish):
    def __init__(self) -> None:
        pass

    #Haikouichthys Show
    def act(self):
        print("""
Haikouichthys:

    Haikouichthys is an extinct genus of craniate that lived 518 million
    years ago, during the Cambrian explosion of multicellular life.
                """)

#Child Class Arandaspis prionotolepis in Jawless fish from Fish
class Arandaspis_prionotolepis(Jawless_fish):
    def __init__(self) -> None:
        pass

    #Arandaspis prionotolepis Show
    def act(self):
        print("""
Arandaspis prionotolepis:

    Arandaspis prionotolepis is an extinct species of jawless fish that
    lived in the Ordovician period, about 480 to 470 million years ago.
    Its remains were found in the Stairway Sandstone near Alice Springs,
    Australia in 1959, but it was not determined that they were the oldest
    known vertebrates until the late 1960s.
                """)

#Child Class Cartilaginous fishes in Fish
class Cartilaginous_fishes(Fish):
    def __init__(self) -> None:
        pass

    #Cartilaginous fishes Show
    def act(self):
        print("""
Cartilaginous fish:

    Chondrichthyes is a class of jawed fish that contains the cartilaginous
    fish or chondrichthyians, which all have skeletons primarily composed
    of cartilage. They can be contrasted with the Osteichthyes or bony fish,
    which have skeletons primarily composed of bone tissue.
                """)

#Child Class Sharks in Cartilaginous fishes from Fish
class Sharks(Cartilaginous_fishes):
    def __init__(self) -> None:
        pass

    #Sharks Show
    def act(self):
        print("""
Shark:

    Sharks are a group of elasmobranch fish characterized by
    a cartilaginous skeleton, five to seven gill slits on the sides 
    of the head, and pectoral fins that are not fused to the head.
    Modern sharks are classified within the clade Selachimorpha
    and are the sister group to the Batoidea.
                """)

#Child Class Batoids in Cartilaginous fishes from Fish
class Batoids(Cartilaginous_fishes):
    def __init__(self) -> None:
        pass

    #Batoids Show
    def act(self):
        print("""
Batoid:

    Batoidea is a superorder of cartilaginous fishes, commonly known as rays.
    They and their close relatives, the sharks, comprise the subclass Elasmobranchii.
    Rays are the largest group of cartilaginous fishes, with well over 600 species
    in 26 families.
                """)

#Child Class Chimaera in Cartilaginous fishes from Fish
class Chimaera(Cartilaginous_fishes):
    def __init__(self) -> None:
        pass

    #Chimaera Show
    def act(self):
        print("""
Chimaera:

    Chimaeras are cartilaginous fish in the order Chimaeriformes,
    known informally as ghost sharks, rat fish, spookfish, or rabbit fish;
    the last three names are not to be confused with rattails, Opisthoproctidae,
    or Siganidae, respectively.
                """)

#Child Class Bony fishes in Fish
class Bony_fishes(Fish):
    def __init__(self) -> None:
        pass

    #Bony fishes Show
    def act(self):
        print("""
Bony fish:

    Osteichthyes, commonly referred to as the bony fish but in the 21st
    century also treated as a clade that includes the tetrapods,
    is a diverse superclass of vertebrate animals that have skeletons 
    primarily composed of bone tissue.
                """)

#Child Atlantic Blue Marlin in Bony fishes from Fish
class AtlanticBlueMarlin(Bony_fishes):
    def __init__(self) -> None:
        pass

    #Atlantic Blue Marlin show
    def act(self):
        print("""
Atlantic Blue Marlin:
                    
    The Atlantic blue marlin (Makaira nigricans) is a
    species of marlin endemic to the Atlantic Ocean.
    It is closely related to, and usually considered
    conspecific with, the Indo-Pacific blue marlin, 
    then simply called blue marlin. Some authorities
    consider both species distinct.
                """)

#Child Class Garfish in Bony fishes from Fish
class Garfish(Bony_fishes):
    def __init__(self) -> None:
        pass

    #Garfish Show
    def act(self):
        print("""
Garfish:
                    
    The garfish (Belone belone), also known as the garpike
    or sea needle, is a pelagic, oceanodromous needlefish
    found in brackish and marine waters of the Atlantic Ocean
    and the Mediterranean, Caribbean, Black, and Baltic Seas.
                """)


#Child Class Birds
class Birds(Animal):
    def __init__(self) -> None:
        pass

    #Birds Show
    def show(self):
        print("""
Bird:

    Birds are a group of warm-blooded vertebrates constituting
    the class Aves, characterised by feathers, toothless beaked jaws,
    the laying of hard-shelled eggs, a high metabolic rate,
    a four-chambered heart, and a strong yet lightweight skeleton.
                """)

    def alive(self):
        print("\nThis animal is alive!")

#Child Class Parrot in Birds
class Parrot(Birds):
    def __init__(self) -> None:
        pass

    #Parrot Show
    def act(self):
        print("""
Parrot:
            
    A bird, often vividly colored, with a short down-curved
    hooked bill, grasping feet, and a raucous voice, found 
    especially in the tropics and feeding on fruits and seeds.
    Many are popular as cage birds, and some are able to 
    mimic the human voice.
                """)

#Child Class Dove in Birds
class Dove(Birds):
    def __init__(self) -> None:
        pass

    #Dove Show
    def act(self):
        print("""
Dove:
            
    A stocky seed- or fruit-eating bird with a small head,
    short legs, and a cooing voice. Doves are generally smaller
    and more delicate than pigeons, but many kinds have
    been given both names.
                """)

#Child Class Budgerigar in Birds
class Budgerigar(Birds):
    def __init__(self) -> None:
        pass

    #Budgerigar Show
    def act(self):
        print("""
Budgerigar:

    The budgerigar, also known as the common parakeet,
    shell parakeet or budgie, is a small, long-tailed,
    seed-eating parrot. Budgies are the only species
    in the genus Melopsittacus. Naturally, the species
    is green and yellow with black, scalloped markings
    on the nape, back, and wings.
                """)

#Child Class Chicken in Birds
class Chicken(Birds):
    def __init__(self) -> None:
        pass

    #Chicken Show
    def act(self):
        print("""
Chicken:

    The chicken is a large and round short-winged bird,
    domesticated from the red junglefowl of Southeast Asia
    around 8,000 years ago. Most chickens are raised for food,
    providing meat and eggs; others are kept as pets or for
    cockfighting.
                """)

#Child Class Owl in Birds
class Owl(Birds):
    def __init__(self) -> None:
        pass

    #Owl Show
    def act(self):
        print("""
Owl:

    Owls are birds from the order Strigiformes, which includes
    over 200 species of mostly solitary and nocturnal birds of
    prey typified by an upright stance, a large, broad head,
    binocular vision, binaural hearing, sharp talons, and feathers
    adapted for silent flight.
                """)


# Child Class Reptiles
class Reptiles(Animal):
    def __init__(self) -> None:
        pass

    def show(self):
        print("""
Reptile:

    Reptiles, as commonly defined, are a group of tetrapods with
    an ectothermic metabolism and amniotic development.
    Living reptiles comprise four orders: Testudines, Crocodilia,
    Squamata, and Rhynchocephalia. As of May 2023, about 12,000 living
    species of reptiles are listed in the Reptile Database.
                """)

    def alive(self):
        print("\nThis animal is alive!")

#Child Class Lizards in Reptiles
class Lizards(Reptiles):
    def __init__(self) -> None:
        pass

    #Lizards Show
    def act(self):
        print("""
Lizard:

    Lizard is the common name used for all squamate reptiles
    other than snakes, encompassing over 7,000 species, ranging
    across all continents except Antarctica, as well as most
    oceanic island chains. The grouping is paraphyletic as some
    lizards are more closely related to snakes than they are
    to other lizards.
                """)

#Child Class Turtles in Reptiles
class Turtles(Reptiles):
    def __init__(self) -> None:
        pass

    #Turtles Show
    def act(self):
        print("""
Turtle:

    Turtles are reptiles of the order Testudines, characterized
    by a special shell developed mainly from their ribs.
    Modern turtles are divided into two major groups, the Pleurodira
    and Cryptodira, which differ in the way the head retracts.
                """)

#Child Class Dinosaur in Reptiles
class Dinosaur(Reptiles):
    def __init__(self) -> None:
        pass

    #Dinosaur Show
    def act(self):
        print("""
Dinosaur:

    Dinosaurs are a diverse group of reptiles of the clade Dinosauria.
    They first appeared during the Triassic period, between 243 and
    233.23 million years ago, although the exact origin and timing
    of the evolution of dinosaurs is a subject of active research.
                """)

#Child Class Snake in Reptiles
class Snake(Reptiles):
    def __init__(self) -> None:
        pass

    #Snake Show
    def act(self):
        print("""
Snake:
            
    Snakes are elongated, limbless, carnivorous reptiles of the suborder
    Serpentes. Like all other squamates, snakes are ectothermic, amniote
    vertebrates covered in overlapping scales.
                """)

#Child Class Crocodile in Reptiles
class Crocodile(Reptiles):
    def __init__(self) -> None:
        pass

    #Crocodile Show
    def act(self):
        print("""
Crocodile:
            
    A large predatory semiaquatic reptile with long jaws,
    long tail, short legs, and a horny textured skin,
    using submersion and stealth to approach prey unseen.
    The crocodile has been extensively hunted for its valuable skin.
                """)

#MAIN-SUB CHOICES
def Choices(animalChoice):
    print("****************************************")
    print("Choices:")
    if animalChoice == "mammal":
        print("\tDog")
        print("\tCat")
        print()
        print("\tBack")
    elif animalChoice == "amphibian":
        print("\tFrog")
        print("\tSalamander")
        print()
        print("\tBack")
    elif animalChoice == "fish":
        print("\tJawless fish")
        print("\tCartilaginous fish")
        print("\tBony fish")
        print()
        print("\tBack")
    elif animalChoice == "bird":
        print("\tParrot")
        print("\tDove")
        print("\tBudgerigar")
        print("\tChicken")
        print("\tOwl")
        print()
        print("\tBack")
    elif animalChoice == "reptile":
        print("\tLizard")
        print("\tTurtle")
        print("\tDinosaur")
        print("\tSnake")
        print("\tCrocodile")
        print()
        print("\tBack")
    print("****************************************")

#DOG CHOICES
def Dog_Choices():
    print("****************************************")
    print("Choices:")
    print("\tGerman Shepherd")
    print("\tBulldog")
    print("\tLabrador Retriever")
    print("\tGolden Retriever")
    print("\tFrench Bulldog")
    print("\tSiberian Husky")
    print()
    print("\tBack")
    print("****************************************")

#CAT CHOICES
def Cat_Choices():
    print("****************************************")
    print("Choices:")
    print("\tSiamese Cat")
    print("\tBritish Shorthair")
    print("\tMaine Coon")
    print("\tPersian Cat")
    print("\tRagdoll")
    print()
    print("\tBack")
    print("****************************************")

#FROG CHOICES
def Frog_Choices():
    print("****************************************")
    print("Choices:")
    print("\tTrue Toad")
    print("\tGlass Frog")
    print("\tAmerican Bullfrog")
    print("\tDesert Rain Frog")
    print("\tSouth American Horned Frog")
    print()
    print("\tBack")
    print("****************************************")

#SALAMANDER CHOICES
def Salamander_Choices():
    print("****************************************")
    print("Choices:")
    print("\tAxolotl")
    print("\tNewt")
    print("\tFire Salamander")
    print("\tChinese Giant Salamander")
    print("\tRed Salamander")
    print()
    print("\tBack")
    print("****************************************")

#JAWLESS FISH CHOICES
def Jawless_Fish_Choices():
    print("****************************************")
    print("Choices:")
    print("\tPteraspidomorphi")
    print("\tHaikouichthys")
    print("\tArandaspis prionotolepis")
    print()
    print("\tBack")
    print("****************************************")

#CARTILAGINOUS FISH CHOICES
def Cartilaginous_Fish_Choices():
    print("****************************************")
    print("Choices:")
    print("\tShark")
    print("\tBatoid")
    print("\tChimaera")
    print()
    print("\tBack")
    print("****************************************")

#BONY FISH CHOICES
def Bony_Fish_Choices():
    print("****************************************")
    print("Choices:")
    print("\tAtlantic Blue Marlin")
    print("\tGarfish")
    print()
    print("\tBack")
    print("****************************************")

#BACK CHOICES
def Back_Choices():
    print("****************************************")
    print("Choices:")
    print()
    print("\tBack")
    print("****************************************")

#BACK FUNCTION
def Back_Function():
    while True:
        user_input = input("Please enter any key to go back: ")
        if user_input == "":
            clear_screen()
            break
        elif user_input.isdigit():
            clear_screen()
            break
        else:
            clear_screen()
            break

#DIFFERENT DOG SPECIES FUNCTION
def Dog_Species(d):
    while True:
        dog.alive()
        dog.act()
        Dog_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(d)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "german shepherd":
            clear_screen()
            german_shepherd.act()
            Back_Function()
        elif user_input == "bulldog":
            clear_screen()
            bulldog.act()
            Back_Function()
        elif user_input == "labrador retriever":
            clear_screen()
            labrador_retriever.act()
            Back_Function()
        elif user_input == "golden retriever":
            clear_screen()
            golden_retriever.act()
            Back_Function()
        elif user_input == "french bulldog":
            clear_screen()
            french_bulldog.act()
            Back_Function()
        elif user_input == "siberian husky":
            clear_screen()
            siberian_husky.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#DIFFERENT CAT SPECIES FUNCTION
def Cat_Species(c):
    while True:
        cat.alive()
        cat.act()
        Cat_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(c)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "siamese cat":
            clear_screen()
            siamese_cat.act()
            Back_Function()
        elif user_input == "british shorthair":
            clear_screen()
            british_shorthair.act()
            Back_Function()
        elif user_input == "maine coon":
            clear_screen()
            maine_coon.act()
            Back_Function()
        elif user_input == "persian cat":
            clear_screen()
            persian_cat.act()
            Back_Function()
        elif user_input == "ragdoll":
            clear_screen()
            ragdoll.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#DIFFERENT FROG SPECIES FUNCTION
def Frog_Species(f):
    while True:
        frog.alive()
        frog.act()
        Frog_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(f)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "true toad":
            clear_screen()
            true_toad.act()
            Back_Function()
        elif user_input == "glass frog":
            clear_screen()
            glass_frogs.act()
            Back_Function()
        elif user_input == "american bullfrog":
            clear_screen()
            american_bullfrog.act()
            Back_Function()
        elif user_input == "desert rain frog":
            clear_screen()
            desert_rain_frog.act()
            Back_Function()
        elif user_input == "south american horned frog":
            clear_screen()
            south_america_horned_frog.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#DIFFERENT SALAMANDER SPECIES FUNCTION
def Salamander_Species(s):
    while True:
        salamander.alive()
        salamander.act()
        Salamander_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(s)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "axolotl":
            clear_screen()
            axolotl.act()
            Back_Function()
        elif user_input == "newt":
            clear_screen()
            newts.act()
            Back_Function()
        elif user_input == "fire salamander":
            clear_screen()
            fire_salamander.act()
            Back_Function()
        elif user_input == "chinese giant salamander":
            clear_screen()
            chinese_giant_salamander.act()
            Back_Function()
        elif user_input == "red salamander":
            clear_screen()
            red_salamander.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#DIFFERENT JAWLESS FISH SPECIES FUNCTION
def Jawless_Fish_Species(j):
    while True:
        jawless_fish.alive()
        jawless_fish.act()
        Jawless_Fish_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(j)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "pteraspidomorphi":
            clear_screen()
            pteraspidomorphi.act()
            Back_Function()
        elif user_input == "haikouichthys":
            clear_screen()
            haikouichthys.act()
            Back_Function()
        elif user_input == "arandaspis prionotolepis":
            clear_screen()
            arandaspis_prionotolepis.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#DIFFERENT CARTILAGINOUS FISH SPECIES FUNCTION
def Cartilaginous_Fish_Species(c):
    while True:
        cartilaginous_fish.alive()
        cartilaginous_fish.act()
        Cartilaginous_Fish_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(c)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "shark":
            clear_screen()
            sharks.act()
            Back_Function()
        elif user_input == "batoid":
            clear_screen()
            batoids.act()
            Back_Function()
        elif user_input == "chimaera":
            clear_screen()
            chimaera.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#DIFFERENT BONY FISH SPECIES FUNCTION
def Bony_Fish_Species(b):
    while True:
        bony_fish.alive()
        bony_fish.act()
        Bony_Fish_Choices()
        user_input = input("\nWhat {} do you want to know? ".format(b)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "atlantic blue marlin":
            clear_screen()
            atlanticblueMarlin.act()
            Back_Function()
        elif user_input == "garfish":
            clear_screen()
            garfish.act()
            Back_Function()
        elif user_input == "back":
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#MAMMAL OPTION
def Option_mammal(m):
    while True:
        clear_screen()
        showAnimals.polyAnimal()
        mammal.show()
        Choices(m)
        user_input = input("\nWhat {} do you want to know? ".format(m)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
        elif user_input == "dog":
            clear_screen()
            Dog_Species(user_input)
        elif user_input == "cat":
            clear_screen()
            Cat_Species(user_input)
        elif user_input == "back":
            clear_screen()
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)

#AMPHIBIAN OPTION
def Option_amphibian(a):
    while True:
        clear_screen()
        showAnimals.polyAnimal()
        amphibian.show()
        Choices(a)
        user_input = input("\nWhat {} do you want to know? ".format(a)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for ax in range(2, 0, -1):
                time.sleep(1)
        elif user_input == "frog":
            clear_screen()
            Frog_Species(user_input)
        elif user_input == "salamander":
            clear_screen()
            Salamander_Species(user_input)
        elif user_input == "back":
            clear_screen()
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for ax in range(2, 0, -1):
                time.sleep(1)
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for ax in range(2, 0, -1):
                time.sleep(1)

#FISH OPTION
def Option_fish(f):
    while True:
        clear_screen()
        showAnimals.polyAnimal()
        fish.show()
        Choices(f)
        user_input = input("\nWhat {} do you want to know? ".format(f)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
        elif user_input == "jawless fish":
            clear_screen()
            Jawless_Fish_Species(user_input)
        elif user_input == "cartilaginous fish":
            clear_screen()
            Cartilaginous_Fish_Species(user_input)
        elif user_input == "bony fish":
            clear_screen()
            Bony_Fish_Species(user_input)
        elif user_input == "back":
            clear_screen()
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)

#BIRD OPTION
def Option_bird(b):
    while True:
        showAnimals.polyAnimal()
        bird.show()
        Choices(b)
        user_input = input("\nWhat {} do you want to know? ".format(b)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "parrot":
            clear_screen()
            parrot.alive()
            parrot.act()
            Back_Function()
        elif user_input == "dove":
            clear_screen()
            dove.alive()
            dove.act()
            Back_Function()
        elif user_input == "budgerigar":
            clear_screen()
            budgerigar.alive()
            budgerigar.act()
            Back_Function()
        elif user_input == "chicken":
            clear_screen()
            chicken.alive()
            chicken.act()
            Back_Function()
        elif user_input == "owl":
            clear_screen()
            owl.alive()
            owl.act()
            Back_Function()
        elif user_input == "back":
            clear_screen()
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#REPTILE OPTION
def Option_reptile(r):
    while True:
        showAnimals.polyAnimal()
        reptile.show()
        Choices(r)
        user_input = input("\nWhat {} do you want to know? ".format(r)).lower()
        if user_input == "":
            clear_screen()
            print("\nNote: Please enter something!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        elif user_input == "lizard":
            clear_screen()
            lizard.alive()
            lizard.act()
            Back_Function()
        elif user_input == "turtle":
            clear_screen()
            turtle.alive()
            turtle.act()
            Back_Function()
        elif user_input == "dinosaur":
            clear_screen()
            dinosaur.alive()
            dinosaur.act()
            Back_Function()
        elif user_input == "snake":
            clear_screen()
            snake.alive()
            snake.act()
            Back_Function()
        elif user_input == "crocodile":
            clear_screen()
            crocodile.alive()
            crocodile.act()
            Back_Function()
        elif user_input == "back":
            clear_screen()
            break
        elif user_input.isdigit():
            clear_screen()
            print("\nGAGO KABAAAAAAA!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            print("\nNote: Please enter a valid choice!")
            for a in range(2, 0, -1):
                time.sleep(1)
            clear_screen()

#MAIN OPTIONS
def Options(animal):
    if animal == "mammal":
        Option_mammal(animal)
    elif animal == "amphibian":
        Option_amphibian(animal)
    elif animal == "fish":
        Option_fish(animal)
    elif animal == "bird":
        Option_bird(animal)
    elif animal == "reptile":
        Option_reptile(animal)

#OBJECT AREA-MAKING FOR CLASSES
showAnimals = Animal()

mammal = Mammal()

#DOG CATEGORY
dog = Dogs()
#DOG SPECIES
german_shepherd = German_Shepherd()
bulldog = Bulldog()
labrador_retriever = Labrador_Retriever()
golden_retriever = Golden_Retriever()
french_bulldog = French_Bulldog()
siberian_husky = Siberian_Husky()

#CAT CATEGORY
cat = Cats()
#CAT SPECIES
siamese_cat = Siamese_cat()
british_shorthair = British_Shorthair()
maine_coon = Maine_Coon()
persian_cat = Persian_cat()
ragdoll = Ragdoll()

amphibian = Amphibian()

#FROG CATEGORY
frog = Frogs()
#FROG SPECIES
true_toad = True_toad()
glass_frogs = Glass_frogs()
american_bullfrog = American_bullfrog()
desert_rain_frog = Desert_rain_frog()
south_america_horned_frog = South_American_horned_frogs()

#SALAMANDER CATEGORY
salamander = Salamander()
#SALAMANDER SPECIES
axolotl = Axolotl()
newts = Newts()
fire_salamander = Fire_salamander()
chinese_giant_salamander = Chinese_giant_salamander()
red_salamander = Red_salamander()

#FISH CATEGORY
fish = Fish()
#JAWLESS FISH CATEGORY IN FISH CATEGORY
jawless_fish = Jawless_fish()
pteraspidomorphi = Pteraspidomorphi()
haikouichthys = Haikouichthys()
arandaspis_prionotolepis = Arandaspis_prionotolepis()
#CARTILAGINOUS FISH CATEGORY IN FISH CATEGORY
cartilaginous_fish = Cartilaginous_fishes()
sharks = Sharks()
batoids = Batoids()
chimaera = Chimaera()
#BONY FISH CATEGORY IN FISH CATEGORY
bony_fish = Bony_fishes()
atlanticblueMarlin = AtlanticBlueMarlin()
garfish = Garfish()

#BIRD CATEGORY
bird = Birds()
parrot = Parrot()
dove = Dove()
budgerigar = Budgerigar()
chicken = Chicken()
owl = Owl()

#REPTILE CATEGORY
reptile = Reptiles()
lizard = Lizards()
turtle = Turtles()
dinosaur = Dinosaur()
snake = Snake()
crocodile = Crocodile()

#MAIN
while True:
    print("\nTITLE: MY ANIMAL DICTIONARY")
    showAnimals.printAnimals()
    user_input = input("\nWhat animal do you want to know? ").lower()
    if user_input == "":
        clear_screen()
        print("\nNote: Please enter something!")
        for a in range(2, 0, -1):
            time.sleep(1)
        clear_screen()
    elif user_input == "mammal":
        Options(user_input)
    elif user_input == "amphibian":
        Options(user_input)
    elif user_input == "fish":
        Options(user_input)
    elif user_input == "bird":
        clear_screen()
        Options(user_input)
    elif user_input == "reptile":
        clear_screen()
        Options(user_input)
    elif user_input == "exit":
        clear_screen()
        print("\n\nThanks Bye!")
        for a in range(3, 0, -1):
            time.sleep(1)
        break
    elif user_input.isdigit():
        clear_screen()
        print("\nGAGO KABAAAAAAA!")
        for a in range(2, 0, -1):
            time.sleep(1)
        clear_screen()
    else:
        clear_screen()
        print("\nNote: Please enter a valid choice!")
        for a in range(2, 0, -1):
            time.sleep(1)
        clear_screen()
