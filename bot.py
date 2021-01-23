import os
import random
import discord
from dotenv import load_dotenv
from dao.piada import PiadaDao
from dao.trello import TrelloDao

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

piada_dao = PiadaDao()
trello_dao = TrelloDao()

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
            '!trello cards do Trello\n'
        ),
    ]

    if message.content == '!help' or message.content == '-help' or message.content == 'help!':
        response = random.choice( mensagem_help )
        await message.channel.send( response )

    mensagem_piada = piada_dao.array_piada()

    if message.content == '!piada' or message.content == '-piada' or message.content == 'piada!':
        response = random.choice( mensagem_piada )
        await message.channel.send( response )

    if message.content == '!trello' or message.content == '-trello' or message.content == 'trello!':
        response = random.choice( trello_dao.get_cards_dashboard() )
        await message.channel.send( response )

client.run(TOKEN)