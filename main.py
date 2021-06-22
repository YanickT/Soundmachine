import asyncio
import discord
from discord.ext import commands

with open("token.txt", "r") as doc:
    TOKEN = doc.readlines()[0]

client = commands.Bot(command_prefix='!')
songs = asyncio.Queue()
restart_permanent = asyncio.Event()


@client.event
async def on_ready():
    print("Bot online")


@client.command(name='join', help='Tells the bot to join the voice channel the writer is in')
async def join(ctx):
    channel = ctx.author.voice.channel
    global vc
    vc = await channel.connect()


@client.command(name='leave', help='Tells the bot to leave the current voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def play(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    if voice_channel is None:
        await ctx.send("The bot is not connected to a voice channel.")

    filename = "sounds/creatures/abomination_cat.flac"
    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
    await ctx.send('GO')



def toggle_next():
    client.loop.call_soon_threadsafe(restart_permanent.set)


client.run(TOKEN)