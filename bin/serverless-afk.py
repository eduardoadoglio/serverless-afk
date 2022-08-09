import os
import sys
import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER_NAME")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", 0))
MY_ID = os.getenv("DISCORD_USER_ID")

client = discord.Client()


@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    current_time = datetime.now()
    if "start" in sys.argv:
        await channel.send("https://bit.ly/3JPmRKk")
    elif "end" in sys.argv:
        await channel.send(
            f"[{current_time.strftime('%d/%m/%Y %H:%M:%S')}] <@{MY_ID}> Terminei o deploy"
        )

    exit()


client.run(TOKEN)
