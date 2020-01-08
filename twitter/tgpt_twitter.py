from tgpt_global import globalManager
import sys
import html
import re
import pandas as pd
import time
from time import sleep
replies = []

def handle_reply(status):
	text = status.full_text
	for reply in replies:
		if(reply['id'] == status.in_reply_to_status_id):
			reply['text'] = text +" "+ reply['text']
			return
	data = {"id": status.in_reply_to_status_id, "text":text}
	replies.append(data)
	return

def remove_unwated(text):
	bad_chars = [';', ':', '!', "*","."]
	text = html.unescape(text.strip())
	text.encode('ascii', 'ignore').decode('ascii')
	text = filter(lambda i: i not in bad_chars, text)
	return "".join(text)

def check_if_reply(tweetId):
	for reply in replies:
		if(reply['id'] == tweetId):
			piece = reply['text']
			replies.remove(reply)
			return piece
	return None

def generate_csv(tweets):
	tweetDf = pd.DataFrame(tweets)
	tweetDf = tweetDf.drop(['date', 'id'], axis=1)
	tweetDf.to_csv('../csv/'+globalManager.args.csv_file_name+'.csv',index=False,header=False)

if __name__ == '__main__':
	allTweets= []
	fininshed = False
	regexp = re.compile(r'http\S+')
	for handle in globalManager.handles:
		nextId = 0
		while True:
			if nextId == 0:
				statuses = globalManager.api.GetUserTimeline(screen_name=handle,exclude_replies=False,count=200,trim_user=True)
			else:
				statuses = globalManager.api.GetUserTimeline(screen_name=handle,exclude_replies=False,count=200,max_id=nextId,trim_user=True)
			try:
				nextId = statuses[-1].id - 1
			except IndexError:
				if fininshed:
					sys.stdout.write('\n')
					break
				else:
					sleep(10)
					fininshed = True
			for status in statuses:
				if not status.full_text.startswith('RT') and len(status.full_text) != '' and not regexp.search(status.full_text):
					status.full_text = remove_unwated(status.full_text)
					if(status.in_reply_to_status_id):
						handle_reply(status)
					else:
						piece = check_if_reply(status.id)
						if(piece):
							status.full_text += " "+  piece
						tweet = {"id":status.id,"date":status.created_at,"text":status.full_text}
						if len(tweet['text']) > 0:
							allTweets.append(tweet)
			sys.stdout.write('\r')
			sys.stdout.write("fetching tweets, handle: "+str(handle)+" total tweets: "+str(len(allTweets)))
			sys.stdout.flush()
	print('\n')

	generate_csv(allTweets)