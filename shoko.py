import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(intents = intents, command_prefix = "s.")

@client.event
async def on_ready():
    print('It fucking works now.')

@client.command()
async def listnames(ctx):
    for member in ctx.guild.members:
        await ctx.send(member)

@client.command()
async def promote(ctx, role1 : discord.Role, role2 : discord.Role):
    for member in ctx.guild.members:
        if role1 in member.roles:
            await member.remove_roles(role1)
            await member.add_roles(role2)

@client.command()
async def giverole(ctx, role : discord.Role):
    for member in ctx.guild.members:
        await member.add_roles(role)

@client.command()
async def takerole(ctx, role : discord.Role):
    for member in ctx.guild.members:
        await member.remove_roles(role)

@client.command()
async def test(ctx, role1, role2):
    await ctx.send('you passed {} and {}'.format(role1, role2))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*100)}ms')

client.run('')

