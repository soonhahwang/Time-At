import os
import discord
import datetime
import pytz
from datetime import datetime

print(os.getenv('bot_token'))
TOKEN = os.getenv('bot_token')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!time'):
        await message.channel.send(message.content[5:].format(message))
        if any(message.content[5:] in word for word in pytz.all_timezones):
            matching = [s for s in pytz.all_timezones if message.content[5:] in pytz.all_timezones]
            await message.channel.send('found in dictionary')

        else:
            await message.channel.send('not in timezone')



    elif message.content.startswith('!testADD'):
        await message.channel.send(datetime.now(pytz.timezone(pytz.all_timezones[2])).strftime("%H:%M:%S"))


            
        

client.run('')
