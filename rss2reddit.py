import feedparser
import praw
from datetime import datetime
from datetime import timedelta
import logging
import unicodedata

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

# Greenwich Free Press
rss_url='https://greenwichfreepress.com/feed/'

#Greenwich Time
#rss_url='https://www.greenwichtime.com/rss/feed/News-1452.php'

#monkey patch to strip all html
feedparser.sanitizer._HTMLSanitizer.acceptable_elements = []

d = feedparser.parse(rss_url)

reddit = praw.Reddit(
    client_id="XXXXXXX",
    client_secret="XXXXXXX",
    password="XXXXXXX",
    user_agent="rss reposter",
    username="XXXX",
)

# set up variables

# all the articles from the RSS feed
article_list = []

# the titles of the articles from the RSS feed
rss_title_list = []

# the titles of the articles posted to Reddit
reddit_title_list = []

#the articles to post to Reddit
posts = []

def utf_norm(string):
    return unicodedata.normalize('NFKC', string) 

# Get 20 most recent articles posted to Reddit
tmpart = reddit.redditor('greenwitchbot').submissions.new(limit=20)

# Put just the titles in a list
for submission in tmpart:
    reddit_title_list.append(utf_norm(submission.title))

f_title = d.feed.title

# put all the articles from the RSS feed into a list of dicts

for entry in reversed(range(len(d.entries))):
    article = {}
    rss_title_list.append(utf_norm(d.entries[entry].title))
    article["title"] = utf_norm(d.entries[entry].title)
    article["selftext"] = f'[{f_title}]({d.entries[entry].link})\n\n{d.entries[entry].summary}\n'
    article_list.append(article)

# get the list of article titles to post bye getting the titles only in the RSS feed

to_post = list(set(rss_title_list).difference(reddit_title_list))

# remove all the articles that have already been posted
for post_article in article_list:
    if post_article["title"] in to_post:
        posts.append(post_article)


logging.info("Begin rss2reddit run")

# post the articles to Reddit
for a in posts:
    print(f'Posting {posts.index(a) + 1}/{len(posts)} {a["title"]}, {a["selftext"]})')
    #reddit.subreddit("greenwich").submit({a["title"]}, selftext={a["selftext"]})

logging.info("End rss2reddit run")
