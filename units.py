#	Import YouTube API and whatever API wrappers are being used
from getcomments import *
from main import *
from ui import *
from commentlist import *

#	Import internal methods and structures
from comment import *

log = open("units.csv", "w");

def generateErrorMessage(message, expected, result):
	log.write(message + "\n");
	log.write("Expected: " + str(expected) + "\n");
	log.write("But got: " + str(result) + "\n");

def testCommentClass():
	empty = Comment();

	result = True;

	if empty.getText() != "":
		log.write("getText failed on an empty comment constructor\n");
		result = False;

	if empty.getLikes() != 0:
		log.write("getLikes failed on an empty comment constructor\n");
		result = False;

	if empty.getReplyCount() != 0:
		log.write("getReplyCount failed on an empty comment constructor")
		result = False

	if empty.getAuthor() != "":
		log.write("getAuthor failed on an empty comment constructor\n");
		result = False;

	if empty.getId() != "":
		log.write("getID failed on an empty comment constructor\n");
		result = False;

	if empty.getTime() != "":
		log.write("getTime failed on an empty comment constructor\n");
		result = False;

	if empty.getAuthorId() != "":
		log.write("getAuthorId failed on an empoty comment constructor")

	testString = "This was formerly blank"
	empty.setText(testString);
	if empty.getText() != testString:
		generateErrorMessage("setText failed on non-empty test string", testString, empty.getText());
		result = False;

	#	Most of these fields have illegal types which should be checked
	testInteger = 123;
	empty.setLikes(testInteger);
	if empty.getLikes() != testInteger:
		generateErrorMessage("setLikes failed on non-zero integer", testInteger, empty.getLikes());
		result = False;

	testCount = 321
	empty.setReplyCount(testCount)
	if empty.getReplyCount() != testCount:
		generateErrorMessage("setReplyCount failed on non-zero integer")
		result = False

	empty.setLikes(testString)
	if empty.getLikes() != testInteger:
		generateErrorMessage("setLikes failed on non-integer type", testInteger, empty.getLikes())
		result = False

	empty.setReplyCount(testString)
	if empty.getReplyCount() != testCount:
		generateErrorMessage("setReplyCount failed on non-integer type", testCount, empty.getReplyCount())
		result = False

	testAuthor = "There no real author for this";
	empty.setAuthor(testAuthor);
	if empty.getAuthor() != testAuthor:
		generateErrorMessage("setAuthor failed on non-empty string", testAuthor, empty.getAuthor());
		result = False;

	testId = "ID is probably alpha numeric123"
	empty.setId(testId);
	if empty.getId() != testId:
		generateErrorMessage("setId failed on non-empty string", testId, empty.getId());
		result = False

	testTime = "also alphanumeric123"
	empty.setTime(testTime)
	if empty.getTime() != testTime:
		generateErrorMessage("setTime failed on non-empty string", testTime, empty.getTime())
		result = False

	testAuthorId = "This is the test author id 4321"
	empty.setAuthorId(testAuthorId)
	if empty.getAuthorId() != testAuthorId:
		generateErrorMessage("setAuthorId failed on a non-empty string", testAuthorId, empty.getAuthorId())

	constructed = Comment(text=testString, likes=testInteger, author=testAuthor, replyCount=testCount, time=testTime, authorId=testAuthorId, id=testId)

	if constructed.getText() != testString:
		generateErrorMessage("Comment constructor failed to set comment text", testString, constructed.getText())
		result = False

	if constructed.getLikes() != testInteger:
		generateErrorMessage("Comment constructor failed to set comment likes", testInteger, constructed.getLikes())
		result = False

	if constructed.getAuthor() != testAuthor:
		generateErrorMessage("Comment constructor failed to set comment author", testAuthor, constructed.getAuthor())
		result = False

	if constructed.getId() != testId:
		generateErrorMessage("Comment constructor failed to set comment Id", testId, constructed.getId())
		result = False

	if constructed.getTime() != testTime:
		generateErrorMessage("Comment constructor failed to set comment time", testTime, constructed.getTime)
		result = False

	if constructed.getReplyCount() != testCount:
		generateErrorMessage("Comment constructor failed to set comment reply count", testCount, constructed.getReplyCount())
		result = False

	if constructed.getAuthorId() != testAuthorId:
		generateErrorMessage("Comment constructor failed to set comment author id", testAuthorId, constructed.getAuthorId())
		result = False

	testToString = "<"
	testToString = testToString + testString + ","
	testToString = testToString + str(testInteger) + ","
	testToString = testToString + testAuthor + ","
	testToString = testToString + testId + ","
	testToString = testToString + testTime + ","
	testToString = testToString + str(testCount) + ","
	testToString = testToString + testAuthorId
	testToString = testToString + ">"

	if constructed.toString() != testToString:
		generateErrorMessage("toString failed on constructed comment", testToString, constructed.toString())
		result = False

	if constructed.toString() != empty.toString():
		generateErrorMessage("toString failed on two identical objects", str(False), str(constructed.toString() != empty.toString()))
		result = False

	#	This should be updated to allow different formats
	formattedComment = str(0) + ") " + constructed.getText() + "\n"
	if constructed.format(0) != formattedComment:
		generateErrorMessage("Format comment failed on constructed comment", formattedComment, constructed.format(0))

	return result;

def testGetById():
	result = True

	commentsOnVideo = getById("pDIQ7Otf1mw")

	if len(commentsOnVideo) == 0:
		generateErrorMessage("getById failed, expected non-empty list(expected answer was greater than zero)", len(commentsOnVideo), 1000)	#	1000 is an arbitrary non-zero number
		results = False

	if str(type(commentsOnVideo)) != "<type 'dict'>":
		generateErrorMessage("getById returns non-dict type", str(type(commentsOnVideo)), "<type 'dict'")

	keys = commentsOnVideo.keys()

	for i in range(len(keys)):
		if str(type(keys[i])) != "<type 'instance'>":
			generateErrorMessage("Keys from getById are of a non-instance type", "<type 'instance'>", str(type(keys[i])))
			results = False

	values = []

	for i in range(len((keys))):
		values.append(commentsOnVideo[keys[i]])

	for i in range(len(values)):
		if str(type(values[i])) != "<type 'list'>":
			generateErrorMessage("Values from getById are of a non-list type", "<type 'list'>", str(type(values[i])))
			results = False

	for i in range(len(values)):
		for j in range(len(values[i])):
			if str(type(values[i][j])) != "<type 'instance'>":
				generateErrorMessage("Values contained in lists from getById are not of instance type", "<type 'instance'>", str(type(values[i][j])))
				results = False

	#	Check to make sure that the replies are not contained in the comment list as well
	#	Additionally, the raw lengths of the values and keys lists are always equal, however many of the values elements are empty

	return result

def testUi():
	result = True;

	videoId = getVideoId()
	if videoId == "":
		generateErrorMessage("getVideoId returns an empty string", "dummy value", videoId)
		results = False

	testString = "xyz"
	idInput.setText(testString)

	if idInput.text() != testString:
		generateErrorMessage(testString, idInput.text(), testString)

	return result;

print("===\tStarting Unit Tests\t===");

if testCommentClass() == False:
	log.write("testCommentClass failed");

if testUi() == False:
	log.write("testUi failed");

if testGetById() == False:
	log.write("testGetById failed");

log.close();

print("===\tEnding Unit Tests\t===");

#	Should test the strings for illegal characters
#	Also, should make the csv file an actual csv file
