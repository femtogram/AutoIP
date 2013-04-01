import urllib2
from bs4 import BeautifulSoup


def get_funny_tweet(addr):
    soup = BeautifulSoup(urllib2.urlopen('http://funtweets.com/'), 'lxml')
    tweet = soup.find('div', class_='tweet-text').contents[-1].strip()
    return ''.join([tweet, ' The IP is ', addr])