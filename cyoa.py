"""This is a Choose Your Own Adventure game. Something akin to a very simple RPG."""

__author__ = "730553817"

from random import randint
player: str = ""
points: int = 0
# The following procedure is the main game loop


def main() -> None:
    """When called will run the basic game loop."""
    global points
    greet()
    playing: str = ""
    print("Your sucess in Sons of Arnor will be determined by Adventure Points.")
    print(f"Currently you have {points} Adventure Points.")
    print()

    print("You awake in an inn of the small town Canondin in the province of Jundterland, the homeland of the Dwarves.")
    print()
    
    playing: str = input("Would you like to continue playing?")
    print()
    while playing == "Yes":
        encounter_choice: str = input("Three opportunities present themselves for the days adventure: You can explore the town, nearby mountains, or a dark forest. What do you choose?")
        print()

        if encounter_choice == "Town":
            points = thieves(points)
            print(f"You now have {points} Adventure Points!")
            print()
        
        elif encounter_choice == "Forest":
            orc()
         
        elif encounter_choice == "Mountains":
            dragon()
         
        playing: str = input("Would you like to continue playing?")
        print()
    
    else: 
        end_game()
        

# The following procedure simulates the game greeting the player


def greet() -> None:
    """Welcomes the player and asks for their name."""
    global player
    player = input("What is your name?")
    print(f"Welcome, {player}, to Sons of Arnor, a 'short RPG'.")
    print()
    

# The following procedure ends the game loop


def end_game() -> None:
    """Ends the main game loop."""
    global points
    print(f"Thank you so much for playing Sons of Arnor, {player}!")
    print(f"You ended the game with {points} Adventure Points! Have a nice day!")


# The following function creates a health-bar for each enemy


def health_bar(health: int, version: int) -> str:
    """Creates a healthbar based on an enemy's health."""
    global FULL_THIEVES_HEALTH
    global FULL_DRAGON_HEALTH
    global FULL_ORC_HEALTH
    GREENBOX: str = "\U0001f7e9"
    REDBOX: str = "\U0001f7e5"
    health_bar: str = ""
    
    if version == 1:
        health_bar = GREENBOX * health
        health_bar += (FULL_DRAGON_HEALTH - health) * REDBOX
        return health_bar
   
    elif version == 2:
        health_bar = GREENBOX * health
        health_bar += (FULL_ORC_HEALTH - health) * REDBOX
        return health_bar
      
    elif version == 3: 
        health_bar = GREENBOX * health
        health_bar += (FULL_THIEVES_HEALTH - health) * REDBOX
        return health_bar
        

# The following procedure is designed to simulate attacks on a dragon


def attack_dragon(attack_version: int) -> None:
    """Simulates attacks on the dragon."""
    global points
    global DRAGON_HEALTH

    if attack_version == 1:
        print("The dragon unleashes a wall of fire from its mouth. You dodge to the side and quickly slash its legs.")
        print()
        damage: int = randint(4, 6)
        DRAGON_HEALTH -= damage
        points += 3

    elif attack_version == 2:
        print("The dragon jumps from the ground and flies toward you. You luckily managed to grab onto its leg before it slams into you.")
        print("Before it manages to grab you, you stab it vigorously and jump off.")
        print()
        damage = randint(8, 10)
        DRAGON_HEALTH -= damage
        points += 4

    elif attack_version == 3:
        print("The dragon charged with a fiery ferocity. Its massive claws swiping at you. Luckily, you manage to cut one of its fingers off and dodge.")
        print()
        damage = randint(10, 15)
        DRAGON_HEALTH -= damage
        points += 5


# The following procedure simulates an encounter with a dragon


def dragon() -> None:
    """Faces the player against a dragon."""
    global FULL_DRAGON_HEALTH
    global DRAGON_HEALTH
    global points
    FULL_DRAGON_HEALTH = 25
    DRAGON_HEALTH = 25
    death: int = 0
    print(f"You, {player}, are walking through an underground fortress when a massive rumble nearly shakes you from your feet.")
    print("In the distance you see it, a huge dragon. And behind it, a diamond the size of your head.")
    print()

    run_or_fight: str = input("You have two options: run or fight. How do you choose?")
    print()
    
    if run_or_fight == "Run":
        print("The dragon roars with the thunder of a thousand armies as you make your escape.")
        print("You make it out alive, but you have found no treasure nor killed any beast.")
        print()

        print(f"You have {points} Adventure Points!")
        print()

    else:
        print("The dragon rises from it's gold, the ground shakes as it begin to walk toward you.")
        print()

        while DRAGON_HEALTH > death:
            if DRAGON_HEALTH == 25:
                print("Dragon Health")
                print(health_bar(DRAGON_HEALTH, 1))
                print()
                attack_choice = input("You rush at it, screaming. You can either use a light attack, heavy attack, or a critical attack. What do you choose?")     
                print()

            else:
                attack_choice = input("The dragon spews fire in anger leaving him open for another attack. What do you do?")
                print()

            if attack_choice == "Light Attack":
                attack_dragon(1)
                print("Dragon Health")
                print(health_bar(DRAGON_HEALTH, 1))
                print()
            if attack_choice == "Heavy Attack":
                attack_dragon(2)
                print("Dragon Health")
                print(health_bar(DRAGON_HEALTH, 1))
                print()
            if attack_choice == "Critical Attack":
                attack_dragon(3)
                print("Dragon Health")
                print(health_bar(DRAGON_HEALTH, 1))
                print()

        else:
            points += randint(7, 9)
            print("You have defeated the mighty dragon and its treasure is yours!")
            print(f"You now have {points} Adventure Points!")
            print()

            print("You begin to walk back to town in search of a nice bed to lie in.")
            print()


# The following procedure is designed to simulate attacks on an orc


def attack_orc(attack_version: int) -> None:
    """Simulates different attacks on an orc."""
    global points
    global ORC_HEALTH

    if attack_version == 1:
        print("The massive orc swings its sword toward your head, however, you duck and quickly slice at its leg.")
        print("The orc screams in pain, 'Man-filth'!")
        print()
        damage: int = randint(2, 4)
        ORC_HEALTH -= damage
        points += 2

    elif attack_version == 2:
        print("The orc jumps into the air bringing its sword above its head. ")
        print("Seeing this you quickly roll out of range for the orc to hit you and bring your sword around, cleaving the orc in the chest.")
        print()
        damage = randint(4, 6)
        ORC_HEALTH -= damage
        points += 3

    elif attack_version == 3:
        print("The orc, feeling a rush of fatigue, lowers his sword for a split-second.")
        print("Seeing this opportunity you swing your sword with all the might you have, slicing off one of the orc's arms.")
        print()
        damage = randint(7, 12)
        ORC_HEALTH -= damage
        points += 4


# The following procedure simulates an encounter with an orc


def orc() -> None:
    """Faces the player against an orc."""
    global FULL_ORC_HEALTH
    global points
    global ORC_HEALTH
    FULL_ORC_HEALTH = 20
    ORC_HEALTH = 20
    death: int = 0
    print(f"You, {player}, are exploring the dark forest of Lounderwood when a screeching sound deafens you for a moment.")
    print("From behind a tree comes sprinting an orc, one the size of a small ogre. In it's hand it holds an dragonscaled sword.")
    print()

    run_or_fight: str = input("You have two options: run from the orc or fight. What do you choose?")

    print()

    if run_or_fight == "Run":
        print("You turn to flee but the orc manages to slash at your back.")
        print("You make it out alive but pain etches across your face as your back bleeds from the wound.")
        print()

        points -= 2
        print(f"You now have {points} Adventure Points!")
        print()

    else:
        
        while ORC_HEALTH > death:
            if ORC_HEALTH == 20:
                print("Orc Health")
                print(health_bar(ORC_HEALTH, 2))
                print()
                attack_choice = input("You stand your ground. You can either use a light attack, heavy attack, or a critical attack. What do you choose?")
                print()

            else: 
                attack_choice = input("The orc stands after your attack leaving him open for another attack. What do you do?")
                print()

            if attack_choice == "Light Attack":
                attack_orc(1)
                print("Orc Health")
                print(health_bar(ORC_HEALTH, 2))
                print()
            if attack_choice == "Heavy Attack":
                attack_orc(2)
                print("Orc Health")
                print(health_bar(ORC_HEALTH, 2))
                print()
            if attack_choice == "Critical Attack":
                attack_orc(3)
                print("Orc Health")
                print(health_bar(ORC_HEALTH, 2))
                print()

        else:
            print("You have defeated the massive orc and you claim his dragonscaled sword!")
            print()
            points += randint(5, 7)
            print(f"You now have {points} Adventure Points!")
            print("You begin your search for a town to rest your aching body in.")
            print()
            

# The following functions simulate attacks on dwarven thieves


def attack_thieves(points: int, attack_version: int) -> None:
    """Simulates different attacks on thieves."""
    global THIEVES_HEALTH

    if attack_version == 1:
        print("The dwarf that spoke begins walking toward you and pulls an axe from under his cloak.")
        print("Quickly, you unsheathe your sword and cut the dwarf along its leg. He seems rather unaffected though.")
        print()
        damage: int = randint(1, 3)
        THIEVES_HEALTH -= damage
        points = points + 1
        return points

    elif attack_version == 2:
        print("Two of the dwarves that were behind you scream in anger, launching themselves at you.")
        print("You deflect one of the blows from one of the dwarves and slash him in the throat leaving him a lifeless corpse on the ground.")
        print()
        damage: int = randint(4, 6)
        THIEVES_HEALTH -= damage
        points = points + 2
        return points

    elif attack_version == 3:
        print("Each one of the dwarves attacks you at once, however, you, being such a skilled swordsman, cut atleast half of them down.")
        print()
        damage: int = randint(7, 10)
        THIEVES_HEALTH -= damage
        points = points + 3
        return points


# The following function simulates an encounter with dwarven thieves


def thieves(points: int) -> int:
    """Faces the player against dwarven thiefs."""
    global THIEVES_HEALTH
    global FULL_THIEVES_HEALTH
    FULL_THIEVES_HEALTH = 15
    THIEVES_HEALTH = 15
    death: int = 0
    print(f"You, {player}, are walking down an alley in the town of Canondin when you hear a voice from ahead.")
    print("'Where do you think you're going lad?' A shadow emerges from the corner and suddenly you are surrounded by dwarves.")
    print("'Give us your gold and silver and perhaps we'll let you go!'")
    print()

    run_or_fight: str = input("You have two options: run from the thieves or fight. What do you choose?")
    print()

    if run_or_fight == "Run":
        print("You whip around and sprint away as fast as possible but one of dwarves throws their axe at you.")
        print("The axe hits you in the arm but you manage to stay on your feet and keep running. Blood drips from your fingers but you are alive.")
        print()

        if points != 0: 
            points = points - 1
        return points

    else:
        while THIEVES_HEALTH > death:
            if THIEVES_HEALTH == 15:
                print("Thieves Health")
                print(health_bar(THIEVES_HEALTH, 3))
                print()
                attack_choice = input("You stand your ground. You can either use a light attack, heavy attack, or a critical attack. What do you choose?")
                print()
            else:
                attack_choice = input("The dwarves ready themselves again, preparing for the next attack. What do you do?")
                print()

            if attack_choice == "Light Attack":
                attack_thieves(points, 1)
                print("Thieves Health")
                print(health_bar(THIEVES_HEALTH, 3))
                print()
            if attack_choice == "Heavy Attack":
                attack_thieves(points, 2)
                print("Thieves Health")
                print(health_bar(THIEVES_HEALTH, 3))
                print()
            if attack_choice == "Critical Attack":
                attack_thieves(points, 3)
                print("Thieves Health")
                print(health_bar(THIEVES_HEALTH, 3))
                print()

        else:
            print("You have defeated the dwarven thieves and their gold and valubles are yours to claim.")
            print("You quietly flee the town, searching for a new place to call home for a time.")
            print()
            points += randint(4, 6)
            return points
        

if __name__ == "__main__":
    main()