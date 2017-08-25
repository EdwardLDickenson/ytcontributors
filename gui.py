from ui import *

#main = QtGui.QApplication(sys.argv)

#window = QtGui.QWidget()
window.resize(1024, 768)

#widget = QMainWindow()
widget.setWindowTitle("YouTube Comment Analytics");
widget.resize(1024, 768)

#mainMenu = widget.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu("File")

#exitMenuButton = QAction("Exit", widget)
exitMenuButton.setShortcut("Ctrl+Q")
exitMenuButton.setStatusTip("Exit application")
exitMenuButton.triggered.connect(widget.close)
fileMenu.addAction(exitMenuButton)

#leftCommentList = QTextEdit(widget)
leftCommentList.setReadOnly(True)
leftCommentList.resize(520, 360)
leftCommentList.move(0, 20)

#commentsLengthPrefix = "Number Of Comments: "
#commentsLength = QLabel(widget)
commentsLength.setText(commentsLengthPrefix)
commentsLength.resize(commentsLength.sizeHint())
commentsLength.move(0, 380)

#idLabel = QLabel(widget)
idLabel.setText("Enter the ID of the desired video");
idLabel.resize(idLabel.sizeHint());
idLabel.move(0, 415);

#idInput = QLineEdit(widget)
idInput.move(200, 400)

#getButton = QPushButton("Get Comments", widget);
getButton.setToolTip("Get the comments entered video");
getButton.clicked.connect(appendComments);
getButton.resize(getButton.sizeHint());
getButton.move(0, 430);

#displayButton = QPushButton("Display Comments", widget)
displayButton.setToolTip("Display the list of comments")
displayButton.clicked.connect(displayComments)
displayButton.resize(displayButton.sizeHint())
displayButton.move(110, 430)

#clearButton = QPushButton("Clear Comment List", widget);
clearButton.setToolTip("Dump current list of comments and clear display")
clearButton.clicked.connect(clearDisplay)
clearButton.resize(clearButton.sizeHint())
clearButton.move(240, 430)

#queryLabel = QLabel(widget)
queryLabel.setText("Enter a search string")
queryLabel.resize(queryLabel.sizeHint())
queryLabel.move(0, 475)

#searchQuery = QLineEdit(widget)
searchQuery.move(130, 460)

#queryButton = QPushButton("Search", widget)
queryButton.setToolTip("Search comments by string")
queryButton.clicked.connect(getSearchQuery)
queryButton.resize(queryButton.sizeHint())
queryButton.move(0, 490)

widget.show()
sys.exit(main.exec_());


#	Really needs a load bar for longer videos
