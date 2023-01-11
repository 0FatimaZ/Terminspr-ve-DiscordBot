from pdb import Restart
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True


client = discord.Client(intents=intents)
TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")




current_room = 1
things = 0


#Klasser & objekter
class room:
    def __init__(self,name,surroundings):
        self.name = name
        self.surroundings = surroundings
        
    def show(self):
        return self.name + "description: " + self.surroundings 

#Dictionaries

things_to_find = {
    "note1" : False,
    "note2" : False,
    "guts" : False,
    "glass" : False,
    "eyes" : False,
    "pen" : False
}

investigate_things = {
    "fridge" : False,
    "window" : False,
    "hole" : False,
    "under_bed" : False,
    "door" : False
}

room_0 = room("Bathroom ", "I am in the bathroom."
     "I can see my mirror, it's a bit dirty"
     "What is that on the wall?")
    
room_1 = room("Bedroom ", "I am in my bedroom."
"It's rather empty, no pictures on the wall... I really wish I had something to hang."
"My bed looks comfortable.")

room_2 = room("Livingroom ", "I am in the livingroom."
"Not much living happening here..."
"There is a window to the side, and my frontdoor.")

room_3 = room("Kitchen ", "I am in the kitchen"
"Am I hungry? I may have some food in the frigde."
"There is something on the wall here aswell, weird.")


def show_room(current_room):
    if current_room == 0:
        return room_0.show()
    elif current_room == 1: 
        return room_1.show()
    elif current_room == 2:
        return room_2.show()
    elif current_room == 3:
        return room_3.show()
    

def move_from_room_0(direction):
    if direction == "e": 
        return 1
    elif direction == "s":
        things_to_find["note1"] == True
        return "There's a note on the wall.."
    else:
        return 0

def move_from_room_1(direction):
    if direction == "s": 
        return 2
    elif direction == "w":  
        return 0
    elif direction == "e":
        things_to_find["bed"] == True
        return "What a comfortable bed."
    else: 
        return 1
    
def move_from_room_2(direction):
    if direction == "e":
        return 3
    elif direction == "n":
        return 1
    elif direction == "s":
        return 4
    elif direction == "west":
        things_to_find["window"] == True
        return "Why's my window so dirty..."
    else: 
        return 2

def move_from_room_3(direction):
    if direction == "w": 
        return 2
    elif direction == "s":
        things_to_find["note2"] == True
        return "What's that stain... oh wait, there's a sticky note"
    elif direction == "east":
        things_to_find["fridge"] == True
        return "Here's the fridge, am I hungry?"
    else: 
        return 3

def look_in_room(current_room):
    if current_room == 0:
        return show_room(current_room)
    elif current_room == 1:
        return show_room(current_room)
    elif current_room == 2: 
        return show_room(current_room)
    elif current_room == 3:
        return show_room(current_room)
    elif current_room == 4:
        return show_room(current_room) 

#fukntion til dialog

def dialog_1(choice):
    print("Something is in the keyhole... what is that?")
    input()
    print("...")
    input()
    print("AAAGH!")
    input()
    print("Unknown: 'My... what a pretty being you are.'")
    input()
    print("'Who... who are you?'")
    input()
    print("Unknown: 'How about you open the door and let me in.'")
    input()
    print("'I'm not letting you inside my home. I don't even know you.'")
    input()
    print("Unknown: 'But you do know me. If you open the door you could see me.")
    input()
    print("I could look at them through the peephole.")
    input()
    print("What? Are they covering the peephole? I can't let an unidentified person in my home.")
    input()
    print("'Go away. I'm going to call the police.")
    input()
    print("Unkown: 'Nonono, no need to act rash my love. I'm sorry if I'm creeping you out. It's just that we haven't seen each other in so long... I miss you.'")
    input()
    print("Honestly I'm curious as to who it is.")
    input()
    print("Should I open the door? yes or no?")
    input()
    if choice == "yes":
        print("'Fine. I'm going to open the door. Step back.'")
        input()
        print("'Unknown: 'Thank you gorgeous, you won't regret it.'")
        input()
        print("'That's weird, I can't open it.'")
        input()
        print("Unknown: 'It must be locked. Do you know where the key is?'")
        input()
        print("'Yeah, let me go get it'")
        input()
    if choice == "no":
        print("'I am not opening the door to a stranger.'")

def investigate(current_room, direction):
    if current_room == 0:
        if direction == "s":
            if things_to_find["note1"] == True:
                if investigate_things["hole"] == True:
                    return "How long has that hole been there?"
                    return "I feel like I dont wanna know the answer to that."
                else: 
                    investigate_things["hole"] == True
                    things =+ 1
                    return "There's a hole in the wall." 
                    return "I don't dare to look through it."
            else:
                "Just a sad wall."
        elif direction == "n":
            return "Nothing but my own tired reflection."
        elif direction == "e":
            return "The way to my bedroom."
        else:
            return "Just a sad empty wall."
    elif current_room == 1:
        if direction == "e":
            if investigate_things["bed"] == True:
                if things_to_find["glass"] == True:
                    if things_to_find["pen"] == True:
                        return "I can't sleep."
                        return "Not right now."
                        return "Something's..."
                        return "Not right..."
                    else:
                        things_to_find["pen"] == True
                        return "There's a pen."
                        return "Feels kinda gross, thinking about how long it must've been there."
                else:
                    investigate_things["glass"] == True
                    things =+ 1
                    return "There's something under my bed."
                    return "It's a glass filled with yellow liquid and a note that says 'DRINK ME :)'..."
                    return "I better not."
            else: 
                return "My bed is over there."
        elif direction == "w":
            return "The way to the bathroom."
        elif direction == "s":
            return "The way to the livingroom."
        else:
            "Just a sad empty wall. I should really decorate my walls."

    elif current_room == 2: 
        if direction == "n":
            return "The way to my bedroom."
        elif direction == "s":
            if investigate_things["door"] == True:
                    return dialog_1()
            else:
                investigate_things["door"] == True
                return "I take a step closer to my door."
                return "I'm getting nervous now."
                return "Something definitely feels off..."
                return "I move my head to look through the keyhole. I see nothing at first, but as I get used to the darkness..."
                return "I see an eye, peeping right back at me."
                return "Frozen with fear, I can do nothing but look right back, at the strange eye on the other side."
                return dialoge()
        elif direction == "e":
            if investigate_things["window"] == True:
                if things_to_find["eyes"] == True:
                    return "I can still feel the intense stare"
                else:
                    things_to_find["eyes"] == True
                    things =+ 1
                    return "I stare blankly out the window."
                    return "It's dark outside."
                    return "The longer I stare, the more I feel like I can see two creepy eyes watching me."
                    return "Observing my every move."
            else:
                return "I feel a slight breeze comming from that direction."
        elif direction == "w":
            return "The way to the kitchen."
        else:
            return "My living room is so empty and lifeless."
            return "Feels more like a 'dying'-room if you ask me."

    elif current_room == 3: 
        if direction == "n":
            return "Nothing but dirty dishes that have been piling up, over the course of the last couple of days."
        elif direction == "s":
            if things_to_find["note2"] == True:
                return "Looking clooser, the wall is stained with the smelly goo."
                return "When did I last clean this kitchen?"
            else:
                things_to_find["note2"] == True
                things =+ 1
                return "I grab the stickynote off the wall."
                return "It says 'DID YOU LIKE THE MEAL I PREPARED FOR YOU? ^_^'."
                return "The stickynote is covered in a gooey matter. The smell is indescriptible."
                return "I feel like throwing up."
                if things_to_find["guts"] == True:
                    return "Again."

        elif direction == "e":
            if investigate_things["fridge"] == True:
                if things_to_find["guts"] == True:
                    return "I'm too scared to look in the fridge again."
                else:
                    things_to_find["guts"] == True
                    things =+ 1
                    return "I open the fridge without a second thought, only to be met by the most awful smell imaginable."
                    return "The botton drawer of my fridge is practically drowning in an unidentifiable matter."
                    return "The only word I can think of to describe what I am seeing, is grusome."
                    return "I threw up in the trash. I feel awful."
            else:
                return "My fridge is over there."
        elif direction == "w":
            return "The way to the livingroom."
        else:
            return "This kitchen is so damn nasty. But it's home."





@client.event
async def on_message(message):
    global current_room
    global things
    global run_game
    contents = message.content
    user = message.author.id
    
    #introduction
    
    while True:
        if contents.startswith("!quit"):
            message.channel.send("Are you sure you want to quit? y/n")
            if contents.startswith("y"):
                Restart
            if contents.startswith("n"):
                await message.channel.send("Then keep going!")
        elif contents.startswith("!help"):
            reply = ['"!look" gives you a short description of the room that you are currently in.',
                '"!walk" lets you walk in whichever direction you type afterwards (n, w, e or s).',
                '"!investigate" lets you investigate whatever is in your chosen direction that you type afterwards (n, w, e or s). Remeber that you may have to walk over to the thing, before you can investigate it.',
                '"!quit" allows you to exit the game at any time.']
            await message.channel.send(reply)
        elif contents.startswith("!look"):
            look_in_room(current_room)
        elif contents.startswith("!walk"):
            direction = contents[6:]
            print(direction)
            if current_room == 0:
                current_room = move_from_room_0(direction)
            elif current_room == 1:
                current_room = move_from_room_1(direction)
            elif current_room == 2:
                    current_room = move_from_room_2(direction)
            elif current_room == 3:
                    current_room = move_from_room_3(direction)
            # else: 
            #         reply = "Sorry, which direction was it again?"
            #         await message.channel.send(reply) 

        # elif contents.startswith("!investigate"):
        #     investigate(current_room, direction)

            
       # elif:
       #     await message.channel.send("That's dosen't seem quite right. What was I doing again?")





token = get_token()
client.run(token)

