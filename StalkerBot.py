import discord

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
things = 0


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

@client.event
async def on_message(message):
    contents = message.content
    user = message.author.id 

@client.event
async def on_ready():
    print("Connected!")


current_room = 1


#Klasser & objekter
class room:
    def __init__(self,name,surroundings):
        self.name = name
        self.surroundings = surroundings
        
    def show(self):
        return self.name + "description: " + self.surroundings 

things_to_find = {
    "note1" : False
    "note2" : False
    "guts" : False
    "glass" : False
    "eyes" : False
    "pen" : False
}

investigate_things = {
    "fridge" : False
    "window" : False
    "hole" : False
    "under_bed" : False
    "door" : False
}

room_0 = room("Bathroom ", "I am in the bathroom. "
     "I can see my mirror, it's a bit dirty"
     "What is that on the wall?")
    
room_1 = room("Bedroom ", "I am in my bedroom. "
"It's rather empty, no pictures on the wall... I really wish I had something to hang"
"My bed looks comfortable.")

room_2 = room("Livingroom ", "I am in the livingroom."
"Not much living happening here..."
"There is a window to the side.")

room_3 = room("Kitchen ", "I am in the kitchen"
"Am I hungry? I may have some food in the frigde."
"There is something on the wall here aswell, weird.")

room_4 = room("Door ", "I am in front of the front door"
"This keyhole is creepy looking for some reason.")


def show_room(current_room):
    if current_room == 0:
        return room_0.show()
    elif current_room == 1: 
        return room_1.show()
    elif current_room == 2:
        return room_2.show()
    elif current_room == 3:
        return room_3.show()
    elif current_room == 4:
        return room_4.show()

def move_from_room_0(direction):
    """ Room 0 only has a single exit , which leads north to room 1. """
    if direction == "east": 
        return 1
    elif direction == "south":
        
    else:
        return 0

def move_from_room_1(direction):
    if direction == "south": 
        return 2
    elif direction == "west":  
        return 0
    else: 
        return 1
    
def move_from_room_2(direction):
    if direction == "east":
        return 3
    elif direction == "north":
        return 1
    elif direction == "south":
        return 4
    else: 
        return 2

def move_from_room_3(direction):
    if direction == "west": 
        return 2
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
def dialoge():
    if 

def investigate(current_room, dicetion):
    if current_room == 0:
        if dicetion == "south":
            if things_to_find[note1] = True:
                if investigate_things[hole] = True:
                    return "How long has that hole been there? I feel like I dont wanna know the answer to that."
                else: 
                    investigate_things[hole] = True
                    things =+ 1
                    return "There's a hole in the wall. I don't dare to look through it."
            else:
                "Just a sad wall."
        elif dicetion == "north":
            return "Nothing but my own tired reflection."
        elif direction == "east":
            return "The way to my bedroom."
        else:
            return "Just a sad empty wall."
    elif current_room == 1:
        if direction == "east":
            if investigate_things[bed] = True:
                if things_to_find[glass] = True:
                    if things_to_find[pen] = True:
                        return "I can't go back to sleep now."
                    else:
                        things_to_find[pen] = True:
                        return "There's a pen."
                else:
                    investigate_things[glass] = True
                    things =+ 1
                    "There's something under my bed. It's a glass filled with yellow liquid and a note that says 'DRINK ME :)'. I better not."
            else: 
                return "My bed is over there."
        elif direction == "west":
            return "The way to the bathroom."
        elif direction == "south":
            return "The way to the livingroom."
        else:
            "Just a sad empty wall. I should really decorate my walls."

    elif current_room == 2: 
        if direction == "north":
            return "The way to my bedroom."
        elif direction == "south":
            if investigate_things[door] = True:
                    return dialoge()
            else:
                investigate_things[door] = True
                return "I take a step closer to my door. I'm getting nervous now. Something definitely feels off. I move my head to look through the keyhole. I see nothing but darkness at first, but as I get used to the darkness, I see an eye, peeping right back at me. Frozen with fear, I can do nothing but look back."
                return dialoge()
        elif direction == "east":
            if investigate_things[window] = True:
                if things_to_find[eyes] = True:
                    return "I can still feel the intense stare"
                else:
                    things_to_find[eyes] = True
                    return "I stare blankly out the window. It's dark outside. The longer I stare, the more I feel like I can see two creepy eyes watching me. Observing my every move."
            else:
                return "I feel a slight breeze comming from that direction."
        elif direction == "west":
            return "The way to the kitchen."
        else:
            return "My living room is so empty and lifeless. Feels more like a 'dying'-room if you ask me."

    elif current_room == 3: 
        if direction == "north":
            return "Nothing but dirty dishes that have been piling up, over the course of the last couple of days."
        elif direction == "south":
            if things_to_find[note2] = True:
                return "Looking clooser, the wall is stained with the smelly goo. When did I last clean this kitchen?"
            else:
                things_to_find[note2] = True
                return "I grab the stickynote off the wall. It says 'DID YOU LIKE THE MEAL I PREPARED FOR YOU? ^_^'. The stickynote is covered in a gooey matter. The smell is indescriptible. I feel like throwing up."
                if things_to_find[guts] = True:
                    return "No. I didn't >:("

        elif direction == "east":
            if investigate_things[fridge] = True:
                if things_to_find[guts] = True:
                    return "I'm too scared to look in the fridge again."
                else:
                    things_to_find[guts] = True
                    return "I open the fridge without a second thought, only to be met by the most awful smell imaginable. The botton drawer of my fridge was practically drowning in unidentifiable matter. The only word I can think of to describe what I am seeing, is grusome."
                    return "I threw up in the trash. I feel awful."
            else:
                return "My fridge is over there."
        elif direction == "west":
            return "The way to the livingroom."
        else:
            return "This kitchen is so damn nasty. But it's home."


@client.event
async def on_message(message):
    global current_room
    contents = message.content
    user = message.author.id
    
    if contents.startswith("!look"):
      #await message.channel.send(show_room(current_room)) 
    elif contents.startswith("!help"):
      reply = ['"!look" gives a short presentation of the current room',
               '"!walk" lets you walk the direction you want (north, west, east, south)',
               '"!quit" you can only use quit if you wish to exit the game']





token = get_token()
client.run(token)

