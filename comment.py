class Comment:
	commentText = "";
	commentLikes = 0;
	commentAuthor = "";
	commentAuthorID = "";
	commentTimeStamp = "";	#	Probably should not be a string

	def __init__(self, likes=0, text="", author="", id="", time=""):
		self.commentText = text;
		self.commentLikes = likes;
		self.commentAuthor = author;
		self.commentAuthorID = id;
		self.commentTimeStamp = time;

	def getText(self):
		return self.commentText;

	def getLikes(self):
		return self.commentLikes;

	def getAuthor(self):
		return self.commentAuthor;

	def getID(self):
		return self.commentAuthorID;

	def getTime(self):
		return self.commentTimeStamp;

	#	Should really impose a type system on the user defined files.
	#	And in the constructor

	def setText(self, newText):
		self.commentText = newText;

	def setLikes(self, newLikes):
		self.commentLikes = newLikes;

	def setAuthor(self, newAuthor):
		self.commentAuthor = newAuthor;

	def setId(self, newID):
		self.commentAuthorID = newID;

	def setTime(self, newTime):
		self.commentTimeStamp = newTime;
