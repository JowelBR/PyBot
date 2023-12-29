from discord.ext import commands

async def Encuesta(ctx:commands.context.Context, pregunta:str, *opciones):
    emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
    pregunta = pregunta.replace("_", " ")
    remplazar = lambda x : str(x).replace("_", " ")
    opciones = list(map(remplazar, opciones))
    await ctx.send(f"{pregunta} ?")
    
    for indexL, opcion in zip(range(1, list(opciones).__len__() + 1), list(opciones)):
        mensaje = await ctx.send(f"{indexL}. {opcion}")
    for i in range(list(opciones).__len__()):
        await mensaje.add_reaction(emojis[i])