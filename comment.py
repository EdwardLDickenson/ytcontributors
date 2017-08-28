class Comment:
	commentId = ""
	commentText = "";
	commentLikes = 0;
	commentAuthor = "";
	commentAuthorId = "";
	commentTimeStamp = "";	#	Probably should not be a string
	commentReplyCount = 0;

	def __init__(self, likes=0, text="", authorId="", author="", id="", time="", replyCount=0):
		self.commentId = id;
		self.commentText = text;
		self.commentLikes = likes;
		self.commentAuthor = author;
		self.commentAuthorId = authorId
		self.commentTimeStamp = time;
		self.commentReplyCount = replyCount

	#	setByDict still needs to be defined even if the constructor accepts the same input
	def parseComment(self, dict):
		if str(type(dict)) != "<type 'dict'>":
			return

		if "id" in dict.keys():
			self.setId(dict["id"])

		if "snippet" in dict.keys():
			dict = dict["snippet"]["topLevelComment"]["snippet"]

		dictKeys = dict.keys()

		if "textOriginal" in dictKeys:
			pass

		if "textDisplay" in dictKeys:
			self.setText(dict["textDisplay"])

		if "authorDisplayName" in dictKeys:
			self.setAuthor(dict["authorDisplayName"])

		if "likeCount" in dictKeys:
			self.setLikes(dict["likeCount"])

		if "publishedAt" in dictKeys:
			self.setTime(dict["publishedAt"])

		if "channelId" in dictKeys:
			pass

		if "updatedAt" in dictKeys:
			pass

		if "videoId" in dictKeys:
			pass

		if "parentId" in dictKeys:
			pass

		if "canRate" in dictKeys:
			pass

		if "viewerRating" in dictKeys:
			pass

		if "moderationStatus" in dictKeys:
			pass

		if "textOriginal" in dictKeys:
			pass

	#	Accesesors
	def getText(self):
		return self.commentText;

	def getLikes(self):
		return self.commentLikes;

	def getAuthor(self):
		return self.commentAuthor;

	def getId(self):
		return self.commentId;

	def getTime(self):
		return self.commentTimeStamp;

	def getReplyCount(self):
		return self.commentReplyCount

	def getAuthorId(self):
		return self.commentAuthorId

	#	Mutators
	def setText(self, newText):
		self.commentText = newText;

	def setLikes(self, newLikes):
		if str(type(newLikes)) == "<type 'int'>":
			self.commentLikes = newLikes;

	def setAuthor(self, newAuthor):
		self.commentAuthor = newAuthor;

	def setId(self, newId):
		self.commentId = newId

	def setTime(self, newTime):
		self.commentTimeStamp = newTime;

	def setReplyCount(self, newCount):
		if str(type(newCount)) == "<type 'int'>":
			self.commentReplyCount = newCount

	def setAuthorId(self, newId):
		self.commentAuthorId = newId

	#	Utility
	def toString(self):
		result = "<"

		result = result + self.commentText + ","
		result = result + str(self.commentLikes) + ","
		result = result + self.commentAuthor + ","
		result = result + self.commentId + ","
		result = result + self.commentTimeStamp + ","
		result = result + str(self.commentReplyCount) + ","
		result = result + self.commentAuthorId

		result = result + ">"

		return result

	def format(self, index):
		#	Index does not strictly have to be a number.  
		result = "" + str(index) + ") "
		result = result + self.commentText
		result = result + "\n"

		return result

#	Most of the mutators will probably go unused, but it's nice to have them anway
