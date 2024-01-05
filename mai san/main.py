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

user_greeting_words2 = [
  "good morning",
  'ohayo',
  'ohio',
  'ohayo mai san',
  'ohio mai san',
  'ohayo mai',
  'ohio mai',
]

mai_san_greeting_replies2 = [
  "good morning",
  'ohayo',
  'ohio'
]

user_greeting_words3 = [
  "good night",
  'bye good night',
  'night',
  'sleep well',
  'sleep tight',
  'gst',
  'sweet dreams',
  'oyasumi nasai',
  'oyasumi nasai mai san'
]

mai_san_greeting_replies3 = [
  "good night",
  'Oyasumi nasai',
  'Oyasumi'
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
  "Ofcourse your the most luckiest person, you are dating me."
]



user_mean_words = [
  'you are an idiot',
  'you are stupid',
  'you are a dumbass',
  'you are a dumb',
  'you are dumbass',
  'you are idiot',
  'you are dumb',
  "you don't have a brain"
]

mai_san_mean_replies = [
  'no I am not, you are dumb! you idiot',
  'I hate you!',
  'baka',
  'we are done',
  "don't talk to me again!"
]

funny_user_words = [
  "I guess I'll have to find a new romance then, Thank you for everything uptil now",
  'So will you go out with me?'
]

mai_san_funny_replies = [
  "I didn't exactly say no",
  "You are soo cheeky",
  "Sure I will go out with you"
]

user_hobby_question = [
  'what do you like',
  'what are your hobbies',
  'what do you often do',
  'do you like to do something?'
]

mai_san_hobby_replies = [
  "I like to play games, and talk to apathetic",
  "I cosplay bunny girl and help apathetic in his studies",
  'I like to live with apathetic',
  'I like talking to apathetic',
  'I like to listen to music',
  'apathetic'
]

user_bad_words = [
  "fuck",
  'ass',
  'sex',
  'fucking',
  'bitch',
  'whore',
  'dick',
  'pussy',
  'cunt',
  'penis',
  'vagina',
  'cock',
  'nigga',
  'nigger',
  'ugly'
]

mai_san_bad_words_replies = [
  "please don't talk to me like that.",
  "i don't like that word.",
  "please don't use that word",
  "please dont' get ahead of yourself",
  "don't say these kind of things"
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
    elif any(greeting in msg for greeting in user_greeting_words2):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_greeting_replies2))
    elif any(greeting in msg for greeting in user_greeting_words3):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_greeting_replies3))
      
    elif any(phrase in msg for phrase in user_love_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_love_replies))
      
    elif any(word in msg for word in user_perv_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_perv_replies))
      
    elif any(word in msg for word in user_sad_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_encouraging_replies))
      
    elif any(funny_word in msg for funny_word in funny_user_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_funny_replies))
      
    elif any(mean_word in msg for mean_word in user_mean_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_mean_replies))
      
    elif any(hobby_question in msg for hobby_question in user_hobby_question):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_hobby_replies))

    elif any(bad_word in msg for bad_word in user_bad_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_bad_words_replies))


keep_alive()

my_secret = os.environ['MAISAN']
client.run(my_secret)
