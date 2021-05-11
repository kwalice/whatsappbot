import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '-', intents=intents)




@client.event
async def on_ready():
    print("Bot online)")
    print("------------------------------")


@client.command()
async def troll(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/826953338696106014/841613197412794398/jWr67J8.png")

@client.event
async def on_member_join(member):
    guild = client.get_guild(789990023596081152)
    channel = client.get_channel(835995985066197012)
    await channel.send(f'{member.mention} acabou de entrar no servidor!')
    await member.send ("https://cdn.discordapp.com/attachments/824824470694920202/825911029392343107/video0-6.mp4")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=100):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= " Sem motivo definido"):
    await member.send("Voce foi expulso do servidor por:" +reason)
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= " Sem motivo definido"):
    await member.send("Voce foi banido do servidor por:" +reason)
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



client.run('ODQwNzgxMTg5NDEyODE0ODc5.YJdMgA.9UQdJRHqpCqXKxOUUS2cYdQzcKE')
