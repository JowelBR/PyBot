import discord
from time import sleep

async def EnviarAyuda(reaction:discord.Reaction, user:discord.member.Member):
    try:
        await user.send(f"hola {user.global_name}")
    except AttributeError:
        return
    
    await user.send("te mostrare una 'documentacion' sobre los comandos")
    
    cont = 3
    while cont > 0:
        sleep(0.8)
        await user.send(cont)
        cont -= 1
    if(cont <= 1):
        sleep(0.5)
        with open("C:/Users/morfa/Desktop/Python/PyBot/BotDiscord/Comandos/Documentation.txt", 'r') as archivo:
            contenido = archivo.read()
            await user.send(contenido)

