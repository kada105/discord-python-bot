import discord
import asyncio

from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
	print('The Bot is ready')


@client.command(pass_context=True)
async def dakhi(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="k.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')

@client.command(pass_context=True)
async def kada(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="d.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')

@client.command(pass_context=True)
async def ikbal(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="i.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')


@client.command(pass_context=True)
async def hichem1(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="h1.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')

@client.command(pass_context=True)
async def hichem2(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="h2.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')


@client.command(pass_context=True)
async def anis(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="a.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')


@client.command(pass_context=True)
async def okba(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio(executable=r"C:/ffmpeg/bin/ffmpeg.exe", source="o.mp3")
        player = voice.play(source, after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await ctx.guild.voice_client.disconnect()
        print('bot in vc')

@client.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('I m not in voice channel')







client.run("MTA1NzAzNzE5NjE1MjAxNzAwNw.G56NSb.cSYw_glgyOqb4lKJ8fssHkmEknfBbP3r085Pfg")
