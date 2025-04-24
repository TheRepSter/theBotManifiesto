from .logging import LoggingMixin
import discord

class BasicDiscordClient(LoggingMixin):
	logging_suffix = "Discord"
	def __init__(self, token):
		self.__token = token
		self.bot = discord.Bot()

	def run(self):
		self.bot.run(self.__token)
		self.logger.info("Running Discord bot.")

	def stop(self):
		pass
