class SameTweetException(BaseException):
	def __init__(self, message):
		self.message = message
