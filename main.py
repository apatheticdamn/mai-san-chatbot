import discord, os, requests, json, time, random
from keep_alive import keep_alive

from requests_and_responses.evening import *
from requests_and_responses.greeting import *
from requests_and_responses.hobby import *
from requests_and_responses.love import *
from requests_and_responses.mean import *
from requests_and_responses.morning import *
from requests_and_responses.night import *
from requests_and_responses.pervy import *
from requests_and_responses.sad import *
from requests_and_responses.wholesome import *


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    print(f"Received message: {msg}")

    if "ping" in msg:
        time.sleep(1)
        await message.channel.send("pong")

    elif any(word in msg for word in greeting_requests):
        time.sleep(1)
        await message.channel.send(random.choice(greeting_responses))

    elif any(word == msg for word in social_greeting):
        time.sleep(1)
        await message.channel.send(random.choice(social_greeting_replies))

    elif any(word in msg for word in morning_requests):
        time.sleep(1)
        await message.channel.send(random.choice(morning_responses))

    elif any(word in msg for word in evening_requests):
        time.sleep(1)
        await message.channel.send(random.choice(evening_responses))

    elif any(word in msg for word in love_requests):
        time.sleep(1)
        await message.channel.send(random.choice(love_responses))

    elif any(word in msg for word in pervy_requests):
        time.sleep(1)
        await message.channel.send(random.choice(pervy_responses))

    elif any(word in msg for word in social_greeting):
        time.sleep(1)
        await message.channel.send(random.choice(social_greeting_replies))

    elif any(word in msg for word in sad_requests):
        time.sleep(1)
        await message.channel.send(random.choice(encouraging_responses))

    elif any(word in msg for word in wholesome_requests):
        time.sleep(1)
        print("processing")
        await message.channel.send(wholesome_responses)

    elif any(word in msg for word in mean_requests):
        time.sleep(1)
        await message.channel.send(random.choice(mean_responses))

    elif any(word in msg for word in hobby_requests):
        time.sleep(1)
        await message.channel.send(random.choice(hobby_responses))


keep_alive()

my_secret = os.environ["MAISAN"]
client.run(my_secret)