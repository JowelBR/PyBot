async def sincro(ctx, bot):
    await bot.tree.sync()
    await ctx.send("sincronizado existosamente")