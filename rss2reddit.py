import feedparser
import praw
import pprint
from datetime import datetime
from datetime import timedelta
# Greenwich Free Press
rss_url='https://greenwichfreepress.com/feed/'

#Greenwich Time
#rss_url='https://www.greenwichtime.com/rss/feed/News-1452.php'

#monkey patch to strip all html
feedparser.sanitizer._HTMLSanitizer.acceptable_elements = []

d = feedparser.parse(rss_url)


earlier = datetime.timetuple(datetime.utcnow() - timedelta(hours=12))


f_title = d.feed.title
for entry in range(len(d.entries)):
    if  d.entries[entry].published_parsed > earlier:
        a_pubdate = d.entries[entry].published
        a_title=d.entries[entry].title
        a_entry=d.entries[entry].summary
        a_link=d.entries[entry].link
        a_author=d.entries[entry].author

        #print(a_title)
        #print(a_author)
        #print(a_entry)
        #print(a_link)
        a_post = f'[{f_title}]({a_link})\n\n{a_entry}\n\n{a_pubdate}'
        print(f"{entry}. {a_post}")

#pprint.pp(len(d.entries))

#reddit = praw.Reddit(
#    client_id="2gFwB4Avy_46lgb2HZDrVQ",
#    client_secret="__OCFHd7EzWG128W2VjtAz3RNa4apA",
#    password="xodpu1-qosguD-jimzyb",
#    user_agent="rss reposter",
#    username="greenwitchbot",
#)

#newarticles = reddit.subreddit("Greenwich").new(limit=5)


#for article in newarticles:
#    print(article)


#reddit.subreddit("test").submit(a_title, selftext=a_post)