import national_flowers
import tweets
import rss_feeds
import random_from_file

source_list = []
source_list.append(national_flowers.get_national_flower)
source_list.append(tweets.get_funny_tweet)
source_list.append(rss_feeds.get_aus_weather)
source_list.append(rss_feeds.get_wotd)
source_list.append(rss_feeds.get_onion)
source_list.append(rss_feeds.get_chinese)
source_list.append(random_from_file.get_dictator)