#	Import YouTube API and whatever API wrappers are being used
from getcomments import *

#	Import GUI deps
from Tkinter import *
import ttk

#	Import internal methods and structures
from comment import *

comments = [];
authors = [];
nextToken = "";

def getByID(vid):

	results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100)
	print(results.keys());

	while("nextPageToken" in results.keys()):

		nextToken = results["nextPageToken"];

		items = results["items"];

		print(items[0]["snippet"]["topLevelComment"]["snippet"].keys());
		for i in range(len(items)):
			item = items[i]["snippet"]["topLevelComment"]["snippet"];
			comment = Comment(text=item["textOriginal"], author=item["authorDisplayName"], likes=item["likeCount"], id=item["authorChannelId"], time=["publishedAt"]);
			comments.append(comment);

		results = comment_threads_list_by_video_id(service, part='snippet, replies', videoId=vid, maxResults=100, pageToken=nextToken)

def formatCommentsForDisplay(comments):
	formatted = "";

	for i in range(len(comments)):
		formatted = formatted + str(i) + ") "

		formatted = formatted + comments[i].getText().encode('utf-8','ignore');

		formatted = formatted + "\n";

	print(formatted)
	return formatted;

def displayComments():

	if len(comments) == 0:
		return;

	print("Should display");

	#for i in range(len(comments)):
	#	commentDisplayBox.insert(END, comments[i].getText());

	commentDisplayBox.insert(END, formatCommentsForDisplay(comments));

def getVideoID(*args):
	idOfVideo = vidEntry.get();
	ID.set("Obtaining comments for video: " + vidEntry.get());
	getByID(idOfVideo);
	return idOfVideo;

root = Tk();

ID = StringVar();

mainframe = Frame(root);
mainframe.grid(row=0, column=0);

getIDLabel = Label(root, text="Video ID");
getIDLabel.grid(row=0);

idLabel = Label(root, textvariable=ID);

vidEntry = Entry(root);
vidEntry.grid(row=1);

getIdButton = Button(root, text="Get ID", command=getVideoID);
getIdButton.grid(row=2);

displayButton = Button(root, text="Display Comments", command=displayComments);
displayButton.grid(row=3);

commentDisplayBox = Text(root, height=30, width=200);
#commentDisplayBox.insert(END, "gfdjnsdkjgfjk");
commentDisplayBox.grid(row=4);

root.mainloop();
