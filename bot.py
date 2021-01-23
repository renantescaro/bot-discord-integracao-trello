import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} conectado ao Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá {member.name}, bem vindo ao meu servidor no Discord!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mensagem_help = [
        (
            '!piada eu te conto uma piada\n'
            '!teste não faz nada\n'
            '!sla não faz nada tbm'
        ),
    ]

    if message.content == '!help' or message.content == '-help' or message.content == 'help!':
        response = random.choice(mensagem_help)
        await message.channel.send(response)

client.run(TOKEN)