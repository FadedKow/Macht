import os
import colorama
import json
import requests
import math
import itertools
import random
import socket
import nekos
import threading
import discord
from datetime import *
from pathlib import Path
import time
from colorama import Fore, Style
from discord.ext import commands

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
machtPath = rf'{os.getcwd()}\Assets'
machtValues = {"patCount": 0, "hugCount": 0, "cuddleCount": 0, "kissCount": 0, "pokeCount": 0}
machtValuePath = rf'{os.getcwd()}\Assets\data.json'

# │
# ―
# guild.member_count()
# guild.name
# guild.owner
os.system("title Connecting to token")
print(f"{Fore.BLACK}=―――――――――――――――――――――――――――――――――――――――={resetClr}")
print(f'        {Fore.LIGHTMAGENTA_EX}    Macht Selfbot{resetClr}')
print(f'        {Fore.LIGHTMAGENTA_EX}Status:  {Fore.RED}Connecting...{resetClr}')
print(f"{Fore.BLACK}=―――――――――――――――――――――――――――――――――――――――={resetClr}")


def userConnected():
    print(f"{Fore.BLACK}=――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――={resetClr}")
    print(f"{Fore.MAGENTA}╔═╗╔═╗     ╔╗ ╔╗")
    print("║║╚╝║║     ║║╔╝╚╗")
    print("║╔╗╔╗╠══╦══╣╚╩╗╔╝")
    print("║║║║║║╔╗║╔═╣╔╗║║")
    print("║║║║║║╔╗║╚═╣║║║╚╗")
    print("╚╝╚╝╚╩╝╚╩══╩╝╚╩═╝")
    print(f'{Fore.LIGHTMAGENTA_EX}Status:  {Fore.GREEN}Connected!{resetClr}')
    print(f'{Fore.LIGHTMAGENTA_EX}Account: {bot.user.name} [Last Login: {lastTime}] [ID: {bot.user.id}]{resetClr}')
    print(f'{Fore.LIGHTMAGENTA_EX}Prefix:  {Fore.LIGHTCYAN_EX}{prefix}{resetClr}')
    print(f"{Fore.BLACK}=――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――={resetClr}")


def getUptime():
    return time.time() - startTime


my_file = Path(rf'{machtPath}\data.json')


def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as exc:
            print(exc)
            raise
    if not my_file.is_file():
        with open(os.path.join(target_path, target_file), 'w') as fWrite:
            json.dump(data, fWrite, sort_keys=True)


def initFiles():
    write_json(machtPath, 'data.json', machtValues)


initFiles()

"""with open(machtValuePath) as vF:
    dataConfig = json.load(vF)
    hugCount = dataConfig["hugCount"]
    patCount = dataConfig["patCount"]
    kissCount = dataConfig["kissCount"]
    cuddleCount = dataConfig["cuddleCount"]
    pokeCount = dataConfig["pokeCount"]"""


def updateTitle():
    for _ in itertools.repeat(None):
        os.system(
            "title Macht 1.0 │ " + str(math.floor(getUptime())) + " sec")  # Removing math.floor decreases memory usage
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
    if message.author.id != clientId:
        return
    if message.author == bot.user:
        return


@bot.command()
async def test(ctx):
    await ctx.message.delete()
    print(f'{commandLog}test')
    await ctx.send("Macht Test")
    embedTest = discord.Embed(colour=hexColor, title="Test", description="Embed Test")
    embedTest.set_image(url=nekos.img("avatar"))
    embedTest.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedTest)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


# -----Help Commands-----
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    print(f'{commandLog}help')
    embedHelpList = discord.Embed(colour=hexColor, title="Macht", description="<> = required, [] = optional")
    embedHelpList.add_field(name=f"`{prefix}help`", value=f"*Displays commands*", inline=False)
    embedHelpList.add_field(name=f"`{prefix}fun`", value=f"*Displays fun commands*", inline=False)
    embedHelpList.add_field(name=f"`{prefix}misc`", value=f"*Displays miscellaneous commands*", inline=False)
    embedHelpList.add_field(name=f"`{prefix}tools`", value=f"*Displays tool commands*", inline=False)
    embedHelpList.add_field(name=f"`{prefix}nsfw`", value=f"*Displays NSFW commands*", inline=False)
    embedHelpList.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedHelpList.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedHelpList)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def fun(ctx):
    await ctx.message.delete()
    print(f'{commandLog}fun')
    embedFunList = discord.Embed(colour=hexColor, title="Fun Commands")
    embedFunList.add_field(name=f"`{prefix}yoight`", value=f"*Sends yoights*", inline=False)
    embedFunList.add_field(name=f"`{prefix}ara`", value=f"*Sends ara ara in chat*", inline=False)
    embedFunList.add_field(name=f"`{prefix}gay <user> [value]`", value=f"*Gay rating of mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}cat`", value=f"*Random cat image*", inline=False)
    embedFunList.add_field(name=f"`{prefix}neko`", value=f"*Random neko image*", inline=False)
    embedFunList.add_field(name=f"`{prefix}foxgirl`", value=f"*Random foxgirl image*", inline=False)
    embedFunList.add_field(name=f"`{prefix}pat <user>`", value=f"*Pat mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}cuddle <user>`", value=f"*Cuddle mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}smug`", value=f"*Random smug face*", inline=False)
    embedFunList.add_field(name=f"`{prefix}kiss <user>`", value=f"*Kiss mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}hug <user>`", value=f"*Hug mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}owoify <text>`", value=f"*Owo-ify your message (r's become w's)*", inline=False)
    embedFunList.add_field(name=f"`{prefix}feed <user>`", value=f"*Feed mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}poke <user>`", value=f"*Poke mentioned user*", inline=False)
    embedFunList.add_field(name=f"`{prefix}woof <user>`", value=f"*Woof woof*", inline=False)
    embedFunList.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedFunList.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedFunList)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def misc(ctx):
    await ctx.message.delete()
    print(f'{commandLog}misc')
    embedMiscList = discord.Embed(colour=hexColor, title="Miscellaneous Commands")
    embedMiscList.add_field(name=f"`{prefix}embed <titletext> <fieldtext>`",
                            value=f"*Sends your message as an embed,* ***add quotes around fieldtext***", inline=False)
    embedMiscList.add_field(name=f"`{prefix}cls`", value=f"*Clears the console window*", inline=False)
    embedMiscList.add_field(name=f"`{prefix}test`", value=f"*Test command*", inline=False)
    embedMiscList.add_field(name=f"`{prefix}avatar`", value=f"*Get a free avatar provided by nekos.life py lib*", inline=False)
    embedMiscList.add_field(name=f"`{prefix}autocls <True/False>`", value=f"*Auto clear the console every 30 minutes*",
                            inline=False)
    embedMiscList.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedMiscList.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedMiscList)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def tools(ctx):
    await ctx.message.delete()
    print(f'{commandLog}tools')
    embedToolsList = discord.Embed(colour=hexColor, title="Tools")
    embedToolsList.add_field(name=f"`{prefix}iplookup <ip>`", value=f"*Displays info on ip*", inline=False)
    embedToolsList.add_field(name=f"`{prefix}resolve <domain>`", value=f"*Resolves domain to an ipv4 address*",
                             inline=False)
    embedToolsList.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedToolsList.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedToolsList)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def nsfw(ctx):
    await ctx.message.delete()
    print(f'{commandLog}nsfw')
    embedNsfwList = discord.Embed(colour=hexColor, title="NSFW")
    embedNsfwList.add_field(name=f"`{prefix}nsfw_neko`", value=f"*Random NSFW neko gif*", inline=False)
    embedNsfwList.add_field(name=f"`{prefix}hentai`", value=f"*Random hentai*", inline=False)
    embedNsfwList.add_field(name=f"`{prefix}kitsune`", value=f"*Random NSFW kitsune*", inline=False)
    embedNsfwList.add_field(name=f"`{prefix}nsfw_avatar`", value=f"*Random NSFW avatar*", inline=False)
    embedNsfwList.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNsfwList.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedNsfwList)
    except discord.HTTPException:
        await ctx.send("An error has occured, are embeds allowed here?")


# -----Fun Commands-----
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
async def gay(ctx, mentionedUser: str = None, gayValue: int = None):
    await ctx.message.delete()
    # -----Error-----
    embedError = discord.Embed(colour=hexColor, title="Error", description=f"No user has been mentioned")
    embedError.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedError.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----Error-----
    print(f'{commandLog}gay')
    if mentionedUser is None:
        try:
            await ctx.send(embed=embedError)
            return
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")
            return
    else:
        pass
    if gayValue is None:
        gayPercentage = random.randint(0, 100)
    else:
        gayPercentage = gayValue
    if mentionedUser == bot.user.name:
        gayPercentage = 0
    embedGayDisplay = discord.Embed(colour=hexColor, title="Gay Meter",
                                    description=f"**{mentionedUser}** is **{gayPercentage}% gay**")
    embedGayDisplay.set_thumbnail(
        url="https://i.dlpng.com/static/png/1210414-rainbow-flag-png-transparent-image-png-images-rainbow-flag-png-400_400_preview.png?width=341&height=341")
    embedGayDisplay.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedGayDisplay)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    print(f'{commandLog}cat')
    embedCat = discord.Embed(colour=hexColor, title="Cat", description="A random cat image by nekos.life lib")
    embedCat.set_image(url=nekos.cat())
    embedCat.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedCat)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def gato(ctx):
    await ctx.message.delete()
    print(f'{commandLog}gato')
    embedGato = discord.Embed(colour=hexColor, title="Gato", description="A random gato (cat) image by nekos.life lib")
    embedGato.set_image(url=nekos.cat())
    embedGato.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedGato)
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
                embedNeko = discord.Embed(colour=hexColor, title=f"Neko", description="Random neko by nekos.life")
                embedNeko.set_image(url=j["neko"])
                embedNeko.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                     text=" Macht Selfbot - Made by Founder#8300")
                await ctx.send(embed=embedNeko)
            except discord.HTTPException:
                await ctx.send(j["neko"])
    except Exception as egg:
        await ctx.send(f"Error: {egg}")


@bot.command()
async def foxgirl(ctx):
    await ctx.message.delete()
    print(f'{commandLog}foxgirl')
    embedFoxgirl = discord.Embed(colour=hexColor, title="Fox Girl",
                                 description="A random foxgirl image by nekos.life lib")
    embedFoxgirl.set_image(url=nekos.img("fox_girl"))
    embedFoxgirl.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedFoxgirl)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def pat(ctx, user: str = None):
    await ctx.message.delete()
    print(f'{commandLog}pat')
    # -----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error", description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if user is None:
        await ctx.send(embed=embedNoMen)
        return
    else:
        embedPat = discord.Embed(colour=hexColor, title="Pat Pat",
                                 description=f"***{bot.user.name}*** *pats* ***{user}***")
        embedPat.set_image(url=nekos.img("pat"))
        with open(machtValuePath) as fPat:
            try:
                patCountJson = json.load(fPat)
                patCountJson["patCount"] += 1
                patCount = patCountJson["patCount"]
                jsonFile = open(machtValuePath, "w+")
                jsonFile.write(json.dumps(patCountJson))
                embedPat.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                    text=f"That's {patCount} total pats now!")
                fPat.close()
            except Exception as patExcept:
                print(f"\nSomething went wrong, Error: {patExcept}")
        try:
            await ctx.send(embed=embedPat)
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def cuddle(ctx, user: str = None):
    await ctx.message.delete()
    print(f'{commandLog}cuddle')
    # -----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error", description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if user is None:
        await ctx.send(embed=embedNoMen)
        return
    else:
        embedCuddle = discord.Embed(colour=hexColor, title="Cuddle",
                                    description=f"***{bot.user.name}*** *cuddles* ***{user}***")
        embedCuddle.set_image(url=nekos.img("cuddle"))
        with open(machtValuePath) as fileCuddle:
            try:
                cuddleCountJson = json.load(fileCuddle)
                cuddleCountJson["cuddleCount"] += 1
                cuddleCount = cuddleCountJson["cuddleCount"]
                jsonFile = open(machtValuePath, "w+")
                jsonFile.write(json.dumps(cuddleCountJson))
                embedCuddle.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                       text=f"That's {cuddleCount} total cuddles now!")
                fileCuddle.close()
            except Exception as cuddleE:
                print(f"\nSomething went wrong, Error: {cuddleE}")
        try:
            await ctx.send(embed=embedCuddle)
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def smug(ctx):
    await ctx.message.delete()
    print(f'{commandLog}smug')
    embedSmug = discord.Embed(colour=hexColor, title="Smug", description="Random smug face by nekos.life lib")
    embedSmug.set_image(url=nekos.img("smug"))
    embedSmug.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedSmug)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def kiss(ctx, user: str = None):
    await ctx.message.delete()
    print(f'{commandLog}kiss')
    # -----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error", description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if user is None:
        await ctx.send(embed=embedNoMen)
        return
    else:
        embedKiss = discord.Embed(colour=hexColor, title="Kiss <3",
                                  description=f"***{bot.user.name}*** *kisses* ***{user}***")
        embedKiss.set_image(url=nekos.img("kiss"))
        with open(machtValuePath) as fileKiss:
            try:
                kissCountJson = json.load(fileKiss)
                kissCountJson["kissCount"] += 1
                kissCount = kissCountJson["kissCount"]
                jsonFile = open(machtValuePath, "w+")
                jsonFile.write(json.dumps(kissCountJson))
                embedKiss.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                     text=f"That's {kissCount} total kisses now!")
                fileKiss.close()
            except Exception as exceptKiss:
                print(f"\nSomething went wrong, Error: {exceptKiss}")
        try:
            await ctx.send(embed=embedKiss)
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def hug(ctx, user: str = None):
    await ctx.message.delete()
    print(f'{commandLog}hug')
    # -----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error", description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if user is None:
        await ctx.send(embed=embedNoMen)
        return
    else:
        embedHug = discord.Embed(colour=hexColor, title="Hug", description=f"***{bot.user.name}*** *hugs* ***{user}***")
        embedHug.set_image(url=nekos.img("hug"))
        with open(machtValuePath) as fileHug:
            try:
                hugCountJson = json.load(fileHug)
                hugCountJson["hugCount"] += 1
                hugCount = hugCountJson["hugCount"]
                jsonFile = open(machtValuePath, "w+")
                jsonFile.write(json.dumps(hugCountJson))
                embedHug.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=f"That's {hugCount} total hugs now!")
                fileHug.close()
            except Exception as exceptHug:
                print(f"\nSomething went wrong, Error: {exceptHug}")
        try:
            await ctx.send(embed=embedHug)
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def owoify(ctx, text: str = None):
    await ctx.message.delete()
    print(f'{commandLog}owoify')
    # -----No Text-----
    embedNoTextError = discord.Embed(colour=hexColor, title="Error", description="Please input a string to owo-ify")
    embedNoTextError.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoTextError.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if text is None:
        await ctx.send(embed=embedNoTextError)
        return
    else:
        owoifiedMessage = nekos.owoify(text)
        try:
            await ctx.send(owoifiedMessage)
        except discord.HTTPException:
            await ctx.send("Uh oh, a fucky wucky has occurred")


@bot.command()
async def feed(ctx, user: str = None):
    await ctx.message.delete()
    print(f'{commandLog}feed')
    # -----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error", description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if user is None:
        await ctx.send(embed=embedNoMen)
        return
    else:
        embedFeed = discord.Embed(colour=hexColor, title="Feed", description=f"***{bot.user.name}*** *feeds* ***{user}***")
        embedFeed.set_image(url=nekos.img("feed"))
        embedFeed.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
        try:
            await ctx.send(embed=embedFeed)
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def poke(ctx, user: str = None):
    await ctx.message.delete()
    print(f'{commandLog}poke')
    # -----No Mention-----
    embedNoMen = discord.Embed(colour=hexColor, title="Error", description="No user was mentioned")
    embedNoMen.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNoMen.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # -----End-----
    if user is None:
        await ctx.send(embed=embedNoMen)
        return
    else:
        embedPoke = discord.Embed(colour=hexColor, title="Poke", description=f"***{bot.user.name}*** *pokes* ***{user}***")
        embedPoke.set_image(url=nekos.img("poke"))
        with open(machtValuePath) as filePoke:
            try:
                pokeCountJson = json.load(filePoke)
                pokeCountJson["pokeCount"] += 1
                pokeCount = pokeCountJson["pokeCount"]
                jsonFile = open(machtValuePath, "w+")
                jsonFile.write(json.dumps(pokeCountJson))
                embedPoke.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                     text=f"That's {pokeCount} total pokes now!")
                filePoke.close()
            except Exception as exceptPoke:
                print(f"\nSomething went wrong, Error: {exceptPoke}")
        try:
            await ctx.send(embed=embedPoke)
        except discord.HTTPException:
            await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def woof(ctx):
    await ctx.message.delete()
    print(f'{commandLog}woof')
    embedWoof = discord.Embed(colour=hexColor, title="Woof", description="Woof woof!")
    embedWoof.set_image(url=nekos.img("woof"))
    embedWoof.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedWoof)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


# -----Misc Commands-----
@bot.command()
async def embed(ctx, titleText, fieldText):
    await ctx.message.delete()
    print(f'{commandLog}embed')
    embedEmbed = discord.Embed(colour=hexColor, title=" ")
    embedEmbed.add_field(name=titleText, value=fieldText, inline=False)
    try:
        await ctx.send(embed=embedEmbed)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def cls(ctx):
    await ctx.message.delete()
    print(f'{commandLog}cls')
    clear()


autoClsToggle = False


def autoClsClear():
    while autoClsToggle:
        for _ in itertools.repeat(None):
            clear()
            time.sleep(1800)


@bot.command()
async def autocls(ctx, toggled: bool = False):
    await ctx.message.delete()
    clear()
    print(f'{commandLog}autocls {toggled}')
    embedNotify = discord.Embed(colour=hexColor, title="Auto CLS", description=f"Auto CLS Set To **{toggled}**")
    embedNotify.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    embedNotify.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    if toggled:
        autoClsClear.autoClsToggle = True
        t = threading.Timer(0.5, autoClsClear)
        t.start()
        await ctx.send(embed=embedNotify)
    else:
        autoClsClear.autoClsToggle = False
        await ctx.send(embed=embedNotify)


@bot.command()
async def avatar(ctx):
    await ctx.message.delete()
    print(f'{commandLog}avatar')
    embedAvatar = discord.Embed(colour=hexColor, title="Avatar", description="Random vatar by nekos.life lib")
    embedAvatar.set_image(url=nekos.img("avatar"))
    embedAvatar.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedAvatar)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


# -----Tools Commands-----
@bot.command()
async def iplookup(ctx, ip: str = None):
    await ctx.message.delete()
    print(f'{commandLog}iplookup')
    if ip is None:
        await ctx.send("Please specify an IP address")
        return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    embedIpInfoError = discord.Embed(colour=hexColor, title=f"Error", description="Invalid IP Address")
                    embedIpInfoError.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
                    embedIpInfoError.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                                text=" Macht Selfbot - Made by Founder#8300")
                    await ctx.send(embed=embedIpInfoError)
                    return
                else:
                    try:
                        j = resp.json()
                        embedIpInfo = discord.Embed(colour=hexColor, title=f"INFO",
                                                    timestamp=datetime.utcfromtimestamp(time.time()))
                        embedIpInfo.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embedIpInfo.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embedIpInfo.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embedIpInfo.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embedIpInfo.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embedIpInfo.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embedIpInfo.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embedIpInfo.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embedIpInfo.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
                        embedIpInfo.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                               text=" Macht Selfbot - Made by Founder#8300")
                        await ctx.send(embed=embedIpInfo)
                    except discord.HTTPException:
                        await ctx.send(
                            f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as exceptIp:
            await ctx.send(f"Error: {exceptIp}")


@bot.command()
async def resolve(ctx, domain: str = None):
    await ctx.message.delete()
    print(f'{commandLog}resolve')
    # Invalid Domain
    domainErrorEmbed = discord.Embed(colour=hexColor, title="Domain Error", description="No Domain Specified")
    domainErrorEmbed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    domainErrorEmbed.set_footer(icon_url="https://i.imgur.com/pVbTpks.png",
                                text=" Macht Selfbot - Made by Founder#8300")
    # Invalid Domain End
    # -----
    # Error
    hostErrorEmbed = discord.Embed(colour=hexColor, title="Domain Error", description="Invalid Domain Name")
    hostErrorEmbed.set_thumbnail(url="https://i.imgur.com/pVbTpks.png")
    hostErrorEmbed.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    # Error End
    if domain is None:
        await ctx.send(embed=domainErrorEmbed)
        return
    else:
        try:
            embedResolve = discord.Embed(colour=hexColor, title=" ")
            embedResolve.add_field(name="Domain: ", value=domain, inline=True)
            embedResolve.add_field(name="Ipv4", value=str(socket.gethostbyname(domain)), inline=True)
            try:
                await ctx.send(embed=embedResolve)
            except discord.HTTPException:
                await ctx.send("An error has occurred, are embeds allowed here?")
        except Exception as exceptHost:
            await ctx.send(embed=hostErrorEmbed)
            print(exceptHost)


# -----NSFW-----
@bot.command()
async def nsfw_neko(ctx):
    await ctx.message.delete()
    print(f'{commandLog}nsfw_neko')
    embedNsfwNeko = discord.Embed(colour=hexColor, title="NSFW Neko", description="A random NSFW neko gif by nekos.life lib")
    embedNsfwNeko.set_image(url=nekos.img("nsfw_neko_gif"))
    embedNsfwNeko.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedNsfwNeko)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def hentai(ctx):
    await ctx.message.delete()
    print(f'{commandLog}hentai')
    embedHentai = discord.Embed(colour=hexColor, title="Hentai", description="Random hentai by nekos.life lib")
    embedHentai.set_image(url=nekos.img("hentai"))
    embedHentai.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedHentai)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def kitsune(ctx):
    await ctx.message.delete()
    print(f'{commandLog}kitsune')
    embedKitsune = discord.Embed(colour=hexColor, title="Kitsune", description="A random kitsune image by nekos.life lib")
    embedKitsune.set_image(url=nekos.img("lewdk"))
    embedKitsune.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedKitsune)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


@bot.command()
async def nsfw_avatar(ctx):
    await ctx.message.delete()
    print(f'{commandLog}nsfw_avatar')
    embedNsfwAvatar = discord.Embed(colour=hexColor, title="NSFW Avatar", description="Random NSFW avatar by nekos.life lib")
    embedNsfwAvatar.set_image(url=nekos.img("nsfw_avatar"))
    embedNsfwAvatar.set_footer(icon_url="https://i.imgur.com/pVbTpks.png", text=" Macht Selfbot - Made by Founder#8300")
    try:
        await ctx.send(embed=embedNsfwAvatar)
    except discord.HTTPException:
        await ctx.send("An error has occurred, are embeds allowed here?")


# Login
with open("config.json") as f:
    try:
        token = json.load(f)
        bot.run(token["token"], bot=False)
    except Exception as e:
        print(f"\nSomething went wrong, Error: {e}")
        input()
