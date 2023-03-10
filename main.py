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
    if random.randint(1, 2) == 1:
        selfpromo = "This bot was made by hii#6002"
    else:
        selfpromo = "The source of this project is available on github, check it out at https://github.com/Mushrrom/Openai-discord-bot"
    #embed creation
    responseembed = discord.Embed(title="OpenAI text response", description = "Prompt: %s"%message, colour=discord.Colour.green())
    responseembed.set_footer(text = selfpromo)
    responseembed.add_field(name = "Response", value = "Loading response...")
    responseembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/974174975793709056/974187217658454036/lp-logo-3-888629431.png")
    messagee = await ctx.send(embed=responseembed)
    #Wow thats annoying
    #Get response
    response = openaii.Completion.create(engine="text-babbage-001", prompt=message, temperature=1, max_tokens=400)

    response_txt = str(response['choices'][0]['text'])

    
    responseembed.set_field_at(index=0, name="Response", value = "%s `%s`"%(message,response_txt))#set field
    await messagee.edit(embed=responseembed)#Edit original message
    # what am i doing I HAVE ENGLISH HOMEWORK I NEED TO DO
    
    # What is it with me doing this project when I have english assignments
bot.run(os.getenv("BOT-TOKEN"))
