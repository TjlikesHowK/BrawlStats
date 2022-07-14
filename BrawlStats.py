import os
import asyncio
import discord
from discord_components import DiscordComponents, Button, ButtonStyle
from BS_config import bot_token, prefix
from discord.ext import commands

bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('Bot connected')

@bot.command()
async def load(ctx, extensions):
	bot.load_extension(f"cogs.{extensions}")

	await ctx.send("loaded")

@bot.command()
async def unload(ctx, extensions):
	bot.unload_extension(f"cogs.{extensions}")

	await ctx.send("unloaded")

async def reload(ctx, extensions):
	bot.unload_extension(f"cogs.{extensions}")
	bot.load_extension(f"cogs.{extensions}")

	await ctx.send("reloaded")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(bot_token)