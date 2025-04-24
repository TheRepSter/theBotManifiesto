from .logging import LoggingMixin
from abc import ABC, abstractmethod

class AbstractBot(ABC, LoggingMixin):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def stop(self):
		pass
