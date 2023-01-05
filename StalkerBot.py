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

# #KODe -----------

current_room = 1


class room:
    def __init__(self,name,surroundings):
        self.name = name
        self.surroundings = surroundings
        

    def show(self):
        return self.name + "description: " + self.surroundings 

#Klasser & objekter

room_0 = room("Bathroom ", "You are in the bathroom "
    'If you need help type "!help" ')
    
room_1 = room("Bedroom ", "You are in the bedroom ")

room_2 = room("Livingroom ", "You are in the livingroom")

room_3 = room("Kitchen ", "You are in the Kitchen")

room_4 = room("Door ", "You are in front of front door")


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
    
    elif current_room == 1:

    elif current_room == 2: 

    elif current_room == 3: 

    elif current_room == 4: 

#investigate funktion her

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

# def show_room(room_num):
#     """Display the contents of the given room.
#     Input:
#     - room_num : int, the number of the room to show.
#     """
#     if room_num == 0:
#         return room_0.show()
#     elif room_num == 1: 
#         return room_1.show()
#     elif room_num == 2:
#         return room_2.show()
#     elif room_num == 3:
#         return room_3.show()
#     else:
#         reply = "You are out of bounds. Room", room_num, "does not exist."
#         return reply




token = get_token()
client.run(token)

