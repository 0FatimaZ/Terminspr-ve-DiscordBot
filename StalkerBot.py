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

def reverse(s):
    return s[::-1]


@client.event
#async: man kan skrive beskeder mens computeren sender signaler (man behøver ikke at vente på at signalet til serveren er modtaget for at gøre noget andet)
async def on_message(message):
    contents = message.content
    if contents.startswith("!echo "):
        rem = contents[5:]
        my_text = rem
        reverse_text = reverse(my_text)
        reply = "Du sendte: " + rem + "!"
        reply = "Du sendte: " + reverse_text + "din besked, men baglæns"
        await message.channel.send(reply)
#await: venter på at modtage beskeder



token = get_token()
client.run(token)

