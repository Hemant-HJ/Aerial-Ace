from discord import Member, ApplicationContext
from discord.ext import commands
from discord.commands import slash_command, Option

from cog_helpers import battle_helper

class BattleSystemSlash(commands.Cog):

    """For viewing battleboard of the server"""

    @slash_command(name="battle-leaderboard", description="View the battle leaderboard of this server")
    async def view_leaderboard(self, ctx : ApplicationContext):

        embd = await battle_helper.get_battle_leaderboard_embed(ctx.guild)

        await ctx.respond(embed=embd)

    """For viewing the battle score"""

    @slash_command(name="battle-score", description="View the battle points of the user")
    async def view_score(self, ctx : ApplicationContext, user : Option(Member, description="View score of which user", required=False, default=None)):

        if user is None:
            user = ctx.author

        reply = await battle_helper.get_battle_score(ctx.guild.id, user)

        await ctx.respond(reply)

    """Remove user from battle board"""

    @slash_command(name="battle-remove", description="Remove user from battle board")
    async def battle_remove(self, ctx : ApplicationContext, user : Option(Member, description="User to remove", required=True)):

        if not ctx.author.guild_permissions.administrator :
            return await ctx.respond("Be Admin when? :/")

        reply = await battle_helper.remove_user_from_battleboard(ctx.guild.id, user)

        await ctx.respond(reply)

def setup(bot : commands.Bot):
    bot.add_cog(BattleSystemSlash())