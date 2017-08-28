class commentList:
	commentMap = {}	#	Yes, commentList is a misnomer

	def __init__(self, list={}):
		self.commentMap = list

	def getComments(self):
		return self.commentMap.keys()

	def setComments(self, list):
		self.commentMap = list

	def getRepliesTo(self, comment):
		#	Test to make sure that comment is comment type
		return self.commentMap[comment]

	def searchString(self, string):
		keys = self.commentMap.keys()
		results = []

		for i in range(len(keys)):
			if string in keys[i].getText():
				results.append(keys[i])

		return results
