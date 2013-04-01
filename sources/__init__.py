import national_flowers
import tweets
import rss_feeds
import random_from_file

source_list = list()
source_list.add(national_flowers.get_national_flower)
source_list.add(tweets.get_funny_tweet)
source_list.add(rss_feeds.get_aus_weather)
source_list.add(rss_feeds.get_wotd)
source_list.add(rss_feeds.get_onion)
source_list.add(rss_feeds.get_chinese)
source_list.add(random_from_file.get_dictator)