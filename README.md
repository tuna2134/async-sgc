# async-sgc

### sample code

```py
import discord
from async_sgc import Read
from async_sgc import Send

client = discord.Client()

@client.event
async def on_message(message):
    if not message.author.bot:
      GLOBAL_CH_NAME = "hoge-global"

      if message.channel.name == GLOBAL_CH_NAME:
        ch = client.get_channel(707158343952629780)
        sgc=Read(message)
        await ch.send(await sgc.send())
        await message.delete()
        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        embed = discord.Embed(title="hoge-global",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        for channel in global_channels:
            await channel.send(embed=embed)
            

client.run('your token')
