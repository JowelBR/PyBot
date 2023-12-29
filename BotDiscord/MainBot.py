import Constantes as Constantes
import discord as DC
import Comandos.Sincronizacion, Comandos.Encuesta, Comandos.Ayuda
from discord.ext import commands

bot = commands.Bot(command_prefix=Constantes.PREFIX, intents=DC.Intents.all())

@bot.command(name="ayuda")
async def muestraReacion(ctx:commands.Context):
    mensaje = await ctx.send(f"haz activado el comando de ayuda, reacciona al mensaje para ayudarte")
    await mensaje.add_reaction('✅')

@bot.event
async def on_reaction_add(reaction:DC.Reaction, user:DC.Member):
    try:
        if reaction.emoji == '✅': await Comandos.Ayuda.EnviarAyuda(reaction, user)
    except AttributeError: return

@bot.command(name="asincro")
async def sincronizacionComando(ctx): await Comandos.Sincronizacion.sincro(ctx, bot)

@bot.command(name="votacion")
async def EncuestaComando(ctx:commands.context.Context, pregunta:str, *opciones): 
    await Comandos.Encuesta.Encuesta(ctx, pregunta, *opciones)

bot.run("MTE4ODMxNDIzODY0OTkwMTExNg.G1We4S.phJ8dQ3N8cca3iHMAi9fxbDSwhD6mjC9x0QET0")