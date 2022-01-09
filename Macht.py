import time
import os
import colorama
import psutil
import json
import requests
import math
import itertools
import random
import nekos
from threading import Thread
import threading
import discord
from datetime import *
import time
from colorama import Fore, Style
from pystyle import Colors, Colorate, Center, Box #pip3 install pystyle - comes with folder
from discord.ext import commands
from discord.ext.commands import CommandNotFound

colorama.init()

with open("config.json") as f:
    config = json.load(f)
    prefix = config["prefix"]
    clientId = config["userid"]

lastTime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
startTime = time.time()
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')
resetClr = Style.RESET_ALL
clearConsole = lambda: os.system('cls')
hexColor = 0x843BAC
commandLog = f'{Fore.YELLOW}|Command| {resetClr}{prefix}'


#│
#―
#guild.member_count()
#guild.name
#guild.owner
os.system("title Connecting to token")
print(f"{Fore.BLACK}=―――――――――――――――――――――――――――――――――――――――={resetClr}")
print(f'        {Fore.LIGHTMAGENTA_EX}    Macht Selfbot{resetClr}')
print(f'        {Fore.LIGHTMAGENTA_EX}Status:  {Fore.RED}Connecting...{resetClr}')
print(f"{Fore.BLACK}=―――――――――――――――――――――――――――――――――――――――={resetClr}")

def userConnected():
    print(f"{Fore.BLACK}=――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――={resetClr}")
    print(f"{Fore.MAGENTA}╔═╗╔═╗     ╔╗─╔╗")
    print("║║╚╝║║     ║║╔╝╚╗")
    print("║╔╗╔╗╠══╦══╣╚╩╗╔╝")
    print("║║║║║║╔╗║╔═╣╔╗║║")
    print("║║║║║║╔╗║╚═╣║║║╚╗")
    print("╚╝╚╝╚╩╝╚╩══╩╝╚╩═╝")
    #print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, "Macht Selfbot.", 1)))
    print(f'{Fore.LIGHTMAGENTA_EX}Status:  {Fore.GREEN}Connected!{resetClr}')
    print(f'{Fore.LIGHTMAGENTA_EX}Account: {bot.user.name} [Last Login: {lastTime}] [ID: {bot.user.id}]{resetClr}')
    print(f'{Fore.LIGHTMAGENTA_EX}Prefix:  {Fore.LIGHTCYAN_EX}{prefix}{resetClr}')
    print(f"{Fore.BLACK}=――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――={resetClr}")


def getUptime():
  return time.time() - startTime

def updateTitle():
    for _ in itertools.repeat(None):
     os.system("title Macht V1.0 │ "+ str(math.floor(getUptime())) +" sec") #Removing math.floor decreases memory usage
     pass
     time.sleep(0.5)


def clear():
    clearConsole()
    userConnected()

@bot.event
async def on_ready():
    clear()
    t = threading.Timer(0.5, updateTitle)
    t.start()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if (message.author.id != clientId):
        return
    if message.author == bot.user:
        return

@bot.command()
async def test(ctx):
    await ctx.message.delete()
    print(f'{commandLog}test')
    await ctx.send("Macht Test")
    try:
        with requests.session() as ses:
            resp = ses.get(f'https://nekos.life/api/neko')
            try:
                j = resp.json()
                embed= discord.Embed(colour=hexColor, title=f"Neko",description="Random neko by nekos.life")
                embed.set_image(url=j["neko"])
                embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(j["neko"])
    except Exception as e:
        await ctx.send(f"Error: {e}")


#-----Help Commands-----
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    print(f'{commandLog}help')
    embed = discord.Embed(colour=hexColor, title="Macht", description="<> = required, [] = optional")
    #embed.add_field(name="Tip:", value="<> = required, [] = optional", inline=False)
    embed.add_field(name=f"`{prefix}help`", value=f"*Displays commands*", inline=False)
    embed.add_field(name=f"`{prefix}fun`", value=f"*Displays fun commands*", inline=False)
    embed.add_field(name=f"`{prefix}misc`", value=f"*Displays miscellaneous commands*", inline=False)
    embed.add_field(name=f"`{prefix}tools`", value=f"*Displays tool commands*", inline=False)
    embed.add_field(name=f"`{prefix}nsfw`", value=f"*Displays NSFW commands*", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?") 

@bot.command()
async def fun(ctx):
    await ctx.message.delete()
    print(f'{commandLog}fun')
    embed = discord.Embed(colour=hexColor, title="Fun Commands")
    embed.add_field(name=f"`{prefix}yoight`", value=f"*Sends yoights*", inline=False)
    embed.add_field(name=f"`{prefix}ara`", value=f"*Sends ara ara in chat*", inline=False)
    embed.add_field(name=f"`{prefix}gay <user>`", value=f"*Gay rating of mentioned user*", inline=False)
    embed.add_field(name=f"`{prefix}cat`", value=f"*Random cat image*", inline=False)
    embed.add_field(name=f"`{prefix}neko`", value=f"*Random neko image*", inline=False)
    embed.add_field(name=f"`{prefix}foxgirl`", value=f"*Random foxgirl image*", inline=False)
    embed.add_field(name=f"`{prefix}pat <user>`", value=f"*Pat mentioned user*", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def misc(ctx):
    await ctx.message.delete()
    print(f'{commandLog}misc')
    embed = discord.Embed(colour=hexColor, title="Miscellaneous Commands")
    embed.add_field(name=f"`{prefix}embed <titletext> <fieldtext>`", value=f"*Sends your message as an embed,* ***add quotes around fieldtext***", inline=False)
    embed.add_field(name=f"`{prefix}cls`", value=f"*Clears the console window*", inline=False)
    embed.add_field(name=f"`{prefix}test`", value=f"*Test command*", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def tools(ctx):
    await ctx.message.delete()
    print(f'{commandLog}tools')
    embed = discord.Embed(colour=hexColor, title="Tools")
    embed.add_field(name=f"`{prefix}iplookup <ip>`", value=f"*Displays info on ip*", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def nsfw(ctx):
    await ctx.message.delete()
    print(f'{commandLog}nsfw')
    embed = discord.Embed(colour=hexColor, title="NSFW")
    embed.add_field(name=f"`{prefix}nsfw_neko`", value=f"*Random NSFW neko gif*", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")





#-----Fun Commands-----
@bot.command()
async def yoight(ctx):
    await ctx.message.delete()
    print(f'{commandLog}yoight')
    await ctx.send("Yoight yoight yoight yoight")

@bot.command()
async def ara(ctx):
    await ctx.message.delete()
    print(f'{commandLog}ara')
    await ctx.send("ara ara~")

@bot.command()
async def gay(ctx, mentionedUser: str=None):
  await ctx.message.delete()
  #-----Error-----
  embedError = discord.Embed(colour=hexColor, title="Error", description=f"No user has been mentioned")
  embedError.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
  embedError.set_footer(text=" Macht Selfbot - Made by Founder#8300")
  #-----Error-----
  print(f'{commandLog}gay')
  if mentionedUser is None:
    try:
     await ctx.send(embed=embedError);return
    except discord.HTTPException:
     await ctx.send("An error has occured, are embeds allowed here?");return
  else: pass
  gayPercentage = random.randint(0, 100)
  if mentionedUser == bot.user.name:
    gayPercentage = 0
  embed = discord.Embed(colour=hexColor, title="Gay Meter", description=f"**{mentionedUser}** is **{gayPercentage}% gay**")
  embed.set_thumbnail(url="https://i.dlpng.com/static/png/1210414-rainbow-flag-png-transparent-image-png-images-rainbow-flag-png-400_400_preview.png?width=341&height=341")
  embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
  try:
    await ctx.send(embed=embed)
  except discord.HTTPException:
    await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    print(f'{commandLog}cat')
    embed = discord.Embed(colour=hexColor, title="Cat",description="A random cat image by nekos.life lib")
    embed.set_image(url=nekos.cat())
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def gato(ctx):
    await ctx.message.delete()
    print(f'{commandLog}gato')
    embed = discord.Embed(colour=hexColor, title="Gato",description="A random gato (cat) image by nekos.life lib")
    embed.set_image(url=nekos.cat())
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def neko(ctx):
    await ctx.message.delete()
    print(f'{commandLog}neko')
    try:
        with requests.session() as ses:
            resp = ses.get(f'https://nekos.life/api/neko')
            try:
                j = resp.json()
                embed= discord.Embed(colour=hexColor, title=f"Neko",description="Random neko by nekos.life")
                embed.set_image(url=j["neko"])
                embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
                embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(j["neko"])
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command()
async def foxgirl(ctx):
    await ctx.message.delete()
    print(f'{commandLog}foxgirl')
    embed = discord.Embed(colour=hexColor, title="Fox Girl",description="A random foxgirl image by nekos.life lib")
    embed.set_image(url=nekos.img("fox_girl"))
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def pat(ctx, user: str=None):
    await ctx.message.delete()
    print(f'{commandLog}pat')
    #-----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error",description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    #-----End-----
    if user is None:
      await ctx.send(embed=embedNoMen)
      return
    else:
     embed = discord.Embed(colour=hexColor, title="Pat",description=f"***{bot.user.name}*** *pats* ***{user}***")
     embed.set_image(url=nekos.img("pat"))
     embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
     embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
     try:
       await ctx.send(embed=embed)
     except discord.HTTPException:
       await ctx.send("An error has occured, are embeds allowed here?")






#-----Misc Commands-----
@bot.command()
async def embed(ctx, titleText, fieldText):
    await ctx.message.delete()
    print(f'{commandLog}embed')
    embed = discord.Embed(colour=hexColor, title=" ")
    embed.add_field(name=titleText, value=fieldText, inline=False)
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")

@bot.command()
async def cls(ctx):
    await ctx.message.delete()
    print(f'{commandLog}cls')
    clear()




#-----Tools Commands-----
@bot.command()
async def iplookup(ctx, ip: str = None):
    await ctx.message.delete()
    print(f'{commandLog}iplookup')
    if ip is None: await ctx.send("Please specify an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    embed= discord.Embed(colour=hexColor, title=f"Error",description="Invalid IP Address")
                    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
                    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
                    await ctx.send(embed=embed)
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(colour=hexColor, title=f"INFO",timestamp=datetime.utcfromtimestamp(time.time()))
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
                        embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")




#-----NSFW-----
@bot.command()
async def nsfw_neko(ctx):
    await ctx.message.delete()
    print(f'{commandLog}nsfw_neko')
    embed = discord.Embed(colour=hexColor, title="NSFW Neko",description="A random NSFW neko gif by nekos.life lib")
    embed.set_image(url=nekos.img("nsfw_neko_gif"))
    embed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embed.set_footer(text=" Macht Selfbot - Made by Founder#8300")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("An error has occured, are embeds allowed here?")














#Login
with open("config.json") as f:
    try:
     token = json.load(f)
     bot.run(token["token"], bot=False)
    except Exception as e:
     print(f"\nSomething went wrong, Error: {e}")
     input()