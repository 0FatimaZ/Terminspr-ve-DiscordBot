import discord
import asyncio

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


# Dictionaries 
state = {
    "stage": 0,
    "current_room": 1,
    "dialogue": 0,
    "user": None
}

things_to_find = {
    "note1" : False,
    "note2" : False,
    "guts" : False,
    "glass" : False,
    "eyes" : False,
    "pen" : False,
    "key" : False
}

walk_over_to = {
    "window" : False,
    "fridge" : False,
    "bed" : False,
    "frontdoor" : False
}

investigateable = {
    "wall_with_hole" : False,
}

room = {
    "room_0" : ["*The bathroom*",
    "Just an ordinary bathroom", 
    "Althoug my mirror could use a bit of a wipe down.",],
        
    "room_1" : ["*The bedroom*",
    "It's rather empty in here",
    "Just my bed, some clothes and a bit of trash here and there.",
    "Especially under my bed."],

    "room_2" : ["*The livingroom*", 
    "My living room is so empty and lifeless.",
    "From here on I can leave my apartment.", 
    "Either by jumping out the window or using the front door."],

    "room_3" : ["*The kitchen*",
    "My kitchen could be in better condition.",
    "Damn, looks like I left the fridge open.",]
}


# List 
help = ["!look gives you a short description of the room that you are currently in. ", 
"-",  
"!walk lets you walk either north, west, east or south from the room that you are in. ", 
"To choose direction, type either n, w, e or s after typing !walk then send your message. ", "E.g. !walk s, for walking south", 
"-", 
"!in lets you further investigate whatever is in your choosen direction. ", 
"Like !walk, to choose direction, type either n, w, e or s.", "E.g. !in w, to invesitgate in the western direction", 
"-", 
"!quit allows you to exit the game at any time.",
"But just remember that all progress will be lost.", 
"-"]


# Dialogues
def dialogue_0():
    if state["dialogue"] == 0:
        return ["I take a step closer to my door.", "Something definitely feels...", "off...", 
        "I move my head to look through the keyhole. I see nothing at first, but as I get used to the darkness...", 
        "I see an eye, peeping right back at me.", "Frozen with fear, I can do nothing but look right back, at the strange eye on the other side.",
        "Unknown: 'My... what a pretty being you are.'", "'Who... who are you?'", 
        "Unknown: 'How about you open the door and let me in.'", "'I'm not letting you inside my home. I don't even know you.'",
        "Unknown: 'But you do know me. If you open the door you could see me.'", "'Go away. I'm going to call the police.'",
        "Unkown: 'Nonono, no need to act rash my love. I'm sorry if I'm creeping you out. It's just that we haven't seen each other in so long... I miss you.'",
        "Honestly I'm curious as to who it is.", "'Tell me your name'", "Unknown: 'You could call me babe, love, soulmate, spou-'",
        "'NAME. Give me your name.'", "Unknown: 'Well, I do prefer the petnames, but you, my love, can call me Doe'", 
        "Doe? What is this persons last name?", "Doe: 'Open the door, darling. Let me see your lovely face.'",
        "'I am not opening the door to a stranger.'", "Doe: 'Baby please, don't do that. I would hate to break down the door, but I would, just so I could see your beautiful smile.'",
        "'I am not opening the door to a stranger.'", "Doe: 'Pretty please? As pretty as you?'", 
        "The person behind the door sounds desperate. They don't sound threatening. What is the worst thing that can happen? Afterall I have nothing to lose.",
        "'Alright, I will open the door. Let me go find the key'"]
        

def dialogue_1():
    if state["dialogue"] == 1 and things_to_find["key"] == True:
        return ["'I got the key.'", "Doe: 'Great job sweetheart, I knew you could do it'", "Affirmations? How long has it been since I heard those?", 
        "Doe: 'Love? Are you alright.'", "'Yes, but... I'm not... going to open the door.'", "Doe: 'What? Darling, don't be stupid now.'", 
        "'I'm not letting you inside my home. I don't know you.'", "Doe: 'Open the door. Now.'", "'I don't want to.'", "Doe: 'I said open the door. NOW.'",
        "Where is my phone? I need to call the police!", "Doe: 'Don't even think about calling the police. I will kill you before they arrive.'", 
        "Can Doe read my mind? Can you read my mind?! What do I do?", "Doe: 'I'm sorry. I shouldn't have yelled at you. Can you open the door for me, sweetheart?", 
        "Should I open the door? y/n?"]

def dialogue_2(choice):   
    if choice == "y" and "yes":
        return ["'Promise not to do anything bad to me?'", "Doe: 'Darling, I just want your heart'", "'Awww. What is there to lose anyway?'", 
        "*Click turn click*", "'Wow, I didn't expect you to be this tall.'", "'Wait... what is that?'", "'Why are you looking at me like that?'",
        "*THUD*", "'Ehhh, where am I?'", "Doe: 'Oh, you're awake? You're home.'", "'This isn't my home.'", "Doe: 'It is now. I couldn't let the love of my life live in that awful place.'",
        "'Let me go, please?'", "Doe: 'Now why would I ever want to do that? We are going to live happily ever after.'", "Ending 1: Doe loved you too much.", "Thanks for playing."]
        
    elif choice == "n" and "no":
        return ["'I am not opening the door to a stranger.'", "Doe: 'Are you that mentally inslaved and stupid?! Open the door, now. I can't keep forgiving you like this.'", 
        "'Forgive me? I didn't do anything wrong. You are in the wrong. You are a stalker.'", "Doe: '...'", "Doe: 'Take it back.'", "'No'", "Doe: 'TÆ K3 l t  B 4 C'", "*THUD*",
        "*THUD*", "Doe: 'There you are...'", "'ÆA A GH'", 
        "Ending 2: Police say that the cause of death was a fire, but no body was discovered at the scene, making that just an assumption. There were no eye witnesses and police say that the victim had no close friends and family to disclose and ruled it as a suicide instead.",
        "Thanks for playing."]
    
    elif choice == "pen" and things_to_find["pen"] == True:
        return ["My pen!", "'Fine... I'll open the door.'", "Doe: 'There it is. I just love your logical thinking.'", "I don't think you'll like it in a second", "Where is my pen?", 
        "Ah, there it is.", "Doe: 'Darling, you are taking an awfully long time. I am so eager to see you.'", "'Take this you piece of shit'", 
        "Doe: 'AAAGHHH, YOU LITTLE... DO YOU HAVE ANY IDEA WHAT YOU HAVE DONE?! CALL AN AMBULANCE. NOW!'", "'No, I won't.'", 
        "Doe: 'What kind of psycho stabs someone in the eye through a keyhole?!'", "Doe: 'You know what? You're ugly anyway. Why did I ever waste a second on you, you are going to die alone.'",
        "Honestly I'd rather die than be with that stalker!", "'Bye Doe'", "Doe: 'This isn't over. I'm getting my revenge someday.'", "Ending 3: Safe again.", "Thanks for playing."]
    else:
        return ["Do I want to open the door?"]  


# Look module
def look():
    if state["current_room"] == 0:
        return room["room_0"]
    elif state["current_room"] == 1: 
        return room["room_1"]
    elif state["current_room"] == 2:
        return room["room_2"]
    elif state["current_room"] == 3:
        return room["room_3"]


# Movement modules
def move_from_room_0(direction):
    if direction == "e": 
        state.update({"current_room": 1})
        return ["I went into my bedroom."]
    elif direction == "s":
        if things_to_find["note1"] == True:
            if investigateable["wall_with_hole"] == True:
                return ["I have to remember to cover up that hole..."]
            else:
                return ["Wait...", "There was something behind the note..."]
        else:
            return ["Just my shower.", "Nothing noticeably weird.", "Wait...", "Theres something stuck on the wall..."]
    elif direction == "n":
        return ["Just my dirty mirror that way."]
    elif direction == "w":
        return ["Just the toilet that way."]


def move_from_room_1(direction):
    if walk_over_to["bed"] == True:
        if direction == "e":
            return ["I wish I could just go back to sleep."]
        else:
            walk_over_to.update({"bed": False})
            return ["I can't sleep now.", "I stepped away from the bed."]
    else:
        if direction == "s": 
            state.update({"current_room": 2})
            return ["I went into the livingroom."]
        elif direction == "w":  
            state.update({"current_room": 0})
            return ["I went into the bathroom."]
        elif direction == "e":
            walk_over_to.update({"bed": True})
            return ["I went over to my bed."]
        elif direction == "n":
            return ["Just my sad and empty wall."]

    
def move_from_room_2(direction):
    if walk_over_to["frontdoor"] == True:
        if direction == "s":
            return ["I can't leave right now.", "For multiple reasons..."]
        else:
            walk_over_to.update({"frontdoor": False})
            return ["I stepped away from the frontdoor."]
    if walk_over_to["window"] == True:
        if direction == "w":
            return ["I shouldn't jump out the window.", "No matter how much I want to."]
        else:
            walk_over_to.update({"window": False})
            return ["I don't have all night to just stare out the window.", "I stepped away from the window."]
    else:
        if direction == "e":
            state.update({"current_room": 3})
            return ["I went into the kitchen."]
        elif direction == "n":
            state.update({"current_room": 1})
            return ["I went into my bedroom."]
        elif direction == "s":
            walk_over_to.update({"frontdoor": True})
            return ["I went over to my frontdoor."]
        elif direction == "w":
            walk_over_to.update({"window": True})
            return ["I went over to my window."]
    
            
def move_from_room_3(direction):
    if walk_over_to["fridge"] == True:
        if direction == "e":
            if things_to_find["guts"] == True:
                return ["I think I'm gonna throw up again, if I stay around this fridge much longer."]
            else:
                return ["Maybe I should grab a snack."]
        else:
            walk_over_to.update({"fridge": False})
            if things_to_find["guts"] == True:
                return ["I need to get away from this fridge. Right now.", "I step away from the fridge."]
            else:
                return ["Now isn't the time for a late-night-snack."]
    else:
        if direction == "w": 
            state.update({"current_room": 2})
            return ["I went into the livingroom."]
        elif direction == "s":
            if things_to_find["note2"] == False:
                things_to_find.update({"note2": True})
                reply = ["What's that stain?...", "Is that a stickynote?", "I grab the stickynote off the wall.", "It says 'DID YOU LIKE THE MEAL I PREPARED FOR YOU? ^_^'.", "The stickynote is covered in a gooey matter. The smell is indescriptible.", "I feel like throwing up."]
                if things_to_find["guts"] == True:
                    reply.append ("Again.")
                return (reply)
            else:
                return ["That's the wall where that creepy note was."]
        elif direction == "e":
            if things_to_find["guts"] == True:
                return ["I can't get myself to go near the fridge again.", "At least not for the time being."]
            else:
                walk_over_to.update({"fridge": True})
                return ["I walked over to the fridge."]
        else: 
            return ["That's where I make the food I eat everyday."]
    

# Investigate modules
def investigate_room_0(direction):
    if direction == "s":
        if things_to_find["note1"] == True:
            if investigateable["wall_with_hole"] == True:
                return ["How long has that hole been there?"]
            else: 
                investigateable.update({"wall_with_hole": True})
                return ["There's a hole in the wall...", "Next to my shower...", "...", "This building is old...", "Of course there'll be some imperfections...", "Right...?" ]
        else:
            things_to_find.update({"note1": True})
            return ["There's a note on the wall...", "It says 'YOU ALWAYS LOOK SO LOVELY DARLING <3'.", "...", "I definitely don't know anyone who would write such things about me.", "I crumple up the note and throw it in the toilet.", "How creepy."]
    elif direction == "n":
        return ["Nothing but my own tired reflection and a note that says 'Remember to take your remember pills'.", "What pills.", "I don't rememb-", "Nevermind."]
    elif direction == "e":
        return ["The way to my bedroom."]
    elif direction == "w":
        if state["dialogue"] == 1:
            if things_to_find["key"] == False:
                things_to_find.update({"key": True})
                return ["...", "What the-", "Is that my key?", "Urhg... I must have dropped it down there.", "I pick up the key, and wash it and my hands in the sink.", "Anyway, I've got the key now."]
        else:
            return ["Just my toilet."]
    else:
        return ["Theres nothing special or noticable in that direction."]

def investigate_room_1(direction):
    if walk_over_to["bed"] == True:
        if direction == "e":
            if things_to_find["glass"] == True:
                    if things_to_find["pen"] == True:
                        return ["I can't sleep.", "Not right now.", "Something's...", "Not right..."]
                    else:
                        things_to_find.update({"pen": True})
                        return ["There's a pen here as well.", "It's covered in lint and feels kinda gross.", "Oh well-", "I put the pen in my pocket.", "Maybe it'll be of use later."]
            else:
                things_to_find.update({"glass": True})
                return ["There's something under my bed.", "It's a glass filled with warm yellow liquid and a note that says 'DRINK ME :)'...", "I better not."]
        else:
            return ["It's rather messy around my bed.", "It's probably a lot worse under my bed."]
    else:
        if direction == "e":
            return ["My bed is over there."]
        elif direction == "w":
            return ["The way to the bathroom."]
        elif direction == "s":
            return ["The way to the livingroom."]
        else:
            return ["Just a sad empty wall. I should really decorate my walls."]


def investigate_room_2(direction):
    if walk_over_to["window"] == True:
        if direction == "w":
            if things_to_find["eyes"] == True:
                return ["I can still feel the intense stare."]
            else:
                things_to_find.update({"eyes": True})
                return ["I stare blankly out the window.", "It's dark outside.", "The longer I stare, the more I feel like I can see two creepy eyes watching me."]
        else:
            return ["I can hear a slight tapping...", "which I am guessing is just a branch knocking against my window."]
    if walk_over_to["frontdoor"] == True:
        return ["I can hear a faint breathing comming form behind the door."]
    else:
        if direction == "n":
            return ["The way to my bedroom."]
        elif direction == "w":
            return ["My window is that way.", "It's so dark, that the window just looks like a black square from where I'm standing."]
        elif direction == "e":
            return ["The way to the kitchen."]
        elif direction == "s":
            return ["That's the way to the frontdoor."]


def investigate_room_3(direction):
    if walk_over_to["fridge"] == True:
        if direction == "e":
            if things_to_find["guts"] == True:
                return ["The smell of the goo and my vomit is mixing in the air."]
            else:
                things_to_find.update({"guts": True})
                return ["I open the fridge without a second thought, only to be met by the most awful smell imaginable.", "The botton drawer of my fridge is practically drowning in an unidentifiable matter.", "The only word I can think of to describe what I am seeing, is gruesome...", "I threw up in the trash."]
        else:
            if things_to_find["guts"] == True:
                return ["The murky goo is seeping from my fridge.", "Covering the floor in the questionable fluid."]
            else:
                return ["Apperently I didn't completely close my fridgedoor.", "Weird. I'm normally so cautious about things like that."]
    else:
        if direction == "n":
            return ["Nothing but dirty dishes that have been piling up."]
        elif direction == "s":
            if things_to_find["note2"] == True:
                return ["Looking closer, the wall is stained with the smelly goo.", "When did I last clean this kitchen?"]
            else:
                return ["I think there's something stuck to the wall..."]
        elif direction == "e":
            return ["My fridge is over there."]
        elif direction == "w":
            return ["The way to the livingroom."]

# Quit module
def quit():
    state.update({"stage": 0})
    state.update({"current_room": 1})
    state.update({"dialogue": 0})
    state.update({"user": None})
    things_to_find.update({"note1" : False})
    things_to_find.update({"note2" : False})
    things_to_find.update({"guts" : False})
    things_to_find.update({"glass" : False})
    things_to_find.update({"eyes" : False})
    things_to_find.update({"pen" : False})
    things_to_find.update({"key" : False})
    walk_over_to.update({"window" : False})
    walk_over_to.update({"fridge" : False})
    walk_over_to.update({"bed" : False})
    walk_over_to.update({"frontdoor" : False})
    investigateable.update({"wall_with_hole" : False})
    return "Thanks for playing."



#Main Gameloop
@client.event
async def on_message(message):
    global run_game
    contents = message.content
    
    if not (message.author.bot):

        if contents.startswith("!quit"):
            await message.channel.send(quit())

        elif contents.startswith("!help"):
            reply = help
            for n in reply:
                await message.channel.send(n)
            await message.channel.send("Here's a map of your location", file=discord.File('mapp.PNG'))
            await message.channel.send("-")
            if state["current_room"] == 0:
                await message.channel.send("You are currently in the bathroom.")
            elif state["current_room"] == 1:
                await message.channel.send("You are currently in the bedroom.")
            elif state["current_room"] == 2:
                await message.channel.send("You are currently in the livingroom.")
            elif state["current_room"] == 3:
                await message.channel.send("You are currently in the kitchen.")
            else:
                await message.channel.send("I currently can't tell you where you are try to !look.")
            await message.channel.send(">>")

        elif state["stage"] == 0:
            if contents.startswith("!start game"):
                state["user"] = message.author.id
                reply = ["*While playing, remember that all messages have to start with '!', be in lowercase and spelled correctly.*", "*Also remember, that a reply is expected when '>>' appears*"]
                for n in reply:
                    await message.channel.send(n)
                    await asyncio.sleep(2)
                await message.channel.send("*Here's a map of your location*", file=discord.File('mapp.PNG'))
                await asyncio.sleep(2)
                await message.channel.send("-")
                await message.channel.send("Before starting the game, would you like to see a description of the controls? y/n")
                await message.channel.send(">>")
                state.update({"stage": 1})

        elif state["user"] == message.author.id and state["stage"] == 1:
            if contents.startswith("!y" or "!yes"):
                await message.channel.send("While playing the game you will be able to use the following controls: ")
                reply = help
                for n in reply:
                    await message.channel.send(n)
                    state.update({"stage": 2})
                await message.channel.send("If you want to see the control descriptions or the map again, then you can simply at any point in the game, type !help.")
                await message.channel.send("To start the game type !start")
                await message.channel.send(">>")
            elif contents.startswith("!n" or "!no"):
                await message.channel.send("If you want to see the control descriptions, then you can simply at any point in the game, type !help.")
                await message.channel.send("To start the game type !start.")
                await message.channel.send(">>")
                state.update({"stage": 2})
        
        elif state["user"] == message.author.id and state["stage"] == 2:
            if contents.startswith("!start"):
                reply = ["*THUD*", "I woke up in cold sweat. Now sitting on my bed, I frantically looked around the room, to see nothing but the same old bedroom in my appartmet.", "What was that?...", "And where did it come from?...", "I can't go back to sleep now.", "I'm too uneasy...", "I should probably investigate and figure out what it was that disturbed my sleep.", "I get out of my bed, almost slipping on a piece of paper, I make may way to the center of my room.", "Where should I start?" ]
                for n in reply:
                    await asyncio.sleep(2)
                    await message.channel.send(n)
                await message.channel.send(">>")
                state.update({"stage": 3})

        elif state["user"] == message.author.id and state["stage"] == 3:
            if contents.startswith("!look"):
                reply = look()
                for n in reply:
                    await message.channel.send(n)
                if state["current_room"] == 2:
                    if state["dialogue"] == 1:
                        reply = ["I can't leave with Doe at my front door tho", "Maybe I should... just jump out the window."]
                        for n in reply:
                            await asyncio.sleep(2)
                            await message.channel.send(n)
                await message.channel.send(">>")

            elif contents.startswith("!walk"):
                direction = contents[6:]
                if state["current_room"] == 0:
                    reply = move_from_room_0(direction)
                elif state["current_room"] == 1:
                    reply = move_from_room_1(direction)
                elif state["current_room"] == 2:
                    reply = move_from_room_2(direction)
                elif state["current_room"] == 3:
                    reply = move_from_room_3(direction)
                for n in reply:
                    await message.channel.send(n)
                    await asyncio.sleep(2)
                await message.channel.send(">>")

            elif contents.startswith("!in"):
                direction = contents[4:]
                if state["current_room"] == 0:
                    reply = investigate_room_0(direction)
                elif state["current_room"] == 1:
                    reply = investigate_room_1(direction)
                elif state["current_room"] == 2:
                    reply = investigate_room_2(direction)
                    if walk_over_to["frontdoor"] == True:
                        if direction == "s":
                            if state["dialogue"] == 0:
                                reply = dialogue_0()
                                state.update({"dialogue": 1})
                            elif state["dialogue"] == 1 and things_to_find["key"] == True:
                                reply = dialogue_1()
                                state.update({"stage": 4})
                elif state["current_room"] == 3:
                    reply = investigate_room_3(direction)
                for n in reply:
                    await message.channel.send(n)
                    await asyncio.sleep(2)
                await message.channel.send(">>")
        
        elif state["user"] == message.author.id and state["stage"] == 4:
            if contents.startswith("!"):
                choice = contents[1:]
                reply = dialogue_2(choice)
            for n in reply:
                    await message.channel.send(n)
                    await asyncio.sleep(2)
            await message.channel.send(quit())


token = get_token()
client.run(token)

