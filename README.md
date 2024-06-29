# odds_ends

**[tidecal.py](tidecal/tidecal.py)** - Take a [NOAA Station ID](https://tidesandcurrents.noaa.gov/map/index.html) and convert the tide data to iCal format  

**[ipcheck.py](ipcheck.py)** - Check if your WAN ip on your home internet connection has changed  

**[teamcal.py](teamcal.py)** - Flask app that returns a calendar feed based on searches for calendar items that match the URL path, e.g.:
http://localhost/ghscal/boys/freshman/lacrosse would return all hits for "boys" and "freshman" and "lacrosse".

Searches are case insensitive and are globbed, so "boy/fresh/lacros" would match the same as "boys/freshman/lacrosse"

Looking at the root **http://hostname/ghscal/** will return all events.

There are a maximum of three arguments/path elements allowed. 

**[rss2reddit.py](rss2reddit.py)** - take an RSS feed and post the articles to a subreddit
