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

@client.event
async def on_message(message):
    contents = message.content
    user = message.author.id 

@client.event
async def on_ready():
    print("Connected!")


current_room = 1


class room:
    def __init__(self,name,surroundings):
        self.name = name
        self.surroundings = surroundings
        

    def show(self):
        return self.name + "description: " + self.surroundings 


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

def move_from_room_4(direction):
    if direction == "north":
        return 2

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

#investigate funktion her
# def investigate(current_room, dicetion):
#     if current_room == 0:

#     elif current_room == 1:

#     elif current_room == 2: 

#     elif current_room == 3: 

#     elif current_room == 4:

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

