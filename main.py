#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

#	Import GUI deps
# from Tkinter import *
# import ttk

#	Import internal methods and structures
from comment import *

comments = [];
replies = [];
authors = [];
#nextToken = "";

def getReplies(comment):
	replyList = [];

	if "replies" in comment.keys():
		for i in range(len(comment["replies"]["comments"])):
			replyList.append(comment["replies"]["comments"][i]["snippet"]["textOriginal"])

	return replyList;

def getComments(items):
	commentList = [];

	for i in range(len(items)):
		item = items[i]["snippet"]["topLevelComment"]["snippet"];
		getReplies(items[i]);
		comment = Comment(text=item["textOriginal"], author=item["authorDisplayName"], likes=item["likeCount"], id=item["authorChannelId"], time=["publishedAt"]);
		commentList.append(comment);
		replies.extend(getReplies(item));

	return commentList;

def formatCommentsForDisplay(comments):
	formatted = "";

	for i in range(len(comments)):
		formatted = formatted + str(i) + ") "
		formatted = formatted + comments[i].getText().encode('utf-8','ignore');
		formatted = formatted + "\n";

	return formatted;

def getByID(vid):
	results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100)

	while("nextPageToken" in results.keys()):
		nextToken = results["nextPageToken"];
		items = results["items"];
		comments.extend(getComments(items));
		results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100, pageToken=nextToken)

	items = results["items"];
	comments.extend(getComments(items));
