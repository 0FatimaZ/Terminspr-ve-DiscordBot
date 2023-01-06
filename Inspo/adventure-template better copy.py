
### Helper functions for displaying rooms ###

#Inventory system

area_0_items = ["seashells"]

area_0_5_items = []

area_1_items = ["coconuts", "leaves", "spiders", "exotic fruits", "bottle of pills"]

area_2_items = []

area_2_5_items = ["rope", "yoghurt container", "bat", "anime character mask", "motoroil", "rubber duck"]

area_3_items = []

area_4_items = ["book"]

inventory = [""]

def get_area_items(current_area):
    """Find the list of items in the room.""" 
    if current_area == 0:
        return area_0_items
    elif current_area == 0.5:
        return area_0_5_items
    elif current_area == 1:
        return area_1_items
    elif current_area == 2:
        return area_2_items
    elif current_area == 2.5:
        return area_2_5_items
    elif current_area == 3:
        return area_3_items
    elif current_area == 4:
        return area_4_items
    else:
        return []
        
def snatch_item(item, current_area):
    if len(inventory) == 6:
        print("I can't carry that many things!")
        return()
    items = get_area_items(current_area)
    if item in items:
        items.remove(item)
        inventory.append(item)
        print("I picked up the " + item + ".")
        if item == "book":
            print("The bagel was fresh out of the oven. It was hot and steamy. 'Y/N I- I think I'm ready'. Y/N grabbed the butter from the fridge. 'Well don't mind if I do'. Y/N slowly picked up the knife and-")
            print("I don't think I can read any more of this. I proberbly will never look at a bagel the same way again.")
    else:
        print("I can't see any " + item + ".")

def throw_item(item, current_area):
    items = inventory
    if item in items:
        items.remove(item)
        get_area_items(current_area).append(item)
        print("Let me put the " + item + " here.")
    else:
        print("I don't have any " + item + ".")
    
def show_inventory(inventory):
    for x in inventory:
        print(x)
        
def examine_item(item):
    """It explores certain items"""
    if "book" in area_4_items:
        if item == "square":
            print("It seems to be a book of some sort.")
    else:
        print("Why would I waste my time exploring that?")

def explore_feet(item):
    if item == "footprints":
        print("Hmm, these are fresh. Someone is here. Let me try and call out.")

#Codes for the island map
        
def show_area_0():
    """Display the contents of the northern area."""
    print("It seems that I'm at an abandoned beach. I can see a boat. ")
    print("I can see a lot of pretty seashells. They remind me of Nagito.")
    if len(area_0_items) >= 1:
        print("I can take the", ", ".join(area_0_items))
    else:
        print("Nothing to take.")

def show_area_0_5():
    """Displays the contents of the extension of area 0"""
    print("This is the boat.")
    if len(area_0_5_items) >= 1:
        print("I have put the", ", ".join(area_0_5_items), "here.")
    else:
        print("Nothing but the boat.")
    
def show_area_1():
    """Displays contents of the center area ."""
    print("I see a lot of trees. This must be a forest.")
    print("There are four paths I can take.")
    if len(area_1_items) >= 1:
        print("I can see a lot of", ", ".join(area_1_items))
    else:
        print("Nothing to take.")

def show_area_2():
    """Displays contents of the western area."""
    print("This is a beach. A bunch of junk is scattered.")
    if len(area_2_items) >= 1:
        print("I can see a lot of", ", ".join(area_2_items))

def show_area_2_part2():
    """Displays contents of the area within the western area."""
    print("I can see a bunch of stuff. Only a few are catching my eye tho.")
    print(", ".join(area_2_5_items))
    
def show_area_3():
    """Displays contents of the southern area."""
    print("This in the other side of the island.")
    print("I see some footprints on the sand.")
    if len(area_3_items) >= 1:
        print("I can see a lot of", ", ".join(area_3_items))

def show_area_4():
    """Displays contents of the eastern area."""
    print("I can see a mountain here")
    print("...")
    print("I am NOT climbing that.")
    if "book" in area_4_items:
        print("Hmmm, I can see something square there.")
    
def show_area(area_num):
    """Display the contents of the given room.
    Input:
    - room_num : int, the number of the room to show.
    """
    if area_num == 0:
        show_area_0()
    elif area_num == 0.5:
        show_area_0_5()
    elif area_num == 1:
        show_area_1()
    elif area_num == 2:
        show_area_2()
    elif area_num == 2.5:
        show_area_2_part2()
    elif area_num == 3:
        show_area_3()
    elif area_num == 4:
        show_area_4()
    else:
        return 1

def move_from_area_0(direction):
    """ Area 0 only has a single exit , which leads to the center area 1. """
    if direction == "s":
        print("A plant just smacked my face. Goddamn nature.")
        return 1
    if direction == "e":
        return 0.5
    else:
        print("That's the sea. What, am I gonna do? Swim? As if.")
        return 0
        
def move_from_area_0_5(direction):
    """This is an extension of area 0, so you can only move back to area 0"""
    if direction == "w":
        return 0
    else:
        print("What's the point of going there?")
        return 0.5

def move_from_area_1(direction):
    """ Area 1 has 4 exit , which leads to all other areas. """
    if direction == "n":
        return 0
    elif direction == "w":
        return 2
    elif direction == "s":
        return 3
    elif direction == "e":
        return 4
    else:
        return ("What am I doing?")

def move_from_area_2(direction):
    """ Area 2 has two exits, which leads to area 1. """
    if direction == "e":
        return 1
    if direction == "w":
        return 2.5
    else:
        print("Crap. This junk never ends.")
        return 2

def move_from_area_2_5(direction):
    """ Area 2.5 only has a single exit , which leads to area 2. """
    if direction == "e":
        return 2
    else:
        print("Should I take something?")
        return 2.5

def move_from_area_3(direction):
    """ Area 3 only has a single exit , which leads to area 1."""
    if direction == "n":
        return 1
    else:
        print("Nothing but the beach. We really are stuck here.")
        return 3

def move_from_area_4(direction):
    """ Area 4 only has a single exit , which leads to the center area 1. """
    if direction == "w":
        return 1 
    else:
        print("I already said that I'm NOT climbing the mountain.")
        return 4
        
#Dialog
        
def empty_dialog():
    """Empty dialog to let the player know that the button works"""
    print("Hajime: 'Is anyone there?!")
    input()
    print("...")
    input()
    print("I must be going crazy here.")
    input()
    
def empty_dialog_2():
    """Empty dialog to let the player know that the button works"""
    print("Hajime: 'Is anyone there?!")
    input()
    print("Something just came out.")
    input()
    print("Is that a monkey?")
    input()
    print("Ah! The monkey just threw a coconut at my head. I think I have a concussion now.")
    input()

def dialog_1():
    """First dialog with Nagito Komaeda"""
    print("Hajime: 'Is anyone there?!'")
    input()
    print("Nagito: 'H-Hajime!'")
    input()
    print("I see a tall skinny figure. Nagito? It seems like his pale soft skin has reddened under the sun, giving him a glow.")
    input()
    print("Nagito runs towards me and gives me a big hug, and I can feel soft hair against my skin… In a bro-way.")
    input()
    print("Hajime: 'Why are you all the way on the other side of the island?'")
    input()
    print("Nagito: 'I was looking for stuff to fix the boat. You did see the boat on the beach, correct?'")
    input()
    print("Hajime: 'Yeah, I did. Do you need me to find anything?'")
    input()
    print("Nagito: 'Actually now that you mention it, yeah. I could use some help.'")
    input()
    print("Nagito: 'I need you to find some items, while I try to fix the boat.'")
    input()
    print("Hajime: 'Alright. What do you need?'")
    input()
    print("Nagito: 'I need you to find a duck, some pills, some motoroil, a rope and lastly yoghurt.'")
    input()
    print("Hajime: 'Alright... I'll find them...'")
    input()
    print("Nagito: 'Great Hajime. I'll be waiting by the boat. You can just drop the items there.'")
    input()
    print("Hajime: 'See you later da-... bro.'")
    input()
    print("What does he need all these items for? Almost none of them have anything to do with a boat.")
    input()

def dialog_2():
    """Last dialog with Nagito bestie"""
    print("I can see Nagito beside the boat.")
    input()
    print("Hajime: 'Nagito! I got the things you asked for.'")
    input()
    print("Nagito: 'Ah! Hajime, thank you, I truly admire and love-'")
    input()
    print("The motor suddenly sparked and made a loud noise. Seems like it's up and running… wait-")
    input()
    print("Nagito: '-and thats why I'm telling you that I-'")
    input()
    print("Hajime: 'Wait! Nagito why did I have to get you all these things if you didn't need them to fix the boat?'")
    input()
    print("Nagito: 'Oh, I just needed my pills that I dropped and I thought that looking for stuff would make the time go faster for you. I didn't think you'd actually find all the things for me, you simp.'")
    input()
    print("Hajime: 'Then how did you know I would get you the pills?'")
    input()
    print("Nagito: 'Pure luck, I guess'")
    input()
    print("...")
    input()
    print("We finally got on the boat. Nagito is sitting close to me. It's a rather small boat.")
    input()
    print("Nagito: 'We did it Hajime.' He is giving me a big smile.")
    input()
    print("And what a lovely smile it is.")
    input()
    print("(It seems like you won. Lucky player.)")
    
def b_e():
    """Bonus ending if you give Nagito the book"""
    print("!Bonus ending!")
    input()
    print("Hajime: 'By the way Nagito, I found this book near the mountain.'")
    input()
    print("He picks up his head and looks at me. Is it just me, or does he look flustered?")
    input()
    print("Nagito: 'Give me that!'")
    input()
    print("He takes the book from my hand and throws it into the ocean.")
    input()
    print("Nagito: 'Ups, my hand slipped. Besides, it's not mine.'")
    input()
    print("Then why does he look so relieved?")
    input()
    print("Hajime: 'Ok, because I could swear I saw your initials in it.")
    input()
    print("Nagito: 'Staying in the island must have made you crazy Hajime...'")
    input()
    print("Does he think I'm crazy?")
    input()
    print("(Thank you for playing.)")
    
#Help
    
def tutorial():
    print("(Hello! It seems that you're not that bright. That's ok!")
    print(" ")
    print("To move to another area press 'n' or 'w' or 'e' or 's', remember that you can't move in any direction in specific areas.")
    print(" ")
    print("To get a description of the area you're in press 'l'.")
    print(" ")
    print("To pick up items on the way press 'p' and then type the item you want to pick up.")
    print(" ")
    print("To throw away an item press 't' and then type the item you want to throw away.")
    print(" ")
    print("To see your inventory press 'i'.")
    print(" ")
    print("To call out for someone or the air press 'c'.")
    print(" ")
    print("To examine an item press 'x' and type the item you want to examine.")
    print(" ")
    print("That's all!)")
    
#Code for conditions of winning the game
    
def area_0_5_conditions():
    if "rubber duck" in area_0_5_items and "bottle of pills" in area_0_5_items and "motoroil" in area_0_5_items and "rope" in area_0_5_items and "yoghurt container" in area_0_5_items:
        dialog_2()
        if "book" in area_0_5_items:
            b_e()
    else:
        print("Nagito: 'Hajime, you're supposed to be looking for the items.'")
        input()

  
### The main game loop ###


def game_loop():
    """Main loop of the game - this is where the fun happens."""
    print("(You probably don't need any help, 'cause you're such a smartypants, but if the immposible happens, press 'h' for help.")
    print("Press 'enter' to start the game. Enjoy.)")
    input()
    print("There is no sign of my friend.")
    
    talkedtonpc = False

    # We start in area n
    current_area = 0

    # Display the area that we start in
    show_area(current_area)

    # Enter the main loop, where the user can input commands.
    while True:
        user_inp = input("> ").lower()

        if user_inp == "quit":
            break
        elif user_inp == "n" or user_inp == "w" or user_inp == "e" or user_inp == "s":
            old_area = current_area
            if current_area == 0:
                current_area = move_from_area_0(user_inp)
            elif current_area == 0.5:
                current_area = move_from_area_0_5(user_inp)                
            elif current_area == 1:
                current_area = move_from_area_1(user_inp)
            elif current_area == 2:
                current_area = move_from_area_2(user_inp)                
            elif current_area == 2.5:
                current_area = move_from_area_2_5(user_inp)
            elif current_area == 3:
                current_area = move_from_area_3(user_inp)                
            elif current_area == 4:      
                current_area = move_from_area_4(user_inp)
                
            if current_area != old_area:
                show_area(current_area)
        elif user_inp == "h":
            tutorial()
        elif user_inp [0] == "p":
            item = user_inp[2:]
            snatch_item(item, current_area)
        elif user_inp [0] == "t":
            item = user_inp[2:]
            throw_item(item, current_area)
        elif user_inp == "l":
            show_area(current_area)
        elif user_inp == "i":
            show_inventory(inventory)
        elif user_inp [0] == "x":
            item = user_inp[2:]
            if current_area == 4:
                examine_item(item)
            if current_area == 3:
                if not talkedtonpc:
                    explore_feet(item)
                if talkedtonpc:
                    print("Stop. Wasting. Time!")
            if current_area != 4 and current_area != 3:
                print("Why would I waste my time exploring that?")
        elif user_inp == "c":
            if current_area == 0:
                empty_dialog()
            elif current_area == 1:
                empty_dialog_2()
            elif current_area == 2:
                empty_dialog()
            elif current_area == 2.5:
                empty_dialog()
            if current_area == 3:
                if not talkedtonpc:
                    dialog_1()
                    talkedtonpc = True
                else:
                    empty_dialog()
            elif current_area == 4:
                empty_dialog()
            elif current_area == 0.5:
                if not talkedtonpc:
                    empty_dialog()
                elif talkedtonpc:
                    area_0_5_conditions()
                    break
    
        else:
            print("What is", "'", user_inp, "'", "supposed to mean? Am I going crazy?")

# Start the game!
game_loop()