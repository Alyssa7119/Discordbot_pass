import discord
from bot_logic import generate_pass
from bot_logic import gen_emoji
from bot_logic import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Hello'):
        await message.channel.send("$Hi")
    elif message.content.startswith('$Bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('como estas?'):
        await message.channel.send("bien") 
    elif message.content.startswith('pass'):
        await message.channel.send(generate_pass(10)) 
    elif message.content.startswith('carita'):
        await message.channel.send(gen_emoji())    
    elif message.content.startswith('coin'):
        await message.channel.send(flip_coin())          
    
    else:
        await message.channel.send(message.content)

client.run(TOKEN)
