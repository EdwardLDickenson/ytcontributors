#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

#	Import internal methods and structures
from comment import *

comments = [];
replies = [];
authors = [];

def parseComment(item):
	comment = Comment()

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
	replyList = [];

	if "replies" in comment.keys():
		for i in range(len(comment["replies"]["comments"])):
			replyList.append(parseComment(comment["replies"]["comments"][i]["snippet"]))

	return replyList;

def getComments(items):
	# commentList = [];
	#
	# for i in range(len(items)):
	# 	replies.extend(getReplies(items[i]));
	# 	item = items[i]["snippet"]["topLevelComment"]["snippet"];
	# 	commentList.append(parseComment(item))
	#
	# return commentList;

	commentList = []

	for i in range(len(items)):
		commentList.append(items[i])

	return commentList

# def getCommentObject(items):
# 	commentList = []
#
# 	for i in range(len(items)):
# 		commentList.append(items[i])
#
# 	return commentList

def formatCommentsForDisplay(comments):
	formatted = "";

	for i in range(len(comments)):
		formatted = formatted + str(i) + ") "
		#formatted = formatted + comments[i].getText().encode('utf-8','ignore');
		formatted = formatted + parseComment(comments[i]).getText().encode('utf-8','ignore');
		formatted = formatted + "\n";

	return formatted;

def getById(vid):
	results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100)

	while("nextPageToken" in results.keys()):
		nextToken = results["nextPageToken"];
		items = results["items"];
		comments.extend(getComments(items));
		results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100, pageToken=nextToken)

	items = results["items"];
	comments.extend(getComments(items));

	return comments

def clearComments():
	del comments[:]
	del replies[:]
	del authors[:]

def searchByString(string):
	pass
