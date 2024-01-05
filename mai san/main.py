import discord, os, requests, json, time, random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

user_perv_words = [
  "boob",
  "boobs",
  "panties",
  "kiss",
  "cuddle",
  "panty"
]

mai_san_perv_replies = [
  "You are such a pervert!",
  "Don't you dare get near me!",
  "What if I said no?",
  "Firstly, beg me.",
  "Close your eyes",
  "Did you really thought I'd do that?",
  "You are such a pervert!",
  "Hey, why don't we kiss?"
]


user_greeting_words = [
  "hello",
  "hi",
  "hey",
  "sup",
  "yo",
  "wassup",
  "hii",
  "hiii",
  "hlo",
  "hi mai san",
  "hlo mai san"
]

mai_san_greeting_replies = [
  "Hiii!",
  "Hello!",
  "Hey!",
  "Hi!",
  "Hiiiii!"
]



user_sad_words = ["sad",
  "depressed",
  "unhappy",
  "angry",
  "miserable",
  "depressing"
]


mai_san_encouraging_replies = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person",
  "Don't worry things will get better",
  "Let me give you a hug come here",
  "Everything is gonna be okay"
]


user_love_words = [
  "i love you",
  "do you love me?",
  "i am the most luckiest person in the world",
  "mai san i love you",
  "mai san i love you so much"
]

mai_san_love_replies = [
  "I love you!",
  "I love you too",
  "You are the best person in the world!",
  "Ofcourse I love you",
  "Ofcourse your the most luckiest person, you are dating me.",
  "Thank you I love you soo much"
  ]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if any(greeting_word == msg for greeting_word in user_greeting_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_greeting_replies))
    elif any(phrase in msg for phrase in user_love_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_love_replies))
    elif any(word in msg for word in user_perv_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_perv_replies))
    elif any(word in msg for word in user_sad_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_encouraging_replies))

keep_alive()

my_secret = os.environ['MAISAN']
client.run(my_secret)