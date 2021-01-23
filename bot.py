import os
import random
import discord
from dotenv import load_dotenv
from dao.piada import PiadaDao
from dao.trello import TrelloDao
from dao.discord import DiscordDao

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

piada_dao   = PiadaDao()
trello_dao  = TrelloDao()
discord_dao = DiscordDao()

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

    if message.content == '!help' or message.content == '-help' or message.content == 'help!':
        mensagem_help = '!piada - Te conto uma piada\n!trello - Cards do Trello\n'
        await message.channel.send( mensagem_help )


    if message.content == '!piada' or message.content == '-piada' or message.content == 'piada!':
        mensagem_piada = piada_dao.array_piada()
        response = random.choice( mensagem_piada )
        await message.channel.send( response )

    if message.content == '!trello' or message.content == '-trello' or message.content == 'trello!':
        texto_str = trello_dao.get_cards_dashboard()
        lista_textos = discord_dao.dividir_str_para_mensagem( texto_str )
        for mensagem in lista_textos:
            await message.channel.send( mensagem )

client.run(TOKEN)