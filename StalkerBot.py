from pdb import Restart
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


#Dictionaries and lists
state = {
    "stage": 0,
    "current_room": 1,
    "things": 0,
    "dialogue": 0
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
    "Althoug my mirror could use bit of a a wipe down.",
    "Maybe the walls too..."],
        
    "room_1" : ["*The bedroom*",
    "It's rather empty in here. No pictures on the walls or any form of decoration.",
    "Just my bed, some clothes and tash here and there, scattered arround on the room."],

    "room_2" : ["*The livingroom*", 
    "My living room is so empty and lifeless.", 
    "Feels more like a 'dying'-room if you ask me.",
    "From here on I can leave my appartmet.",
    "Whether that be by using the frontdoor up ahead, or by jumping out the window."],

    "room_3" : ["*The kitchen*",
    "My kitchen could be in better condition.",
    "Damn, looks like I left the fridge open.",
    "It hurts just thinking about my electrical bill."]
}

help = ["!look gives you a short description of the room that you are currently in. ", 
"-",  
"!walk lets you walk in either north, west, east or south from the room that you are in. ", 
"To choose direction, after typing !walk then type either n, w, e or s, and then send your message. ", 
"-", 
"!investigate lets you further investigate whatever is in your choosen direction. ", 
"Like !walk, to choose direction, type either n, w, e or s after typing the control. ", 
"Remeber that you may have to walk clooser to whatever it is you want to investigate, before you can investigate it. ", 
"-", 
"!quit allows you to exit the game at any time. ", 
"-"]



#Modules
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
            return ["Just my shower.", "Nothing noticeably weird.", "Wait...", "Now that I'm actually looking.", "Thres something stuck on the wall..."]
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
            return ["I can't leave right now.", "For multible reasons..."]
        else:
            walk_over_to.update({"frontdoor": False})
            return ["I stepped away from the frontdoor."]
    elif walk_over_to["window"] == True:
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
                return ["I think I'm gonna throw up again, if I say around this fridge much longer."]
            else:
                return ["Maybe I should gab a snack."]
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
                reply = ["What's that stain?...", "Hold up...", "Is that a stickynote?", "I grab the stickynote off the wall.", "It says 'DID YOU LIKE THE MEAL I PREPARED FOR YOU? ^_^'.", "The stickynote is covered in a gooey matter. The smell is indescriptible.", "I feel like throwing up."]
                if things_to_find["guts"] == True:
                    reply.append ("Again.")
                return (reply)
            else:
                return ["Overe theres is the wall where that creepy note was."]
        elif direction == "e":
            if things_to_find["guts"] == True:
                return ["I can't get myself to go near the fridge again.", "At least not for the time being."]
            else:
                walk_over_to.update({"fridge": True})
                return ["I walked over to the fridge."]


def dialogue_0():
    if state["dialogue"] == 0:
        return ["I take a step closer to my door.", "I'm getting nervous now.", "Something definitely feels off...", "...", 
        "I see an eye, peeping right back at me.", "Frozen with fear, I can do nothing but look right back, at the strange eye on the other side."
        "I move my head to look through the keyhole. I see nothing at first, but as I get used to the darkness...", 
        "Unknown: 'My... what a pretty being you are.'", "'Who... who are you?'", 
        "Unknown: 'How about you open the door and let me in.'", "'I'm not letting you inside my home. I don't even know you.'",
        "Unknown: 'But you do know me. If you open the door you could see me.'", "I could look at them through the peephole.",
        "What? Are they covering the peephole? I can't let an unidentified person in my home.", "'Go away. I'm going to call the police.'",
        "Unkown: 'Nonono, no need to act rash my love. I'm sorry if I'm creeping you out. It's just that we haven't seen each other in so long... I miss you.'",
        "Honestly I'm curious as to who it is.", "'Tell me your name'", "Unknown: 'You could call me babe, love, soulmate, spou-'",
        "'NAME. Give me your name.'", "Unknown: 'Well, I do prefer the petnames, but you, my love, can call me Doe'", 
        "Doe? What is this persons last name?", "Doe: 'Open the door, darling. Let me see your lovely face.'", "Should I open the door? yes or no?"]
    
    state.update({"dialogue": 1})

"""def dialogue_1(choice):
    if state["dialogue"] == 1:
        if choice == "yes":
            return ["'Fine. I'm going to open the door. Step back.'", "Doe: 'Thank you gorgeous, you won't regret it.'", "'That's weird, I can't open it.'",
            "Doe: 'It must be locked. Do you know where the key is?'", "'Yeah, let me go get it'"]
            
        if choice == "no":
            return ["'I am not opening the door to a stranger.'", "Doe: 'Baby please, don't do that. I would hate to break down the door, but I would just so I could see your beatiful smile.'",
            "'I am not opening the door to a stranger.'", "Doe: 'Pretty please? As pretty as you?'", 
            "The person behind the door sounds desperate. They don't sound threatening. What is the worst thing that can happen? Afterall I have nothing to lose.",
            "'Alright, I will open the door. Let me go find the key'"]
            
    state.update({"dialogue": 2})"""

""" def dialogue_2(choice):
    if state["dialogue"] == 1:
        print("'I got the key.'")
        input()
        print("Doe: 'Great job sweetheart, I knew you could do it'")
        input()
        print("Affirmations? How long has it been since I heard those?")
        input()
        print("Doe: 'Love? Are you alright.'")
        input()
        print("'Yes, but... I'm not... going to open the door.'")
        input()
        print("Doe: 'What? Darling, don't be stupid now.'")
        input()
        print("'I'm not letting you inside my home. I don't know you.'")
        input()
        print("Doe: 'Open the door. Now.'")
        input()
        print("'I don't want to.'")
        input()
        print("Doe: 'I said open the door. NOW.'")
        input()
        print("Where is my phone? I need to call the police!")
        input()
        print("Doe: 'Don't even think about calling the police. I will kill you before they arrive.'")
        input()
        print("Can Doe read my mind? Can you read my mind?! What do I do?")
        input()
        print("Doe: 'I'm sorry. I shouldn't have yelled at you. Can you open the door for me, sweetheart?")
        input()
        print("Should I open the door? yes or no?")
        input()
        if choice == "yes":
            print("'Promise not to do anything bad to me?'")
            input()
            print("Doe: 'Darling, I just want your heart'")
            input()
            print("'Awww. What is there to lose anyway?'")
            input()
            print("*Click turn click*")
            input()
            print("'Wow, I didn't expect you to be this tall.'")
            input()
            print("'Wait... what is that?'")
            input()
            print("'Why are you looking at me like that?'")
            input()
            print("'PLEASE. Just put the knife down.")
            input()
            print("'No. Don't come any closer'")
            input("")
            print("'AAAGH!'")
            input()
            print("Ending 1: Here lies the grave of @#!?*. They are going to be remembered by none.")
        if choice == "no":
            print("'I am not opening the door to a stranger.'")
            input()
            print("Doe: 'Are you that mentally inslaved and stupid?! Open the door, now. I can't keep forgiving you like this.'")
            input()
            print("'Forgive me? I didn't do anything wrong. You are in the wrong. You are a stalker.'")
            input()
            print("Doe: '...'")
            input()
            print("Doe: 'Take it back.'")
            input()
            print("'No'")
            input()
            print("Doe: 'TÆ K3 l t  B 4 C'")
            input()
            print("*THUD*")
            input()
            print("*THUD*")
            input()
            print("Doe: 'There you are...'")
            input()
            print("'ÆA A GH'")
            input()
            print("Ending 2: Police say that the cause of death was a fire, but no body was discovered at the scene, making that just an assumption. There were no eye witnesses and police say that the victim had no close friends and famuily to disclose and ruled it as a suicide instead.")
        state.update({"dialogue": 1}) """

def look():
    if state["current_room"] == 0:
        return room["room_0"]
    elif state["current_room"] == 1: 
        return room["room_1"]
    elif state["current_room"] == 2:
        return room["room_2"]
    elif state["current_room"] == 3:
        return room["room_3"]


def investigate_room_0(direction):
    if direction == "s":
        if things_to_find["note1"] == True:
            if investigateable["wall_with_hole"] == True:
                return ["How long has that hole been there?", "I don't think I want to know the answer to that."]
            else: 
                investigateable.update({"wall_with_hole": True})
                state["things"] += 1
                return ["There's a hole in the wall...", "Next to my shower...", "No- I'm not gonna think about it.", "This building is old...", "...", "Ofcouse there'll be some imperfections..."]
        else:
            things_to_find.update({"note1": True})
            return ["There's a note on the wall...", "It says 'YOU ALWAYS LOOK SO LOVELY DARLING <3'.", "...", "I definitely don't know anyone who would write such things about me.", "I crumple up the note and throw it in the toilet.", "What a joke..."]
    elif direction == "n":
        return ["Nothing but my own tired reflection."]
    elif direction == "e":
        return ["The way to my bedroom."]
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
                        return ["There's a pen.", "Feels kinda gross, thinking about how long it must've been there."]
            else:
                things_to_find.update({"glass": True})
                state["things"] += 1
                return ["There's something under my bed.", "It's a glass filled with yellow liquid and a note that says 'DRINK ME :)'...", "I better not."]
        else:
            return ["It's rather messy around my bed.", "Lots of trash and dirty clothes.", "It's probably a lot worse under my bed."]
    else:
        if direction == "e":
            if walk_over_to["bed"] == True:
                return ["My bed is over there."]
        elif direction == "w":
            return ["The way to the bathroom."]
        elif direction == "s":
            return ["The way to the livingroom."]
        else:
            return ["Just a sad empty wall. I should really decorate my walls."]


def investigate_room_2(direction):
    if walk_over_to["frontdoor"] == True:
        if direction == "s":
            """ if state["dialogue"] == 0:
                return dialogue_1(choice) """
        else:
            return ["I feel like I can hear breathing coming from my frontdoor."]
    elif walk_over_to["window"] == True:
        if direction == "w":
            if things_to_find["eyes"] == True:
                return ["I can still feel the intense stare."]
            else:
                things_to_find.update({"eyes": True})
                state["things"] += 1
                return ["I stare blankly out the window.", "It's dark outside.", "The longer I stare, the more I feel like I can see two creepy eyes watching me.", "Observing my every move."]
        else:
            return ["I can hear a slight tapping...", "which I am guessing is just the wind knocking a branch against my window."]
    else:
        if direction == "n":
            return ["The way to my bedroom."]
        elif direction == "s":
            if state["dialogue"] == 0:
                return ["My front door is blocking the way"]
        elif direction == "w":
            return ["My window is that way.", "It's so dark, that the window just looks like a black square from where I'm standing."]
        elif direction == "e":
            return ["The way to the kitchen."]
            


def investigate_room_3(direction):
    if walk_over_to["fridge"] == True:
        if direction == "e":
            if things_to_find["guts"] == True:
                return ["The smell of the goo and my vomit is mixing in the air."]
            else:
                things_to_find.update({"guts": True})
                state["things"] += 1
                return ["I open the fridge without a second thought, only to be met by the most awful smell imaginable.", "The botton drawer of my fridge is practically drowning in an unidentifiable matter.", "The only word I can think of to describe what I am seeing, is grusome...", "I threw up in the trash.", "I feel awful."]
        else:
            if things_to_find["guts"] == True:
                return ["The murky goo is seeping from my fridge.", "Covering the floor in the questionable fluid."]
            else:
                return ["Apperently I didn't completely close my fridgedoor.", "Weird. I'm normally so cautious about things like that."]
    else:
        if direction == "n":
            return ["Nothing but dirty dishes that have been piling up, over the course of the last couple of days."]
        elif direction == "s":
            if things_to_find["note2"] == True:
                return ["Looking clooser, the wall is stained with the smelly goo.", "When did I last clean this kitchen?"]
            else:
                return ["I think there's something stuck to the wall..."]
        elif direction == "e":
            return ["My fridge is over there."]
        elif direction == "w":
            return ["The way to the livingroom."]


#Main Gameloop
@client.event
async def on_message(message):
    global run_game
    contents = message.content
    user = message.author.id
    
    if not (message.author.bot):

        if contents.startswith("!quit"):
            await message.channel.send("Are you sure you want to quit? y/n")
            await message.channel.send(">>")
            if contents.startswith("!y"):
                await message.channel.send("Thanks for playing.")
                Restart
            elif contents.startswith("!n"):
                await message.channel.send("Good luck.")
                await message.channel.send(">>")
        elif contents.startswith("!help"):
            reply = help
            for n in reply:
                await message.channel.send(n)
            await message.channel.send(">>")

        elif state["stage"] == 0:
            if contents.startswith("!start game"):
                reply = ["*While playing, remember that all messages have to start with '!', be in lowercase and spelled correctly.*", "*Also remember, that a reply is expected when '>>' appears*", "Before starting the game, would you like to see a description of the controls? y/n"]
                for n in reply:
                    await asyncio.sleep(1)
                    await message.channel.send(n)
                await message.channel.send(">>")
                state.update({"stage": 1})

        elif state["stage"] == 1:
            if contents.startswith("!y"):
                await message.channel.send("While playing the game you will be able to use the following controls: ")
                reply = help
                for n in reply:
                    await message.channel.send(n)
                    state.update({"stage": 2})
                await message.channel.send("If you want to see the control discriptions again, then you can simply at any point in the game, type !help.")
                await message.channel.send("To start the game type !start.")
                await message.channel.send(">>")
            elif contents.startswith("!n"):
                await message.channel.send("If you want to see the control discriptions, then you can simply at any point in the game, type !help.")
                await message.channel.send("To start the game type !start.")
                await message.channel.send(">>")
                state.update({"stage": 2})
        
        elif state["stage"] == 2:
            if contents.startswith("!start"):
                reply = ["*THUD*", "I woke up in cold sweat. Now sitting on my bed, I frantically looked around the room, to see nothing but the same old bedroom in my appartmet.", "What was that?...", "And where did it come from?...", "I can't go back to sleep now.", "I'm too uneasy...", "I should probably investigate and figure out what it was that disturbed my sleep.", "I get out of my bed, almost slipping on a pice of paiper, I make may way to the center of my room.", "Where should I start?" ]
                for n in reply:
                    await asyncio.sleep(1)
                    await message.channel.send(n)
                await message.channel.send(">>")
                state.update({"stage": 3})

        elif state["stage"] == 3:
            if contents.startswith("!look"):
                reply = look()
                for n in reply:
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
                    await asyncio.sleep(1)
                await message.channel.send(">>")

            elif contents.startswith("!investigate"):
                direction = contents[13:]
                if state["current_room"] == 0:
                    reply = investigate_room_0(direction)
                elif state["current_room"] == 1:
                    reply = investigate_room_1(direction)
                elif state["current_room"] == 2:
                    reply = investigate_room_2(direction)
                    if direction == "s":
                        #choice = contents[6:]
                        if state["dialogue"] == 0:
                            reply = dialogue_0()
                            if contents.startswith("!y"):
                                reply = ["'Fine. I'm going to open the door. Step back.'", "Doe: 'Thank you gorgeous, you won't regret it.'", "'That's weird, I can't open it.'",
                                "Doe: 'It must be locked. Do you know where the key is?'", "'Yeah, let me go get it'"]
                            elif contents.startswith("!n"):
                                reply = ["'I am not opening the door to a stranger.'", "Doe: 'Baby please, don't do that. I would hate to break down the door, but I would just so I could see your beatiful smile.'",
                                "'I am not opening the door to a stranger.'", "Doe: 'Pretty please? As pretty as you?'", 
                                "The person behind the door sounds desperate. They don't sound threatening. What is the worst thing that can happen? Afterall I have nothing to lose.",
                                "'Alright, I will open the door. Let me go find the key'"]
                            
                            state.update({"dialogue": 1})
                            
                elif state["current_room"] == 3:
                    reply = investigate_room_3(direction)
                for n in reply:
                    await message.channel.send(n)
                    await asyncio.sleep(1)
                await message.channel.send(">>")


token = get_token()
client.run(token)

