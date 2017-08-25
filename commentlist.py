class commentList:
	commentMap = {}	#	Yes, commentList is a misnomer

	def __init__(self, list={}):
		self.commentMap = list

	def getComments(self):
		return self.commentMap.keys()

	def setComments(self, list):
		self.commentMap = list
