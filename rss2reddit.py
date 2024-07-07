import feedparser
import praw
from datetime import datetime
from datetime import timedelta
import time
import logging


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

# Greenwich Free Press
rss_url='https://greenwichfreepress.com/feed/'

#Greenwich Time
#rss_url='https://www.greenwichtime.com/rss/feed/News-1452.php'

#monkey patch to strip all html
feedparser.sanitizer._HTMLSanitizer.acceptable_elements = []

d = feedparser.parse(rss_url)


earlier = datetime.timetuple(datetime.utcnow() - timedelta(hours=12))

#reddit = praw.Reddit(
#    client_id="XXXXXXX"
#    client_secret="XXXXXXX",
#    password="XXXXXXX",
#    user_agent="rss reposter",
#    username="XXXX",
#)

tmpart = reddit.redditor('greenwitchbot').submissions.new(limit=1)

try:
    latest_r_post=time.gmtime(tmpart.__iter__().__next__().created_utc)
except:
    latest_r_post=time.gmtime(0)

f_title = d.feed.title
logging.info("Begin rss2reddit run")
for entry in reversed(range(len(d.entries))):
    if  d.entries[entry].published_parsed > latest_r_post:
        a_pubdate = d.entries[entry].published
        a_title=d.entries[entry].title
        a_entry=d.entries[entry].summary
        a_link=d.entries[entry].link
        a_author=d.entries[entry].author

        a_post = f'[{f_title}]({a_link})\n\n{a_entry}\n\n{a_pubdate}'
        #print(f"{entry}. {a_post}")
        logging.info(f"Posted: {a_title}")
        reddit.subreddit("Greenwich").submit(a_title, selftext=a_post)
logging.info("End rss2reddit run")

