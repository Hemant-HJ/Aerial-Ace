from discord.ext import commands

import config
from cog_helpers import pokedex_helper
from cog_helpers import general_helper

class PokeDex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def dex(self, ctx, poke):

        try:
            poke_data = await pokedex_helper.get_poke_by_id(poke)
        except:
            reply = await general_helper.get_info_embd("Pokemon not found", f"Dex entry for id : `{poke}` was not found in the pokedex.\n Most uncommon ids follow this format : \n```-aa dex gallade-mega\n-aa dex meowstic-female\n-aa dex deoxys-defense\n-aa dex necrozma-dawn\n-aa dex calyrex-shadow-rider\n-aa dex cinderace-gmax```\nIf you still think this pokemon is missing, report it at official server", config.ERROR_COLOR)
            await ctx.send(embed=reply)
            return

        reply = await pokedex_helper.get_dex_entry_embed(poke_data)

        await ctx.send(embed=reply)

    @dex.error
    async def dex_handler(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            reply = await general_helper.get_info_embd(title="Error!!", desc="Please provide a `Pokemon_Name` or `Pokemon_ID` as a parameter", footer="Try [dex necrozma-dawn", color=config.ERROR_COLOR)
            await ctx.reply(embed=reply)
        else:
            await ctx.reply(error)

    @commands.guild_only()
    @commands.command(name="random_poke", aliases=["rp"])
    async def random_poke(self, ctx):
        poke_data = await pokedex_helper.get_random_poke()
        reply = await pokedex_helper.get_random_pokemon_embed(poke_data)

        await ctx.send(embed=reply)

def setup(bot):
    bot.add_cog(PokeDex(bot))