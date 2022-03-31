import discord
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

token = os.getenv("token")
client = discord.Client()

@client.event
async def on_ready():
    print("Ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("getsupl"):
        bgv = BeautifulSoup(requests.get("https://bgv.cz/suplovani.html").text, "html.parser")
        lastSupl = bgv.find_all(class_="photo-supl")[-1].contents[0]["src"]
        await message.channel.send(f"<@&829977373339418665>\nhttps://bgv.cz/{lastSupl}")

client.run(token)