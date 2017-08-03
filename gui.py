#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

#	Import GUI deps
from Tkinter import *
import ttk

#	Import internal methods and structures
from comment import *

comments = [];
replies = [];
authors = [];
nextToken = "";

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

def displayComments():
	if len(comments) == 0:
		return;

	commentDisplayBox.insert(END, formatCommentsForDisplay(comments));
	commentsVScroll.config(command=commentDisplayBox.yview);

def getByID(vid):
	results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100)

	while("nextPageToken" in results.keys()):
		nextToken = results["nextPageToken"];

		items = results["items"];

		comments.extend(getComments(items));

		results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100, pageToken=nextToken)

	items = results["items"];
	comments.extend(getComments(items));

	numComments.set("Number of Comments: " + str(len(comments)));

def getVideoID(*args):
	idOfVideo = vidEntry.get();
	ID.set("Obtaining comments for video: " + vidEntry.get());
	getByID(idOfVideo);
	return idOfVideo;

root = Tk();

ID = StringVar();
numComments = StringVar();

mainframe = Frame(root);
mainframe.grid(row=0, column=0);

#commentFrame = Frame(mainframe);
#commentFrame.grid(row=4);

#commentsVScroll = Scrollbar(commentFrame);
commentsVScroll = Scrollbar(mainframe);
commentsVScroll.grid(row=4, column=5);

getIDLabel = Label(mainframe, text="Video ID");
getIDLabel.grid(row=0, column=0);

vidEntry = Entry(mainframe);
vidEntry.grid(row=0, column=1);

getButton = Button(mainframe, text="Get Comments", command=getVideoID);
getButton.grid(row=2);

displayButton = Button(mainframe, text="Display Comments", command=displayComments);
displayButton.grid(row=3);

#idLabel = Label(mainframe, textvariable=ID);
#idLabel.grid(row=0, column=2);

#commentDisplayBox = Text(commentFrame, height=30, width=150, yscrollcommand=commentsVScroll.set);
commentDisplayBox = Text(mainframe, height=30, width=100, yscrollcommand=commentsVScroll.set);
commentDisplayBox.grid(row=4, column=0);

numCommentsLabel = Label(mainframe, textvariable=numComments);
numCommentsLabel.grid(row=5, column=0);

root.mainloop();
