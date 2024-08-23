import discord
import random
from discord.ext import commands
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

bot = commands.Bot(command_prefix = "$", intents=intents)


@bot.event
async def on_ready():
    print(f'iniciamos sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send ("hi")
@bot.command()
async def bye (ctx) :
    await ctx.send ("Hasta pronto: {member.name}")
@bot.command
async def password (ctx):
    await ctx.send (gen_pass (10))
@bot.command()
async def joined_server(ctx, member: discord.Member):
    await ctx.send (f' {member.name} joined this server on {discord.utils.format_dt(member. joined at)}')
@bot.command()
async def joined_discord(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined Discord on {discord.utils.format_dt(member created at)}')


bot.run("token")
