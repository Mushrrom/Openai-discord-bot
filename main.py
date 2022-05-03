from dotenv import load_dotenv
import discord
from discord import Client, Intents, Embed
import os
import openai as openaii
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

load_dotenv()

openai_token = os.getenv("OPENAI-TOKEN")
bot_token = os.getenv("BOT-TOKEN")

#PROGRAM HERE
guild_ids = [970592778495090728]
openaii.api_key = openai_token


bot = commands.Bot(command_prefix='-')
slash = SlashCommand(bot, sync_commands=True)
@bot.event

async def on_ready():
    print('If you can see this then something is working. Logged in as {0.user}'.format(bot))

@slash.slash(name="ping", description="ping")
async def test(ctx):
    await ctx.send("Pong!")
    print(ctx)



@slash.slash(name="openai", description="Ask GPT-3 something")
async def openai(ctx, message):
    print(message)
    await ctx.send("```Loading ai... \nprompt = '%s'```"%message)
    response = openaii.Completion.create(engine="text-davinci-002", prompt=message, temperature=1, max_tokens=400)
    print(response['choices'][0]['text'])
    response_txt = str(response['choices'][0]['text'])
    print(str(len(response_txt)))
    await ctx.send(response_txt)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('openai'):
        stuff = message.content
        stuff = stuff.replace('openai ', '')
        response = openaii.Completion.create(engine="text-davinci-002", prompt=stuff, temperature=1, max_tokens=2000)
        await message.channel.send(response['choices'][0]['text'])

bot.run(bot_token)