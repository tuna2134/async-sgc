import asyncio
import json

class Send:
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

class Read:
  def __init__(self,content):
    res=json.loads(content)
    self.res=res

  async def user_id(self):
    return self.res["userId"]
  
  async def user_name(self):
    return self.res["userName"]

  async def user_tag(self):
    return self.res["userDiscriminator"]

  async def user_avatar(self):
    return self.res["userAvatar"]

  async def user_bot(self):
    return self.res["isBot"]

  async def guild_id(self):
    return self.res["guildId"]

  async def guild_name(self):
    return self.res["guildName"]

  async def guild_icon(self):
    return self.res["guildIcon"]

  async def channel_id(self):
    return self.res["channelId"]

  async def message_id(self):
    return self.res["channelName"]

  async def message_content(self):
    return self.res["content"]

  async def message_attachments(self):
    if self.res["attachmentsUrl"]:
      return self.res["attachmentsUrl"]
    else:
      return "None"
