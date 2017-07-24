#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

#	Import internal methods and structures
from comment import *

log = open("units.csv", "w");

def testCommentClass():
	empty = Comment();

	result = True;

	if empty.getText() != "":
		log.write("getText failed on an empty comment constructor");
		result = False;

	if empty.getLikes() != 0:
		log.write("getLikes failed on an empty comment constructor");
		result = False;

	if empty.getAuthor() != "":
		log.write("getAuthor failed on an empty comment constructor");
		result = False;

	if empty.getID() != "":
		log.write("getID failed on an empty comment constructor");
		result = False;

	if empty.getTime() != "":
		log.write("getTime failed on an empty comment constructor");
		result = False;

	return result;

print("===\tStarting Unit Tests\t===");


if testCommentClass() == False:
	log.write("testCommentClass failed");

log.close();
print("===\tEnding Unit Tests\t===");
