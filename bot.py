import os
from twitchio.ext import commands

bot = commands.Bot(irc_token=os.environ['TMI_TOKEN'],client_id=os.environ['CLIENT_ID'],nick=os.environ['BOT_NICK'],prefix= os.environ['BOT_PREFIX'],
initial_channels=[os.environ['CHANNEL']])

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")

    ws = bot._ws
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has arrived and ready to give some love!")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat'

    #make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return 
    
    await bot.handle_commands(ctx)

    #if 'hello' in ctx.content.lower():
        #await ctx.channel.send(f"Hi, @{ctx.author.name}!")

    
    #await ctx.channel.send(ctx.content)

@bot.command(name='givehug')
async def hug(ctx):
    if "givehug" in ctx.content():
        await ctx.send(f'GivePLZ @{ctx.author.name} You are loved!')

@bot.command(name='headpat')
async def headpat(ctx):
    if "headpat" in ctx.content:
        await ctx.send(f'FBBlock Pat, pat,@{ctx.author.name} it will be ok fren')  

@bot.command(name='snuggle')
async def snuggle(ctx):
    await ctx.send(f'GivePLZ TakeNRG I love snuggles @{ctx.author.name}')   







if __name__ == "__main__":
    bot.run()