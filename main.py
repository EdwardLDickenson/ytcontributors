#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

#	Import internal methods and structures
from comment import *

comments = [];
replies = [];
authors = [];

#	A significant percentage of the functionality in this file could be wrapped into the comment class
def parseComment(item):
	comment = Comment()

	if str(type(item)) == "<type 'instance'>":
		return item

	#	If it's a root level comment then strip the rest from the content
	if "snippet" in item:
		item = item["snippet"]["topLevelComment"]["snippet"]

	if "textOriginal" in item.keys():
		pass

	if "textDisplay" in item.keys():
		comment.setText(item["textDisplay"]);

	if "channelId" in item.keys():
		pass

	if "updatedAt" in item.keys():
		pass

	if "videoId" in item.keys():
		pass

	if "parentId" in item.keys():
		pass

	if "canRate" in item.keys():
		pass

	if "viewerRating" in item.keys():
		pass

	if "moderationStatus" in item.keys():
		pass

	if "authorDisplayName" in item.keys():
		comment.setAuthor(item["authorDisplayName"])

	if "likeCount" in item.keys():
		comment.setLikes(item["likeCount"]);

	if "id" in item.keys():
		comment.setId(item["id"])

	if "publishedAt" in item.keys():
		comment.setTime(item["publishedAt"]);

	return comment

def getReplies(comment):
	if str(type(comment)) != "<type 'list'>":
		return

	replyList = [];

	if str(type(comment)) == "<type 'dict'>":
		if "items" in comment.keys():
			comment = comment["items"]

	for i in range(len(comment)):
		if "replies" in comment[i].keys():
			for j in range(len(comment[i]["replies"]["comments"])):
				replyList.append(comment[i]["replies"]["comments"][j]["snippet"])

	return replyList;

def getComment(items):
	comment = Comment()
	comment.parseComment(items)
	return comment

#	Currently only includes comments with replies. This is obviously wrong
def constructCommentReplyMap(commentList, replyList):
	keyList = []
	results = {}

	#	Very inefficient, removing some list elements would probably make it faster
	for i in range(len(commentList)):
		#	If/when the video class is written this probably should be wrapped into it
		itemList = commentList[i]["items"]
		for i in range(len(itemList)):
			comment = Comment()
			comment.parseComment(itemList[i])
			keyList.append(comment)

	for i in range(len(keyList)):
		values = []
		for j in range(len(replyList)):
			if replyList[j]["parentId"] == keyList[i].getId():
				tmp = Comment()
				tmp.parseComment(replyList[j])
				values.append(tmp)

		results.update({keyList[i]: values})

	return results

def getById(vid):
	nextToken = " "
	results = []
	commentList = []
	replyList = []

	#	Benchmark the relative sizes of maxResults and the time it takes to download the comments
	while nextToken != "":
		results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100, pageToken=nextToken)

		commentList.append(results)

		if "nextPageToken" in results.keys():
			nextToken = results["nextPageToken"]

		else:
			nextToken = ""

		replyList.extend(getReplies(results["items"]))
		print("Comments: " + str(len(commentList) * 100 - 100) + " - " + str(len(commentList) * 100))

	return constructCommentReplyMap(commentList, replyList)

def formatCommentForDisplay(comment, index):
	formatted = "" + str(index) + ")"
	formatted = formatted + parseComment(comment).getText().encode("utf-8", "ignore")
	formatted = formatted + "\n"

	return formatted

def formatCommentsForDisplay(commentList):
	formatted = "";

	for i in range(len(commentList)):
		formatted = formatted + str(i) + ") "
		formatted = formatted + parseComment(commentList[i]).getText().encode('utf-8','ignore');
		formatted = formatted + "\n";

	return formatted;

def clearComments():
	del comments[:]
	del replies[:]
	del authors[:]

def searchByString(string):
	pass
