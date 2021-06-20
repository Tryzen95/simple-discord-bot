import discord
import asyncio
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix= '/')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('TRYZEN-ROLEPLAY'))
    print('bot ist ready')

@client.event
async def on_member_join(member):
    print(f'{member} Ist Gejoint.')

@client.event
async def on_member_remove(member):
    print(f'{member} Ist Runtergegangen.')

@client.event
async def on_role_remove(role):
    print(f'{role} entfernt')

@client.command()
async def command(ctx):
    await ctx.send('Hier die Commands /info, /tastb, /perm')

@client.command()
async def info(ctx):
    await ctx.send('Wo zu brauchst du Infos wenn du Hilfe Benötigst öffne doch gerne ein Ticket im Ticket Channel')

@client.command()
async def tastb(ctx):
    await ctx.send('Du suchst die Tasten belegung vom Server? Hier Bitte Schön https://forum.tryzenrp.de/forum/thread/52-tasten-belegung/')

@client.command()
async def perm(ctx):
    await ctx.send('Du Zockst gerne bei uns? und willst dein Freund auch rauf holen? dann hier ein Link zum einladen https://discord.gg/cGtmH5kuXG')

@client.command()
async def tsip(ctx):
    await ctx.send('Hier einmal unser TS IP  ts.tryzenrp.de')

@client.command()
async def forum(ctx):
    await ctx.send('https://forum.tryzenrp.de/')

@client.command()
async def twitch(ctx):
    await ctx.send('Hier die Aktuellen Twitch Partner https://forum.tryzenrp.de/ha-streaming-partner/')

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run('ODU1Nzg4NjA5OTQzNjMzOTYy.YM3lQA.aTN4-z8CkjkA-G56y5c994uhKJQ')