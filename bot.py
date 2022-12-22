# bot.py
import os
import random
 
import discord
from discord import Interaction, app_commands, Intents, Client

import giphy_client
from giphy_client.rest import ApiException
import requests

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
key = os.getenv('TENOR_KEY')

class Bot(Client):
    def __init__(self,*,intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) ->None:
        await self.tree.sync(guild=None)
bot= Bot(intents=Intents.default())

#EVENTOS DEL BOT
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
 
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
 
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
 
@bot.event
async def on_message(message):
    if message.author == client.user:
        return
 
    _99_frases_aleatorias = [
        'Bruninho',
        'https://www.youtube.com/watch?v=OxSwFP0dBJo !!!!',
        'joto al que le toque'
        'Inge al k le toque'
    ]
 
    if message.content == 'bruno mi dios':
        response = random.choice(_99_frases_aleatorias )
        await message.channel.send(response)






@bot.tree.command(name='siono')
async def brunomidios(interaction : Interaction):
    siono = [
        'joto al que le toque',
        'Inge al k le toque',
    ]
    respuesta = random.choice(siono)
    await interaction.response.send_message(respuesta)    

@bot.tree.command(name='videitosdelbruno')
async def videitos_del_bruno(interaction : Interaction):
    videos_bruno_random = [
        'https://www.youtube.com/watch?v=_LUsKymAC2w',
        'https://www.youtube.com/watch?v=OxSwFP0dBJo',
        'https://www.youtube.com/watch?v=_NKane0VC8E',
        'https://www.youtube.com/watch?v=rcGdisaO-aY',
        'https://www.youtube.com/watch?v=G2Pxb42ES9w',
    ]
    respuesta = random.choice(videos_bruno_random)
    await interaction.response.send_message(respuesta)

@bot.tree.command(name='brunodiario')
async def videitos_del_bruno(interaction : Interaction):
    brunorandom = [
        'https://media.tenor.com/sqpXC3OWsJEAAAAd/bruno-diferente.gif',
        'https://media.tenor.com/k-MCA4fbKs8AAAAC/baby.gif',
        'https://media.tenor.com/6E9tTiA6ZRkAAAAC/brunodiferente-happy.gif',
        'https://media.tenor.com/c-RyNVO70wkAAAAd/issopqnaofumaroainda-sinistroviado.gif',
        'https://media.tenor.com/6Qx6Wb1t7G0AAAAM/brunodiferente-dance.gif',
    ]
    respuesta = random.choice(brunorandom)
    await interaction.response.send_message(respuesta)

@bot.tree.command(name="buenosdias")    
async def brunogif(interaction : Interaction):

    num = random.randint(0,30)
    buscar = "buenos dias"

    result = requests.get(f"https://tenor.googleapis.com/v2/search?q={buscar}&key={key}&limit=31") 
    data = result.json()

    url = data["results"][num]["media_formats"]["gif"]["url"]

    emb = discord.Embed(title="Buenos dias",color=discord.Color.yellow())
    emb.set_image(url=url)
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name="brunogif")
async def brunogif(interaction : Interaction):

    num = random.randint(0,37)
    buscar ="Brunodiferente"

    result = requests.get(f"https://tenor.googleapis.com/v2/search?q=brunodiferente&key={key}&limit=37") 
    data = result.json()

    url = data["results"][num]["media_formats"]["gif"]["url"]

    emb = discord.Embed(title="",color=discord.Color.blue())
    emb.set_image(url=url)
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name="buenasnoches")    
async def brunogif(interaction : Interaction):

    num = random.randint(0,30)
    buscar = "buenas noches"

    result = requests.get(f"https://tenor.googleapis.com/v2/search?q={buscar}&key={key}&limit=31") 
    data = result.json()

    url = data["results"][num]["media_formats"]["gif"]["url"]

    emb = discord.Embed(title="Buenos dias",color=discord.Color.yellow())
    emb.set_image(url=url)
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name="amimir")    
async def brunogif(interaction : Interaction):

    emb = discord.Embed(title="A mimir",color=discord.Color.blurple())
    emb.set_image(url="https://media.tenor.com/q9OafBm1icIAAAAM/good-night-sleepy.gif")
    await interaction.response.send_message(embed=emb)

bot.run(TOKEN)

