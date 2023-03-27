import interactions
from dotenv import load_dotenv
import openai as openaii
import os
import random
import json

load_dotenv()
openaii.api_key = os.getenv("OPENAI-TOKEN")
bot = interactions.Client(
    token=os.getenv("BOT-TOKEN")
)


@bot.command(name="ping", description="ping") #Every bot needs to keep the ping command
async def test(ctx):
    await ctx.send("Pong!")
    print(ctx)


@bot.command(name="openai",
    description="say openai!",
    options = [
        interactions.Option(
            name="message",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],)
async def openai(ctx: interactions.CommandContext, message: str):
    print(message)
    if random.randint(1, 2) == 1:
        selfpromo = "This bot was made by hii#6002"
    else:
        selfpromo = "The source of this project is available on github, check it out at https://github.com/Mushrrom/Openai-discord-bot"
    #embed creation
    responseembed = interactions.Embed(title="OpenAI text response", description = "Prompt: %s"%message, colour="#00ff00")
    responseembed.set_footer(text = selfpromo)
    responseembed.add_field(name = "Response", value = "Loading response...")
    responseembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/974174975793709056/974187217658454036/lp-logo-3-888629431.png")
    messagee = await ctx.send(embeds=[responseembed])
    #Wow thats annoying
    #Get response
    response = openaii.Completion.create(engine="text-babbage-001", prompt=message, temperature=1, max_tokens=400)

    response_txt = str(response['choices'][0]['text'])

    
    responseembed.set_field_at(index=0, name="Response", value = "%s `%s`"%(message,response_txt))#set field
    await messagee.edit(embeds=responseembed)#Edit original message
    # what am i doing I HAVE ENGLISH HOMEWORK I NEED TO DO
    
    # What is it with me doing this project when I have english assignments
bot.start()
