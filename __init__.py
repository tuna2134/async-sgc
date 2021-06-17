import asyncio
import json

class Read:
  def __init__(self,message):
    self.message=message
  
  async def send(self):
	  rjson = {
	    "userId": self.message.author.id,
      "userName": self.message.author.name,
      "userDiscriminator": self.message.author.discriminator,
      "userAvatar": self.message.author.avatar,
      "isBot": self.message.author.bot,
      "guildId": self.message.guild.id,
      "guildName": self.message.guild.name,
      "guildIcon": self.message.guild.icon,
      "channelId": self.message.channel.id,
      "channelName": self.message.channel.name,
      "messageId": self.message.id,
      "content": self.message.content
	  }
	  if self.message.attachments:
	    url = self.message.attachments[0].url
	    rjson["attachmentsUrl"] = [url]
	  return json.dumps(rjson)
