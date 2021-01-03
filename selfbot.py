import discord
import asyncio
from discord.ext import commands

token = 'mfa.Y_M976UEhgTyM75kaRYRfI7NdE-CVxaM2zFgzyVrWpRJffAF34mXMLdBtaFzupJQwqry4en1IdDprh2Ls2pr'

prefix = '!'
client = discord.Client()
client = commands.Bot(
    description='Dropout',
    command_prefix=prefix,
    self_bot=True
)
client.remove_command('help') 

@client.event
async def on_ready():
    print('Online')
   

@client.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await user.send(message)
            print(f"Sent To {user}")
        except:
            pass

    
client.run(token, bot = False)
