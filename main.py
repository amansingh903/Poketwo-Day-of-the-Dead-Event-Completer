import discord
from discord.ext import commands
import config
import re
import asyncio
import random
import requests
from utility import Utils
import time


bot = commands.Bot(command_prefix="!",self_bot=True)
sleeping = config.sleep


def click_button(guild_id, channel_id, message_id, button_custom_id, user_id, session_id, application_id):
    url = f"https://discord.com/api/v10/interactions"
    headers = {
        "Authorization": f"Bot YOUR_BOT_TOKEN",
        "Content-Type": "application/json"
    }
    payload = {
        "type": 2,  # Type 2 corresponds to a button interaction
        "token": "YOUR_INTERACTION_TOKEN",  # This is obtained from the original message containing the button
        "member": {
            "user": {
                "id": user_id  # User ID of the bot or the user simulating the click
            },
            "session_id": session_id,
            "deaf": False,
            "mute": False,
        },
        "guild_id": str(guild_id),
        "channel_id": str(channel_id),
        "message_id": str(message_id),
        "data": {
            "component_type": 2,  # Type 2 represents buttons
            "custom_id": button_custom_id,  # The unique ID for the button
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


async def market_search():
    channel = bot.get_channel(config.ChannelId)
    if channel:
        await channel.send('<@716390085896962058> m s')

async def market_buy(hint):
    channel = bot.get_channel(config.ChannelId)
    await asyncio.sleep(5)
    if channel:
        await channel.send(f'<@716390085896962058> m b {hint}')


async def spam():
    while not sleeping:
        channel = bot.get_channel(config.ChannelId)
        if channel is not None:
            random_message = random.randint(1,5)
            if random_message==1:
                await channel.send('<@716390085896962058> ev q')
            if random_message==2:
                await channel.send('<@716390085896962058> event quests')
            if random_message==3:
                await channel.send('<@716390085896962058> dotd q')
            if random_message==4:
                await channel.send('<@716390085896962058> ev quests')
            random_interval = random.uniform(50, 100)  # Random interval between 50 and 100 seconds
            await asyncio.sleep(random_interval)
        else:
            print("Channel not found. Please check the channel ID in the config.")
            break

@bot.event
async def on_ready():
    print(f'\033[91mLOGGED IN AS {bot.user.name} ({bot.user.id})\033[0m')
    print(f'\033[91mSERVER STATUS: ONLINE\033[0m')
    print(f'\033[91mMade by who.meee\033[0m')
    print(f'\033[91m------------------------------------------------------------------------------------------\033[0m')
    await spam()

@bot.event
async def on_message(msg: discord.Message):
    channel = bot.get_channel(config.ChannelId)
    message = msg.content

    if msg.author.id == 716390085896962058 and msg.guild.id== config.GuildId:
        for embed in msg.embeds:
            if 'mysterious' in embed.title and "Trade" not in embed.description:
                await asyncio.sleep(5)
                try: 
                    click_yes = msg.components[0].children[0]
                    custom_id = click_yes.custom_id
                    guild_id = str(msg.guild.id)
                    session_id = Utils.generate_session_id()
                    type = 2
                    channel_id = str(msg.channel.id)
                    application_id = str(msg.author.id)
                    Utils.click_button(config.token, msg.id, custom_id, channel_id, guild_id, application_id, session_id, type)
                except:
                    pass
                await asyncio.sleep(5)
                await channel.send('<@716390085896962058> ev q')

            elif 'Quests' in embed.title:
                missions=embed.description
                if "Trade" in missions and "~~Trade" not in embed.description:
                    await asyncio.sleep(5)
                    await channel.send('<@716390085896962058> dotd cancel')

                elif "Release" in missions and "~~Release" not in embed.description:
                    await asyncio.sleep(5)
                    await channel.send('<@716390085896962058> r l')

                elif "Spend" in missions and "~~Spend" not in embed.description:
                    await market_search()

                elif "Earn" in missions and "~~Earn" not in embed.description:
                    await asyncio.sleep(5)
                    await channel.send('<@716390085896962058> market add l 500')

                elif "Evolve" in missions and "~~Evolve" not in embed.description:
                    await asyncio.sleep(5)
                    await channel.send('<@716390085896962058> p --n bidoru')

            elif "Pokétwo Marketplace" in embed.title:
                market_info = embed.description
                marketpattern = r"`(\d+)`.*?•\s*500 pc"
                hint = re.findall(marketpattern,market_info)
                hint=hint[0]
                await market_buy(hint)

            elif "Your pokémon" in embed.title:
                bidorus_id = embed.description
                pattern = r"`(\d+)`"
                ids = re.findall(pattern, bidorus_id)
                id = ids[0]
                await channel.send(f'<@716390085896962058> evolve {id}')
                await asyncio.sleep(5)
                await channel.send(f'<@716390085896962058> m s --n bidoru')
                
        if "Are you sure you want to buy this" in message:
            await asyncio.sleep(5)
            try:
                click_yes = msg.components[0].children[0]
                custom_id = click_yes.custom_id
                guild_id = str(msg.guild.id)
                session_id = Utils.generate_session_id()
                type = 2
                channel_id = str(msg.channel.id)
                application_id = str(msg.author.id)
                Utils.click_button(config.token, msg.id, custom_id, channel_id, guild_id, application_id, session_id, type)
            except:
                pass
            await asyncio.sleep(5)
            await channel.send('<@716390085896962058> ev q')

        elif "Are you sure you want to **release**" in message:
            await asyncio.sleep(5)
            try:
                click_yes = msg.components[0].children[0]
                custom_id = click_yes.custom_id
                guild_id = str(msg.guild.id)
                session_id = Utils.generate_session_id()
                type = 2
                channel_id = str(msg.channel.id)
                application_id = str(msg.author.id)
                Utils.click_button(config.token, msg.id, custom_id, channel_id, guild_id, application_id, session_id, type)
            except:
                pass
            await asyncio.sleep(5)
            await channel.send('<@716390085896962058> ev q')

        elif "Are you sure you want to cancel your quests" in message:
            await asyncio.sleep(5)
            try:
                click_yes = msg.components[0].children[0]
                custom_id = click_yes.custom_id
                guild_id = str(msg.guild.id)
                session_id = Utils.generate_session_id()
                type = 2
                channel_id = str(msg.channel.id)
                application_id = str(msg.author.id)
                Utils.click_button(config.token, msg.id, custom_id, channel_id, guild_id, application_id, session_id, type)
            except:
                pass
                    
        
        elif "Are you sure you want to list" in message:
            await asyncio.sleep(5)
            try:
                click_yes = msg.components[0].children[0]
                custom_id = click_yes.custom_id
                guild_id = str(msg.guild.id)
                session_id = Utils.generate_session_id()
                type = 2
                channel_id = str(msg.channel.id)
                application_id = str(msg.author.id)
                Utils.click_button(config.token, msg.id, custom_id, channel_id, guild_id, application_id, session_id, type)
                await asyncio.sleep(20)
            except:
                pass
            await asyncio.sleep(5)
            await channel.send('<@716390085896962058> ev q')
        

bot.run(config.token)
