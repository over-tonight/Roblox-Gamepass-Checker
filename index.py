import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents= discord.Intents.all())

TOKEN = '' # Put your discord token here.
GAMEPASS = ''

# Dont edit anything below unless you know what you're doing.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.tree.sync()

@client.tree.command()
async def check(interaction: discord.Interaction, user: str):
    req = requests.get(f"https://inventory.roblox.com/v1/users/{user}/items/1/{GAMEPASS}/is-owned")
    print(req.status_code)
    if req.status_code == 200:
        # Found gamepass message
        await interaction.response.send_message(embed=discord.Embed(title=f"Found gamepass!", description="Confirmed", color=0x00ff00))
    else:
        # Couldnt find gamepass message
        await interaction.response.send_message(embed=discord.Embed(title=f"Failed to find gamepass.", description="Did you make your inventory public?", color=0xff0000))

client.run(TOKEN)
