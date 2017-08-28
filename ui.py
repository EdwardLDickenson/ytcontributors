import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

from main import *
from commentlist import *

main = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
widget = QMainWindow()
mainMenu = widget.menuBar()
exitMenuButton = QAction("Exit", widget)
leftCommentList = QTextEdit(widget)
filteredLeft = QTextEdit(widget)
filteredLeftLength = QLabel()
commentsLengthPrefix = "Number Of Comments: "	#	Not a UI element
commentsLength = QLabel(widget)
idLabel = QLabel(widget)
idInput = QLineEdit(widget)
getButton = QPushButton("Get Comments", widget);
displayButton = QPushButton("Display Comments", widget)
clearButton = QPushButton("Clear Comment List", widget);
queryLabel = QLabel(widget)
searchQuery = QLineEdit(widget)
queryButton = QPushButton("Search", widget)

comments = commentList()

def getVideoId():
	id = idInput.text()

	if id == "":
		id = "wwyXQn9g40I"	#	Allman Brother's Blue Sky

	return id;

#	Needs to be rewritten for an arbitrary display(QTextEdit)
def displayComments():
	keys = comments.getComments()
	if len(keys) == 0:
		return

	formattedString = ""

	for i in range(len(keys)):
		formattedString = formattedString + keys[i].format(i)
		for j in range(len(comments.getRepliesTo(keys[i]))):
			formattedString = formattedString + " " + comments.getRepliesTo(keys[i])[j].format(j)

	leftCommentList.setText(formattedString)

def appendComments():
	commentsOnVideo = getById(getVideoId())
	commentsLength.setText(commentsLengthPrefix + str(len(commentsOnVideo.keys())))
	commentsLength.resize(commentsLength.sizeHint())

	comments.setComments(commentsOnVideo)

#	Needs to be rewritten for an arbitrary display(QTextEdit)
def clearDisplay():
	clearComments()

	leftCommentList.setText("")
	commentsLength.setText(commentsLengthPrefix)

def getSearchQuery():
	query = searchQuery.text()

	results = comments.searchString(query)
	formattedString = ""
	for i in range(len(results)):
		formattedString = formattedString + results[i].format(i)

	filteredLeft.setText("")
	filteredLeft.setText(formattedString)
