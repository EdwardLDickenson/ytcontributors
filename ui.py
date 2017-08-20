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
	getById(getVideoID());
	commentsLength.setText(commentsLengthPrefix + str(len(comments)));
	commentsLength.resize(commentsLength.sizeHint());

def clearDisplay():
	clearComments()

	leftCommentList.setText("")
	commentsLength.setText(commentsLengthPrefix)

def getSearchQuery():
	query = searchQuery.text()
	print(query);
