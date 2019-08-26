import asyncio
import datetime

from discord.ext import commands

from bot.reference import *
import bot.reference as ref


class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="clear")
    async def clear(self, ctx, number=5):
        number = int(number)  # Converting the amount of messages to delete to an integer
        await ctx.channel.purge(limit=number)
        temp = await ctx.send(f"**@everyone :white_check_mark: {number} message(s) Cleared!**")
        print(f":wastebasket: Cleared {number} messages from channel: {ctx.channel}")
        await asyncio.sleep(2.5)
        await temp.delete()

    @commands.command(pass_context=True, name="prefix")
    async def prefix(self, ctx, prefix=None):
        if prefix is None:
            await ctx.send(f"**Current prefix is '{os.environ['BOT_PREFIX']}'")
            return
        try:
            os.environ["BOT_PREFIX"] = prefix
            ref.BOT_PREFIX = prefix
            self.bot.command_prefix = prefix
            await ctx.send(f"**Set prefix to '{prefix}'**")
            print(f"**Command prefix is now '{prefix}'**")
        except Exception as e:
            print("Failed to set prefix")
            print(e)

    @commands.command(name="info", pass_context=True, alias=['status'])
    async def info(self, ctx):
        current_datetime = datetime.datetime.now()
        time = current_datetime.time()
        date = current_datetime.date()
        user = self.bot.user.display_name
        info = await ctx.send(f"```{user} {RELEASE_VERSION}\n(C Nathan Estrada 2019\nServer Time: {time}\n"
                              f"Server Date: {date}```")

        await asyncio.sleep(5)
        await info.delete()
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Util(bot))
