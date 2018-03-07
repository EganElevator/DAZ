import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "this")
do = 'msg'
go = 2

chat_filter = ["FUCK", "CRAP", "SHIT"]
bypass_list = ["371756025717587969"]


@client.event
async def on_ready():
   print ("Active!")


@client.event
async def on_message(message):
   if message.content.upper().startswith("EC2PING"):
      userID = message.author.id
      await client.send_message(message.channel, "<@%s> Pong!" % (userID))
   if message.content.upper().startswith("EC2CHAT"):
      if message.author.userid == "371756025717587968":
          args = message.content.split(" ")
          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
      else:
          await client.send_message(message.channel, "<@%s> You are NOT my boss!" % (userID))
   if message.content.upper().startswith("EC2AMIADMIN"):
      if "410550034027773973" in [role.id for role in message.author.roles]:
         await client.send_message(message.channel, "Yes.")
      else:
         await client.send_message(message.channel, "No.")
   contents = message.content.split(" ")
   for word in contents:
      if word.upper() in chat_filter:
        if not message.author.id in bypass_list:
           await client.delete_message(message)
           await client.send_message(message.channel, "You said a forbidden word!")
   if message.content.upper().startswith("EC2SPAMCAST"):
      args = message.content.split(" ")
      if args[1] == ("start"):
           go = 1
           while go==1:
              await client.send_message(message.channel, "%s" % (" ".join(args[2:])))
              if go==0:
                 break
      return
      if args[1] == ("pause"):
         go = 0
                            
                   
          
client.run("NDIwNjc4NDk3NTc3NzMwMDgw.DYCiyA.VA1WUVBeebRfc6rWwbcgqcQ77LQ")
