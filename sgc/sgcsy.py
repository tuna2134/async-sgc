import asyncio
import discord
from discord.ext import commands

async def send(message):
	rjson = {
           "userId": message.author.id,
           "userName": message.author.name,
           "userDiscriminator": message.author.discriminator,
           "userAvatar": message.author.avatar,
           "isBot": message.author.bot,
           "guildId": message.guild.id,
           "guildName": message.guild.name,
           "guildIcon": message.guild.icon,
           "channelId": message.channel.id,
           "channelName": message.channel.name,
           "messageId": message.id,
           "content": message.content
     }
     if message.attachments:
       url = message.attachments[0].url
       rjson["attachmentsUrl"] = [url]
     return json.dumps(rjson)) 
     
async def read(cnt):
	res=json.loads(cnt)
	c="None"
	if res["attachmentsUrl"]:
		c=res["attachmentsUrl"]
	return user_id=res["userId"],user_name=res["userName"],user_tag=res["userDiscriminator"],user_avatar=res["userAvatar"],isbot=res["isBot"],guild_id=res["guildId"],guild_name=res["guildName"],guild_icon=res["guildIcon"],channel_id=res["channelId"],channel_name=res["channelName"],message_id=res["messageId"],message_content=res["content"], attachments_url=c
