from .logging import LoggingMixin
from praw import Reddit

class BasicRedditClient(LoggingMixin):
	logging_suffix = "Reddit"
	def __init__(self, client_id, client_secret, user_agent):
		self.reddit = Reddit(client_id=client_id,
								  client_secret=client_secret,
								  user_agent=user_agent)

	def run(self):
		self.logger.info("Running Reddit Bot.")

	def stop(self):
		pass
