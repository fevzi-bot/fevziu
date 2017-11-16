import discord
import asyncio


client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if'fevz'in message.content.lower():
        if'mendon'in message.content:
            if'light'in message.content.lower():
                await client.send_message(message.channel,'Light eshte shpirt njeriu')
            elif'pasanik'in message.content.lower():
                await client.send_message(message.channel,'Asgje')
            elif'batsy'in message.content.lower():
                await client.send_message(message.channel,'Batsy eshte malok')
            elif'dhor'in message.content.lower():
                await client.send_message(message.channel,'Kush eshte dhori ?')
            elif'gpu'in message.content.lower():
                await client.send_message(message.channel,'GPU ka instagram me cool ne Ballkan')
            elif'plasm'in message.content.lower():
                await client.send_message(message.channel,'Plasmo eshte kawaii')
            elif'zhani'in message.content.lower():
                await client.send_message(message.channel,'Zhani eshte master weeb')
            elif'wub'in message.content.lower():
                await client.send_message(message.channel,'Wubban e kam frike')
            elif'lame'in message.content.lower():
                await client.send_message(message.channel,'Lamen e kam koleg')
            elif'kolonel'in message.content.lower():
                await client.send_message(message.channel,'Koloneli eshte master troll')
            elif'yeez'in message.content.lower():
                await client.send_message(message.channel,'Yeezi duhet tja leri gpu-se')
            elif'nori'in message.content.lower():
                await client.send_message(message.channel,'Nori ka problem me alkolin,duhet te shkoj te alkoliket anonim')
            elif'shpen'in message.content.lower():
                await client.send_message(message.channel,'iii vlonjat')


client.run('email','password')
