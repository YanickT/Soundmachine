import discord
from discord.ext import commands


with open("token.txt", "r") as doc:
    TOKEN = doc.readlines()[0]


STATUS = None
CHANNEL = None
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    global STATUS
    STATUS = True


@client.command(name='join', help='Tells the bot to join the voice channel the writer is in')
async def join(ctx):
    channel = ctx.author.voice.channel
    global CHANNEL
    CHANNEL = await channel.connect()


@client.command(name='leave', help='Tells the bot to leave the current voice channel')
async def leave(ctx):
    if is_connected():
        await CHANNEL.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


def play(filename):
    audio = discord.FFmpegPCMAudio(executable="ffmpeg", source=filename)
    CHANNEL.play(audio)


def is_connected():
    if CHANNEL is not None and CHANNEL.is_connected:
        return True
    return False