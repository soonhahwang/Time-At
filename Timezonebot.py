import os
import discord
from datetime import datetime
from pytz import timezone
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder



print(os.getenv('bot_token'))
TOKEN = os.getenv('bot_token')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('with time'))
    print("Timebot is ready")

@client.event
async def on_message(message):




    if message.author == client.user:
        return
##################################################################################################################################################################
   
    if message.content.startswith('!time'):
        region = message.content[5:]
        geolocator = Nominatim(user_agent="Discord bot")
        location = geolocator.geocode(region)

        local_zone = TimezoneFinder(in_memory=True)
        local_zone = local_zone.timezone_at(lng= location.longitude, lat = location.latitude)
        await message.channel.send("**"+datetime.now(timezone(local_zone)).strftime("%I:%M:%S %p")+"**, "+"Timezone: "+local_zone)

    elif message.content.startswith('!testADD'):
        await message.channel.send(datetime.now(pytz.timezone('Europe/Paris')))


##################################################################################################################################################################

            
        

client.run('')
