import emoji
import asyncio
import discord
import brawlstats
from discord_components import DiscordComponents, Button, ButtonStyle
from discord.ext import commands
from BS_config import client_token
from discord.ext import commands

userIcons = {
	28000000: "https://cdn.discordapp.com/attachments/750738794831151155/750740352377421884/latest.png",
	28000001: "https://cdn.discordapp.com/attachments/750738794831151155/750740511802917015/latest.png",
	28000002: "https://cdn.discordapp.com/attachments/750738794831151155/750740666337984572/latest.png",
	28000003: "https://cdn.discordapp.com/attachments/750738794831151155/750745094721765537/latest.png",
	28000004: "https://cdn.discordapp.com/attachments/750738794831151155/750745064443084961/latest.png",
	28000005: "https://cdn.discordapp.com/attachments/750738794831151155/750745008939991091/latest.png",
	28000006: "https://cdn.discordapp.com/attachments/750738794831151155/750745029357600798/latest.png",
	28000007: "https://cdn.discordapp.com/attachments/750738794831151155/750745079995433050/latest.png",
	28000008: "https://cdn.discordapp.com/attachments/750738794831151155/750744845206945822/latest.png",
	28000009: "https://cdn.discordapp.com/attachments/750738794831151155/750744599676452874/latest.png",
	28000010: "https://cdn.discordapp.com/attachments/750738794831151155/750745050866253954/latest.png",
	28000011: "https://cdn.discordapp.com/attachments/750738794831151155/750744518210355290/latest.png",
	28000012: "https://cdn.discordapp.com/attachments/750738794831151155/750744579686400131/latest.png",
	28000013: "https://cdn.discordapp.com/attachments/750738794831151155/750744557444136990/latest.png",
	28000014: "https://cdn.discordapp.com/attachments/750738794831151155/750744078244773888/latest.png",
	28000015: "https://cdn.discordapp.com/attachments/750738794831151155/750744825715884144/latest.png",
	28000016: "https://cdn.discordapp.com/attachments/750738794831151155/750743698265866371/latest.png",
	28000017: "https://cdn.discordapp.com/attachments/750738794831151155/750745658054541492/latest.png",
	28000018: "https://cdn.discordapp.com/attachments/750738794831151155/750744237875920906/latest.png",
	28000019: "https://cdn.discordapp.com/attachments/750738794831151155/750741535452037128/latest.png",
	28000020: "https://cdn.discordapp.com/attachments/750738794831151155/750741667270754405/latest.png",
	28000021: "https://cdn.discordapp.com/attachments/750738794831151155/750742223737585734/latest.png",
	28000022: "https://cdn.discordapp.com/attachments/750738794831151155/750742522644398081/latest.png",
	28000023: "https://cdn.discordapp.com/attachments/750738794831151155/750743047511474217/latest.png",
	28000024: "https://cdn.discordapp.com/attachments/750738794831151155/750743071158829176/latest.png",
	28000025: "https://cdn.discordapp.com/attachments/750738794831151155/750743100002926648/latest.png",
	28000026: "https://cdn.discordapp.com/attachments/750738794831151155/750743128587370606/latest.png",
	28000027: "https://cdn.discordapp.com/attachments/750738794831151155/750743213421363311/latest.png",
	28000028: "https://cdn.discordapp.com/attachments/750738794831151155/750744162579775528/latest.png",
	28000029: "https://cdn.discordapp.com/attachments/750738794831151155/750743917183369286/latest.png",
	28000030: "https://cdn.discordapp.com/attachments/750738794831151155/750743231926370455/latest.png",
	28000031: "https://cdn.discordapp.com/attachments/750738794831151155/750743243335008368/latest.png",
	28000032: "https://cdn.discordapp.com/attachments/750738794831151155/750743272456192140/latest.png",
	28000033: "https://cdn.discordapp.com/attachments/750738794831151155/750743289627672586/latest.png",
	28000034: "https://cdn.discordapp.com/attachments/750738794831151155/750744306272436234/latest.png",
	28000035: "https://cdn.discordapp.com/attachments/750738794831151155/750744290162114560/latest.png",
	28000036: "https://cdn.discordapp.com/attachments/750738794831151155/750744147165446204/latest.png",
	28000037: "https://cdn.discordapp.com/attachments/750738794831151155/750743674622705764/latest.png",
	28000038: "https://cdn.discordapp.com/attachments/750738794831151155/750743899298857160/latest.png",
	28000039: "https://cdn.discordapp.com/attachments/750738794831151155/750744273007411232/latest.png",
	28000040: "https://cdn.discordapp.com/attachments/750738794831151155/750744541371433060/latest.png",
	28000041: "https://cdn.discordapp.com/attachments/750738794831151155/750744121433391164/latest.png",
	28000042: "https://cdn.discordapp.com/attachments/750738794831151155/750744811190878318/latest.png",
	28000043: "https://cdn.discordapp.com/attachments/750738794831151155/750744796536242226/latest.png",
	28000044: "https://cdn.discordapp.com/attachments/750738794831151155/750743656889319535/latest.png",
	28000045: "https://cdn.discordapp.com/attachments/750738794831151155/750744780253823146/latest.png",
	28000046: "https://cdn.discordapp.com/attachments/750738794831151155/750744096485802044/latest.png",
	28000047: "https://cdn.discordapp.com/attachments/750738794831151155/750743878809682001/latest.png",
	28000048: "https://cdn.discordapp.com/attachments/750738794831151155/750743863731290123/latest.png",
	28000049: "https://cdn.discordapp.com/attachments/750738794831151155/750744256653688892/latest.png",
	28000050: "https://cdn.discordapp.com/attachments/750738794831151155/750743846731776041/latest.png",
	28000051: "https://cdn.discordapp.com/attachments/750738794831151155/750743641806471248/latest.png",
	28000052: "https://cdn.discordapp.com/attachments/750738794831151155/750743621510103173/latest.png",
	28000053: "https://cdn.discordapp.com/attachments/750738794831151155/750741932254298283/latest.png",
	28000054: "https://static.wikia.nocookie.net/brawlstars/images/e/ee/Colette1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015022",

	28000055: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000056: "https://static.wikia.nocookie.net/brawlstars/images/d/d2/Lou1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015044",

	28000057: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000058: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000059: "https://static.wikia.nocookie.net/brawlstars/images/5/5f/Colonel_Ruffs1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015103",
	28000061: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000061: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000062: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000063: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000064: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000065: "https://static.wikia.nocookie.net/brawlstars/images/d/dd/Belle1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015118",

	28000066: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000067: "https://static.wikia.nocookie.net/brawlstars/images/b/be/Buzz1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015140",

	28000068: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000069: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000070: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000071: "https://static.wikia.nocookie.net/brawlstars/images/f/fb/Ash1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015200",
	28000072: "https://static.wikia.nocookie.net/brawlstars/images/3/3b/Power_League_S4-Silver.png/revision/latest/scale-to-width-down/100?cb=20210829002143",

	28000073: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000074: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000075: "https://static.wikia.nocookie.net/brawlstars/images/9/9e/Lola1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015217",
	28000076: "https://static.wikia.nocookie.net/brawlstars/images/8/8f/Power_League_S5-Silver.png/revision/latest/scale-to-width-down/100?cb=20211110085401",

	28000077: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000078: "https://static.wikia.nocookie.net/brawlstars/images/a/a3/Power_League_S6-Silver.png/revision/latest/scale-to-width-down/100?cb=20220117103102",
	28000079: "https://static.wikia.nocookie.net/brawlstars/images/c/c5/Power_League_S6-Gold.png/revision/latest/scale-to-width-down/100?cb=20220117103114",

	28000080: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000081: "https://static.wikia.nocookie.net/brawlstars/images/f/fb/Fang1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015244",
	28000082: "https://static.wikia.nocookie.net/brawlstars/images/0/02/Eve1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220429015302",

	28000083: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000084: "https://static.wikia.nocookie.net/brawlstars/images/5/5f/Power_League_S7-Gold.png/revision/latest/scale-to-width-down/100?cb=20220307085659",
	28000085: "https://static.wikia.nocookie.net/brawlstars/images/5/56/Janet1-pfp.png/revision/latest/scale-to-width-down/100?cb=20220503022810",

	28000086: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000087: "https://static.wikia.nocookie.net/brawlstars/images/3/33/Power_League_S8-Silver.png/revision/latest/scale-to-width-down/100?cb=20220429213311",
	28000088: "https://static.wikia.nocookie.net/brawlstars/images/7/70/Power_League_S8-Gold.png/revision/latest/scale-to-width-down/100?cb=20220429213327",

	28000089: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000090: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000091: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000092: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000093: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000094: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000095: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000096: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000097: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000098: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000099: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000100: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000101: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000102: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000103: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000104: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000105: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000106: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000107: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000108: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000109: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000110: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000111: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000112: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000113: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###
	28000114: "https://i.pinimg.com/originals/d3/f6/31/d3f631cffe267432bfff6e9ddadb3ea7.png", ###

	28000115: "https://static.wikia.nocookie.net/brawlstars/images/e/e6/Deep_Sea_Brawl-pfp.png/revision/latest/scale-to-width-down/100?cb=20220629093106"
}

leagueIcons = {
	"wood": "https://static.wikia.nocookie.net/brawlstars/images/c/c3/League1.png/revision/latest/scale-to-width-down/60?cb=20200204150722&path-prefix=ru",
	"bronze": "https://static.wikia.nocookie.net/brawlstars/images/3/3a/League2.png/revision/latest/scale-to-width-down/60?cb=20200204150828&path-prefix=ru",
	"silver": "https://static.wikia.nocookie.net/brawlstars/images/c/cc/League3.png/revision/latest/scale-to-width-down/60?cb=20200204151021&path-prefix=ru",
	"gold": "https://static.wikia.nocookie.net/brawlstars/images/8/8d/League4.png/revision/latest/scale-to-width-down/60?cb=20200204151141&path-prefix=ru",
	"diamond": "https://static.wikia.nocookie.net/brawlstars/images/3/36/League5.png/revision/latest/scale-to-width-down/60?cb=20200204151307&path-prefix=ru",
	"amethyst": "https://static.wikia.nocookie.net/brawlstars/images/b/bd/League6n.png/revision/latest/scale-to-width-down/60?cb=20210317151436&path-prefix=ru",
	"ruby": "https://static.wikia.nocookie.net/brawlstars/images/9/97/League7n.png/revision/latest/scale-to-width-down/60?cb=20210317151801&path-prefix=ru",
	"star": "https://static.wikia.nocookie.net/brawlstars/images/b/b2/League8.png/revision/latest/scale-to-width-down/60?cb=20200204151852&path-prefix=ru",
	"hyacin": "https://static.wikia.nocookie.net/brawlstars/images/1/16/League9.png/revision/latest/scale-to-width-down/60?cb=20200703110109&path-prefix=ru",
	"sugulit": "https://static.wikia.nocookie.net/brawlstars/images/b/be/League10.png/revision/latest/scale-to-width-down/60?cb=20200802164337&path-prefix=ru",
	"purple": "https://static.wikia.nocookie.net/brawlstars/images/1/18/League11.png/revision/latest/scale-to-width-down/60?cb=20200802164222&path-prefix=ru"
}

class BrawlStars(commands.Cog, name='Brawl Stars'):
	def __init__(self, bot):
		self.bot = bot
		self.client = brawlstats.Client(client_token, is_async = True)

	@commands.command()
	async def brawl(self, ctx, tag: str):
		try:
			star = emoji.emojize(":star:")
			green = emoji.emojize(":green_square:")
			black = emoji.emojize(":black_large_square:")

			player = await self.client.get_profile(tag)

			idUserIcon = player.icon.id
			idRoborumble = player.bestRoboRumbleTime

			isClub = False

			if len(player.club) != 0:
				isClub = True

			curTrophies = player.trophies
			userLvl = player.expLevel
			lvlBar = userLvl * 10 + 30
			minExp = (40 + lvlBar - 10)/2 * (userLvl - 1) - 100
			curExp = player.expPoints - 100
			maxExp = (40 + lvlBar)/2 * userLvl - 100
			pointExp = (110 * (curExp - minExp)) / lvlBar
			roborumble = "None"
			league = "wood"
			bar = ""

			for point in range(0, 110, 10):
				if point < pointExp:
					bar += green
				elif point > pointExp:
					bar += black

			if curTrophies >= 50000:
				league = "purple"
			elif curTrophies >= 30000:
				league = "sugulit"
			elif curTrophies >= 16000:
				league = "hyacin"
			elif curTrophies >= 10000:
				league = "star"
			elif curTrophies >= 8000:
				league = "ruby"
			elif curTrophies >= 6000:
				league = "amethyst"
			elif curTrophies >= 4000:
				league = "diamond"
			elif curTrophies >= 3000:
				league = "gold"
			elif curTrophies >= 2000:
				league = "silver"
			elif curTrophies >= 1000:
				league = "bronze"

			bestBrawlerTrophies = 0
			bestBrawlername = "SHELLY"

			for brawler in player.brawlers:
				if brawler.trophies > bestBrawlerTrophies:
					bestBrawlerTrophies = brawler.trophies
					bestBrawlername = brawler.name

			if idRoborumble == 1:
				roborumble = "Normal"
			elif idRoborumble == 2:
				roborumble = "Hard"
			elif idRoborumble == 3:
				roborumble = "Expert"
			elif idRoborumble == 4:
				roborumble = "Master"
			elif idRoborumble == 5:
				roborumble = "Insane"
			elif idRoborumble == 6:
				roborumble = "Insane II"
			elif idRoborumble == 7:
				roborumble = "Insane III"
			elif idRoborumble == 8:
				roborumble = "Insane IV"
			elif idRoborumble == 9:
				roborumble = "Insane V"
			elif idRoborumble == 10:
				roborumble = "Insane VI"
			elif idRoborumble == 11:
				roborumble = "Insane VII"
			elif idRoborumble == 12:
				roborumble = "Insane VIII"
			elif idRoborumble == 13:
				roborumble = "Insane IX"
			elif idRoborumble == 14:
				roborumble = "Insane X"
			elif idRoborumble == 15:
				roborumble = "Insane XI"
			elif idRoborumble == 16:
				roborumble = "Insane XII"
			elif idRoborumble == 17:
				roborumble = "Insane XIII"
			elif idRoborumble == 18:
				roborumble = "Insane XIV"
			elif idRoborumble == 19:
				roborumble = "Insane XV"
			elif idRoborumble == 20:
				roborumble = "Insane XVI"

		except brawlstats.RequestError as e:
			return await ctx.send('```\n{}: {}\n```'.format(e.code, e.message))

		embed = discord.Embed(
			title = "",
			description = f"```\n\t\t\t {star}{star}{star}\n{userLvl} {bar} {userLvl + 1}\n\t\t    {int(curExp - minExp)} / {lvlBar}```",
			colour = discord.Colour.from_rgb(75, 0, 130))

		embed.set_author(
			name = f'{player.name} ({player.tag})',
			icon_url = leagueIcons[league])

		if isClub:
			embed.set_footer(
				text = f'{player.club.name} ({player.club.tag})', 
				icon_url = "https://static.wikia.nocookie.net/brawlstars/images/e/e1/Club_League.png/revision/latest/scale-to-width-down/100?cb=20211118005216")

		embed.set_thumbnail(url = userIcons[idUserIcon])

		embed.add_field(name = f'{emoji.emojize(":medal:")}  Trophies:', value = player.trophies, inline = True)
		embed.add_field(name = f'{emoji.emojize(":trophy:")}  Max. trophies:', value = player.highestTrophies, inline = True)
		embed.add_field(name = f'{emoji.emojize(":crown:")}  Best character:', value = f'{bestBrawlername}  |  {bestBrawlerTrophies}', inline = False)
		embed.add_field(name = f'{emoji.emojize(":vs:")} Wins 3 on 3:', value = f"{player['3vs3_victories']}", inline = True)
		embed.add_field(name = f'{emoji.emojize(":muscle:")}  Solo wins:', value = f"{player['soloVictories']}", inline = True)
		embed.add_field(name = f'{emoji.emojize(":skull_crossbones:")}  Duo wins:', value = f"{player['duoVictories']}", inline = True)
		embed.add_field(name = f'{emoji.emojize(":robot:")}  Robo Rumble:', value = f"{roborumble}", inline = True)

		await ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(BrawlStars(bot))