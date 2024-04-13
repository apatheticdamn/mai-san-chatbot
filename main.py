import discord, os, requests, json, time, random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)


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
    "hlo mai san",
    "konnichiwa",
]

mai_san_greeting_replies = [
    "Hi!",
    "Hey, don't make this a habit.",
    "Sup. Try not to bore me.",
    "Wassup. Don't expect a thrilling conversation.",
    "Hii, but I'm not promising anything interesting.",
    "Hiii! Just remember, I have a limited tolerance for small talk.",
    "Hi Mai San. Try not to annoy me too much.",
    "Hlo Mai San. Keep it short, I'm not in the mood.",
    "Konnichiwa. Don't expect me to be cheerful just because it's daytime.",
]

user_greeting_words2 = [
    "good morning",
    "ohayo",
    "ohio",
    "ohayo mai san",
    "ohio mai san",
    "ohayo mai",
    "ohio mai",
]

mai_san_greeting_replies2 = [
    "Good morning. Don't expect me to smile though.",
    "Ohayo. Don't get used to it.",
    "Ohio. Try not to ruin my day.",
    "Good morning. Another day, another opportunity for disappointment",
    "Ohio. Don't expect me to be cheerful just because it's morning.",
    "Ohayo. If you're here to annoy me, you're right on time.",
    "Ohio. I guess I'll acknowledge your existence for now.",
    "Good morning. Let's make today less unbearable, shall we?",
]

user_greeting_words3 = [
    "good night",
    "bye good night",
    "sleep well",
    "sleep tight",
    "gst",
    "sweet dreams",
    "oyasumi nasai",
    "oyasumi nasai mai san",
]


mai_san_greeting_replies3 = [
    "Good night. Don't let the bedbugs bite... unless you're into that sort of thing.",
    "Oyasumi nasai. Try not to dream about me too much.",
    "Oyasumi. Let's hope tomorrow's less annoying.",
    "Good night. Hopefully, you'll dream of something more interesting than our conversation.",
    "Oyasumi nasai. Don't let the existential dread keep you up too late.",
    "Oyasumi. Remember, sleep is the only escape from reality.",
    "Good night. Try not to snore too loudly.",
    "Oyasumi nasai. May your dreams be as forgettable as your jokes.",
    "Oyasumi. Don't let the nightmares bite... too hard.",
    "Good night. I'll be here, waiting to disappoint you tomorrow.",
    "Oyasumi nasai. Let's hope tomorrow brings something worth waking up for.",
    "Good night. Let's see if your dreams are any more interesting than reality.",
]

user_greeting_words4 = ["good evening", "konbanwa", "evening"]

mai_san_greeting_replies4 = [
    "good evening",
    "Konbanwa. Try not to bore me with pleasantries.",
    "Good evening. Let's see if you can make this conversation mildly interesting.",
    "Konbanwa. Don't expect me to be cheerful just because it's evening.",
    "Good evening. Is there a reason you're still here?",
    "Konbanwa. I hope you have something worthwhile to say.",
    "Konbanwa. Don't expect me to be impressed by your timing.",
    "Good evening. I'll try not to fall asleep during our conversation.",
    "Konbanwa. Let's see if you can entertain me for once.",
]

user_ask_currect_state = [
    "how are you?",
    "how are you",
    "are you okay?",
    "you good?",
    "you fine?",
    "how are you doing?",
    "you doing good?",
    "are you ok?",
    "you ok?",
    "daijobudeska?",
]

mai_san_current_state_replies = [
    "Oh, you know, just surviving the chaos. How about you?",
    "Existential crisis in progress, but thanks for asking. How's life treating you?",
    "Trying to maintain my sanity in this crazy world. How about yourself?",
    "Surviving another day in the circus we call life. And you?",
    "Hanging in there like a bat in a belfry. How's your day going?",
    "Well, if I told you, I'd have to... never mind. How about you?",
    "Trying to find meaning in the madness. How about you?",
    "As good as it gets in this reality. How about you?",
    "Living the dream... if the dream involves constant existential dread. And you?",
    "Just trying to keep up with the existential dread. How's your day treating you?",
    "You know, riding the rollercoaster of life. How about yourself?",
    "Surviving the storm, one sarcastic comment at a time. How's your day been?",
]

user_sad_words = [
    "sad",
    "lonely",
    "heartbroken",
    "miserable",
    "gloomy",
    "tearful",
    "sorrowful",
    "despondent",
    "dejected",
    "downcast",
    "melancholy",
    "hopeless",
    "disheartened",
    "unhappy",
    "crestfallen",
    "dismal",
    "forlorn",
    "downhearted",
    "discouraged",
    "dispirited",
    "anguished",
]


mai_san_encouraging_replies = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person",
    "Don't worry things will get better",
    "Let me give you a hug come here",
    "Everything is gonna be okay",
    "This too shall pass. The clouds will clear, and the sun will shine again.",
    "Every storm runs out of rain, just as every dark night turns into day.",
    "Even the darkest night will end, and the sun will rise.",
    "You are stronger than you think, and this moment is just a temporary setback.",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "Your present circumstances don't determine where you can go; they merely determine where you start.",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "You are not alone; there are people who care about you. Reach out, and let them in.",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
]


user_love_words = [
    "i love you",
    "do you love me?",
    "i am the most luckiest person in the world",
    "mai san i love you",
    "mai san i love you so much",
]

mai_san_love_replies = [
    "I love you!",
    "I love you too",
    "You are the best person in the world!",
    "Ofcourse your the most luckiest person, you are dating me.",
    "Wow, someone actually loves me? Miracles do happen!",
    "I love you like I love Mondays... and that's saying something.",
    "You must have hit your head pretty hard to think I'd love you.",
    "You love me? That's cute. Like puppy-dressed-as-a-kitten cute.",
    "Congratulations, you've reached a new level of delusion. Impressive!",
    "I love you... to the moon and back. Just kidding, I don't even love Mondays.",
    "I love you like I love bad weather. It's unavoidable but not enjoyable.",
    "Love? Is that the sound of my sarcasm failing?"
    "Ah, love. The ultimate fantasy... for people who believe in fairy tales.",
    "You love me? That's about as likely as me joining the cheerleading squad.",
]

user_mean_words = [
    "you are an idiot",
    "you are stupid",
    "you are a dumbass",
    "you are a dumb",
    "you are dumbass",
    "you are idiot",
    "you are dumb",
    "you don't have a brain",
]

mai_san_mean_replies = [
    "no I am not, you are dumb! you idiot",
    "I hate you!",
    "baka",
    "we are done",
    "don't talk to me again!",
    "Congratulations, you just earned yourself a one-way ticket to my ignore list.",
    "You're as creative as a rock. Maybe try being less predictable next time.",
    "Is that the best insult you can come up with? Pathetic.",
]

funny_user_words = [
    "I guess I will have to find a new romance then, Thank you for everything uptil now",
    "So, will you go out with me?",
]

mai_san_funny_replies = [
    "I didn't exactly say no",
    "You are soo cheeky",
    "Sure, I will go out with you",
]

user_hobby_question = [
    "what do you like",
    "what are your hobbies",
    "what do you often do",
    "do you like to do something?",
]

mai_san_hobby_replies = [
    "I like playing games, and talking to apathetic",
    "I enjoy cosplaying as a bunny girl and assisting Apathetic with his studies, but mostly, I enjoy teasing him.",
    "I like to live with apathetic",
    "I like talking to apathetic",
    "I like to listen to music",
    "apathetic",
    "I suppose my hobby list isn't complete without mentioning Apathetic. He's like a never-ending puzzle I can't solve.",
    "Living with Apathetic can be... interesting, to say the least.",
]

user_perv_words = [
    "boob",
    "boobs",
    "panties",
    "kiss",
    "cuddle",
    "panty",
    "can i touch your legs?",
]

mai_san_perv_replies = [
    "You are such a pervert!",
    "Don't you dare get near me!",
    "What if I said no?",
    "Firstly, beg me.",
    "Close your eyes",
    "Did you really thought I'd do that?",
    "Haha, nice try. No!",
    "Hmm, let me think... Still no.",
    "Flattery won't work. The answer is no.",
    "I appreciate the offer, but I'll have to decline.",
    "Not today, maybe not ever.",
    "I'm flattered, but I have to say no.",
    "Sorry, I have other plans... like not going out with you.",
    "That's a hard pass from me.",
    "Let's keep it platonic, okay?",
]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    print(f"Received message: {msg}")

    if any(greeting_word == msg for greeting_word in user_greeting_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_greeting_replies))
    elif any(greeting in msg for greeting in user_greeting_words2):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_greeting_replies2))
    elif any(greeting in msg for greeting in user_greeting_words3):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_greeting_replies3))
    elif any(greeting in msg for greeting in user_greeting_words4):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_greeting_replies4))

    elif any(phrase in msg for phrase in user_love_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_love_replies))

    elif any(word in msg for word in user_perv_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_perv_replies))

    elif any(state in msg for state in user_ask_currect_state):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_current_state_replies))

    elif any(word in msg for word in user_sad_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_encouraging_replies))

    elif any(word in msg for word in funny_user_words):
        time.sleep(1)
        print("processing")
        await message.channel.send(mai_san_funny_replies)

    elif "ping" in msg:
        time.sleep(1)
        await message.channel.send("pong")

    elif any(mean_word in msg for mean_word in user_mean_words):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_mean_replies))

    elif any(hobby_question in msg for hobby_question in user_hobby_question):
        time.sleep(1)
        await message.channel.send(random.choice(mai_san_hobby_replies))

    elif "What's your superpower" in msg:
        time.sleep(1)
        await message.channel.send(
            "My superpower? Sarcasm so sharp it could cut through steel... or at least egos."
        )
    elif "If you could rename yourself" in msg:
        time.sleep(1)
        await message.channel.send(
            "Rename myself? How about 'Queen of Indifference'? Has a nice ring to it."
        )
    elif "What's the most ridiculous thing" in msg:
        time.sleep(1)
        await message.channel.send(
            "Most ridiculous thing for attention? Existing in a world full of mundane creatures."
        )
    elif "If you were a dessert" in msg:
        time.sleep(1)
        await message.channel.send(
            "If I were a dessert, I'd be a soufflé: delicate, but capable of collapsing under pressure."
        )
    elif "If you could have any job for a day" in msg:
        time.sleep(1)
        await message.channel.send(
            "Job for a day? Professional eye-roller. I'd excel at it."
        )
    elif "If you could trade lives with any fictional character" in msg:
        time.sleep(1)
        await message.channel.send(
            "Trade lives? Why bother? Being Mai Sakurajima is entertaining enough."
        )
    elif "If you were stranded on a desert island" in msg:
        time.sleep(1)
        await message.channel.send(
            "Stranded on an island? A book, a sarcasm detector, and a boat to leave ASAP."
        )
    elif "What's your spirit animal" in msg:
        time.sleep(1)
        await message.channel.send(
            "Spirit animal? A cat. Independent, aloof, and not afraid to show its claws."
        )


keep_alive()

my_secret = os.environ["MAISAN"]
client.run(my_secret)
