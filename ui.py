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
commentsLengthPrefix = "Number Of Comments: "
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

def displayComments():
	keys = comments.getComments()
	print(type(keys))
	if len(keys) == 0:
		return

	formattedString = ""

	for i in range(len(keys)):
		formattedString = formattedString + keys[i].format(i)

	leftCommentList.setText(formattedString)

def appendComments():
	commentsOnVideo = getById(getVideoId())
	commentsLength.setText(commentsLengthPrefix + str(len(commentsOnVideo.keys())))
	commentsLength.resize(commentsLength.sizeHint())

	comments.setComments(commentsOnVideo)

def clearDisplay():
	clearComments()

	leftCommentList.setText("")
	commentsLength.setText(commentsLengthPrefix)

def getSearchQuery():
	query = searchQuery.text()
	print(query);
