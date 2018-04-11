import datetime
import logging
import sys
import time

import got3 as got
import pickle as pkl


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(stdout_formatter)
log.addHandler(stdout_handler)

file_handler = logging.FileHandler('tweets.log')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
log.addHandler(file_handler)


class TweetWrapper():

    def __init__(self, tweet, term):
        self.term = term
        self.date = tweet.date
        self.favorites = tweet.favorites
        self.geo = tweet.geo
        self.hashtags = tweet.hashtags
        self.tweet_id = tweet.id
        self.mentions = tweet.mentions
        self.permalink = tweet.permalink
        self.retweets = tweet.retweets
        self.text = tweet.text
        self.username = tweet.username

    @property
    def properties(self):
        properties = [p for p in self.__dict__ if not p.startswith('_')]
        properties = [p for p in properties if not callable(getattr(self, p))]
        return properties

    def to_dict(self):
        representation = {}
        for p in self.properties:
            representation[p] = getattr(self, p)
        return representation

def fetch_tweets(term, start_date, end_date, limit=None):
    """Get old tweets for specified day of a month in a given year."""

    query_factory = got.manager.TweetCriteria()

    if limit:
        query = query_factory.setQuerySearch(term).setSince(start_date).setUntil(end_date).setMaxTweets(limit)
    else:
        query = query_factory.setQuerySearch(term).setSince(start_date).setUntil(end_date)

    return [TweetWrapper(tweet, term) for tweet in got.manager.TweetManager.getTweets(query)]

def main(term, date_range, limit, backoff):
    """Get old tweets for specified date range within a given month"""

    year, month, start_day, end_day = date_range

    for day in range(start_day, end_day + 1):

        start_date = datetime.date(year, month, day)

        # accounting for Twitter's non-inclusive date range
        if day is end_day and month is 12:
            end_date = datetime.date(year + 1, 1, 1) # next year
        elif day is end_day and month < 12:
            end_date = datetime.date(year, month + 1, 1) # next month
        else:
            end_date = datetime.date(year, month, day + 1) # next day

        # datetime stamps as strings
        start_date, end_date = start_date.isoformat(), end_date.isoformat()

        log.info(" ".join(["fetching", term, 'posted', start_date, 'to', end_date]))

        # get and save tweets for given day
        tweets = fetch_tweets(term, start_date, end_date, limit)
        tweets = [x.to_dict() for x in tweets]
        with open("{}_{}_tweets.pkl".format(start_date, term), "wb") as f:
        	pkl.dump(tweets, f)

        log.info(" ".join(['completed', str(len(tweets)), 'for', term, 'posted', start_date]))

        if day != end_day:
            log.info(" ".join(["backing off", str(backoff), 'minutes', '\n']))
            time.sleep(60 * backoff)


if __name__ == '__main__':
    """
    Completed:
        - #healthcare: 2016-11-01 to 2016-11-30
        - #aca: 2016-11-01 to 2016-11-30
        - #aca: 2016-12-01 to 2016-12-31
        - #aca: 2017-01-01 to 2017-01-31
        - #obamacare: 2016-11-01 to 2016-11-30
        - #obamacare: 2016-12-01 to 2016-12-31
        - #obamacare: 2017-01-01 to 2017-01-31
    """
    # configure courtesy
    backoff_minutes = 1 #unpadded integer
    message_limit = None #none or unpadded integer

    # prepare twitter query
    lst = ['Petersen Automotive Museum','Griffith Observatory','The Getty','El Pueblo de Los Angeles Historical Monument','Autry Museum of the American West', 'Griffith Park', 'Korean Friendship Bell', 'Runyon Canyon Park', 'Universal Studios Hollywood','Hollywood Sign','The Broad','Los Angeles County Museum of Art','Hollywood Bowl','Bradbury Building','Pierce Brothers Westwood Village Memorial Park and Mortuary','California Science Center','The Annenberg Space for Photography','Watts Towers State Historic Park','Natural History Museum of Los Angeles County','Skirball Cultural Center']
    for i in lst:
        term = i #string
        year = 2017 #four-digit integer
        month = 11 #unpadded integer
        start_day = 1 #unpadded integer
        end_day = 5 #unpadded integer

    # execute query
        date_range = (year, month, start_day, end_day)
        main(term, date_range, message_limit, backoff_minutes)