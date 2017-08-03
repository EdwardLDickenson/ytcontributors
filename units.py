#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

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

	if empty.getID() != "":
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

	

	return result;

print("===\tStarting Unit Tests\t===");


if testCommentClass() == False:
	log.write("testCommentClass failed");

log.close();
print("===\tEnding Unit Tests\t===");
