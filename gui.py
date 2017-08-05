import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

from main import *

def getVideoID():
	id = idInput.text()

	if id == "":
		id = "wwyXQn9g40I"	#	Allman Brother's Blue Sky

	return id;

def displayComments():
	if len(comments) == 0:
		return;

	leftCommentList.setText(formatCommentsForDisplay(comments));

def appendComments():
	getByID(getVideoID());
	commentsLength.setText(commentsLengthPrefix + str(len(comments)));
	commentsLength.resize(commentsLength.sizeHint());
	commentsLength.move(0, 430);

def clearComments():
	del comments[:]
	del replies[:]
	del authors[:]

def clearDisplay():
	clearComments()

	leftCommentList.setText("")
	commentsLength.setText(commentsLengthPrefix)

main = QtGui.QApplication(sys.argv);
window = QtGui.QWidget();
widget = QWidget(window);

window.resize(1024, 768);
window.setWindowTitle("YouTube Comment Analytics");

idInput = QLineEdit(widget);
idInput.move(0, 400);

commentsLengthPrefix = "Number Of Comments: "
commentsLength = QLabel(widget);
commentsLength.setText(commentsLengthPrefix);
commentsLength.resize(commentsLength.sizeHint());
commentsLength.move(0, 430);

getButton = QPushButton("Get Comments", widget);
getButton.setToolTip("Get the comments entered video");
getButton.clicked.connect(appendComments);
getButton.resize(getButton.sizeHint());
getButton.move(0, 450);

displayButton = QPushButton("Display Comments", widget);
displayButton.setToolTip("Display the list of comments");
displayButton.clicked.connect(displayComments);
displayButton.resize(displayButton.sizeHint());
displayButton.move(110, 450);

clearButton = QPushButton("Clear Comment List", widget);
clearButton.setToolTip("Dump current list of comments and clear display")
clearButton.clicked.connect(clearDisplay)
clearButton.resize(clearButton.sizeHint())
clearButton.move(240, 450);

leftCommentList = QTextEdit(widget);
leftCommentList.setReadOnly(True);
leftCommentList.resize(520, 364);
leftCommentList.move(0, 0);

window.show();
sys.exit(main.exec_());
