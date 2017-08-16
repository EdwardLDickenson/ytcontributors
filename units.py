#	Import YouTube API and whatever API wrappers are being used
from getcomments import *
from main import *

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

	if empty.getAuthor() != "":
		log.write("getAuthor failed on an empty comment constructor\n");
		result = False;

	if empty.getId() != "":
		log.write("getID failed on an empty comment constructor\n");
		result = False;

	if empty.getTime() != "":
		log.write("getTime failed on an empty comment constructor\n");
		result = False;

	testString = "This was formerly blank"
	empty.setText(testString);
	if empty.getText() != testString:
		generateErrorMessage("setText failed on non-empty test string", empty.getText(), testString);
		result = False;

	testInteger = 123;
	empty.setLikes(testInteger);
	if empty.getLikes() != testInteger:
		generateErrorMessage("setLikes failed on non-zero integer", empty.getLikes(), testInteger);
		result = False;

	testAuthor = "There really should be no author for this";
	empty.setAuthor(testAuthor);
	if empty.getAuthor() != testAuthor:
		generateErrorMessage("setAuthor failed on non-empty string", empty.getAuthor(), testAuthor);
		result = False;

	testId = "ID is probably alpha numeric123"
	empty.setId(testId);
	if empty.getId() != testId:
		generateErrorMessage("setId failed on non-empty string", empty.getId(), testId);
		result = False

	testTime = "also alphanumeric123"
	empty.setTime(testTime)
	if empty.getTime() != "also alphanumeric123":
		generateErrorMessage("setTime failed on non-empty string", empty.getTime(), testTime)
		result = False

	return result;

def testGetById():
	result = True

	commentsOnVideo = getById("pDIQ7Otf1mw")

	for i in range(len(commentsOnVideo.keys())):
		print(len(commentsOnVideo[commentsOnVideo.keys()[i]]))


	return result

def testGetComments():
	result = True
	testList = []
	testReplies = []

	testList = getById("pDIQ7Otf1mw")	#	Soulshine

	if str(type(testList)) != "<type 'list'>":
		generateErrorMessage("Fatal Error, list generated from video ID is not of list type", "<type 'list'>", str(type(testList)));

		return False;

	if len(testList) == 0:	#	Assuming that the comments are not disabled
		generateErrorMessage("getCommentsById failed on a video");
		result = False;

	replyList = []

	# for i in range(len(testList)):
	# 	replyList.extend(getReplies(testList[i]))

	# print(type(testList[0]))
	# if type(str(testList)) != "<type 'instance'>":
	# 	print("gfndjklgnfl")

	return result

def testUi():
	result = True;

	return result;

print("===\tStarting Unit Tests\t===");

if testCommentClass() == False:
	log.write("testCommentClass failed");

if testUi() == False:
	log.write("testUi failed");

if testGetById() == False:
	log.write("testGetComments failed");

print(len(replies))
print(len(comments))

log.close();
print("===\tEnding Unit Tests\t===");

#	Should test the strings for illegal characters
#	Also, should make the csv file an actual csv file
