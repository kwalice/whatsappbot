import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '-', intents=intents)




@client.event
async def on_ready():
    print("Bot online)")
    print("------------------------------")
    await client.change_presence(activity=discord.Game('WhatsApp | -help'))

@client.command()
async def troll(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/826953338696106014/841613197412794398/jWr67J8.png")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=100):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= " "):
    await member.send("Voce foi espuco do serve lollllll" +reason)
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= " "):
    await member.send("banido xD:" +reason)
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Canal bloqueado')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Canal desbloqueado')



client.run('your_token_here')
