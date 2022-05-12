from dotenv import load_dotenv
import discord
from discord import Client, Intents, Embed
import os
import openai as openaii
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import random
#Do I really need this many libraries?.. Yes ofc

#Dumb boring setup stuff
load_dotenv()
openaii.api_key = os.getenv("OPENAI-TOKEN")

bot = commands.Bot(command_prefix='-')
slash = SlashCommand(bot, sync_commands=True)


#Actual code fun stuff
@bot.event
async def on_ready():
    print('If you can see this then something is working. Logged in as {0.user}'.format(bot))

@slash.slash(name="ping", description="ping") #Every bot needs to keep the ping command
async def test(ctx):
    await ctx.send("Pong!")
    print(ctx)

@slash.slash(name="openai", description="Ask GPT-3 something")
async def openai(ctx, message):
    print(message)#Is self promotion really necessary?  Absolutely!
    if random.randint(1, 2) == 1:
        selfpromo = "\n\nThis bot was made by hii#6002"
    else:
        selfpromo = "\n\nThe source of this project is available on github, check it out at https://github.com/Mushrrom/Openai-discord-bot"
    openai_response = await ctx.send("```prompt = '%s'\nLoading ai... %s```"%(message, selfpromo))
    response = openaii.Completion.create(engine="text-babbage-001", prompt=message, temperature=1, max_tokens=400)
    print(response)
    print(response['choices'][0]['text'])
    response_txt = str(response['choices'][0]['text'])
    print(str(len(response_txt)))
<<<<<<< HEAD
    await openai_response.edit(content="prompt: %s\n```%s %s %s```"% (message, message, response_txt, selfpromo))
=======
    await ctx.send(response_txt) 
>>>>>>> 5fb7cba71168c4928dada3c2fe06e960ed95ef34
    #what am i doing I HAVE ENGLISH HOMEWORK I NEED TO DO

bot.run(os.getenv("BOT-TOKEN"))
