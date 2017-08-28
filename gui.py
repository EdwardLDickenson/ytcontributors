from ui import *

window.resize(1024, 768)

widget.setWindowTitle("YouTube Comment Analytics");
widget.resize(1024, 768)

mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu("File")

exitMenuButton.setShortcut("Ctrl+Q")
exitMenuButton.setStatusTip("Exit application")
exitMenuButton.triggered.connect(widget.close)
fileMenu.addAction(exitMenuButton)

leftCommentList.setReadOnly(True)
leftCommentList.resize(520, 360)
leftCommentList.move(0, 20)

commentsLength.setText(commentsLengthPrefix)
commentsLength.resize(commentsLength.sizeHint())
commentsLength.move(0, 380)

idLabel.setText("Enter the ID of the desired video");
idLabel.resize(idLabel.sizeHint());
idLabel.move(0, 415);

idInput.move(200, 400)

getButton.setToolTip("Get the comments entered video");
getButton.clicked.connect(appendComments);
getButton.resize(getButton.sizeHint());
getButton.move(0, 430);

displayButton.setToolTip("Display the list of comments")
displayButton.clicked.connect(displayComments)
displayButton.resize(displayButton.sizeHint())
displayButton.move(110, 430)

clearButton.setToolTip("Dump current list of comments and clear display")
clearButton.clicked.connect(clearDisplay)
clearButton.resize(clearButton.sizeHint())
clearButton.move(240, 430)

queryLabel.setText("Enter a search string")
queryLabel.resize(queryLabel.sizeHint())
queryLabel.move(0, 475)

searchQuery.move(130, 460)

queryButton.setToolTip("Search comments by string")
queryButton.clicked.connect(getSearchQuery)
queryButton.resize(queryButton.sizeHint())
queryButton.move(0, 490)

filteredLeftLength.setText(commentsLengthPrefix)
filteredLeftLength.resize(filteredLeftLength.sizeHint())
filteredLeftLength.move(300, 470)

filteredLeft.setReadOnly(True)
filteredLeft.resize(520, 180)
filteredLeft.move(0, 520)

widget.show()
sys.exit(main.exec_());


#	Really needs a load bar for longer videos
