
import discord
import time
import random
from discord.ext import commands
client = commands.Bot(command_prefix = ".")
orangeJuice = 20
code1 = 0
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game("some trick on you"))
  print("bot is ready")

@client.command()
async def orangejuice(ctx):
  await ctx.send("Orange Juice Loading...")
  time.sleep(2)
  global orangeJuice
  if orangeJuice >= 1:
    orangeJuice -= 1
    await ctx.send("Here is your orange juice! We have " + str(orangeJuice) + " cups of orange juice left.")
  else:
    await ctx.send("Sorry, we ran out of cups! But you can ask juicy to reload this bot to get more juice!")
  
@client.command()
async def refillcode(ctx):
  global code1
  code1 = random.randrange(10000, 99999)
  print(str(code1))
  await ctx.send("Check the Heroku Console for the refill code.")
@client.command()
async def refill(ctx, code):
  global code1
  global orangeJuice
  if int(code) == code1:
    await ctx.send("Refilled!")
    global orangeJuice
    orangeJuice = 20
    code1 = random.randrange(67037392, 92928282892)
  else:
    await ctx.send("That is not the correct refill code!")
   
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("No idea what you're saying, but I can make an orange juice for you by typing .orangejuice!")

client.run('NzcxNjYyNzY1MDAwNzUzMTUz.X5vY8w.trmRyEXSbxqz-N3rwSfDadLnSzE')
