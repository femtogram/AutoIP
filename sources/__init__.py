import national_flowers
import tweets
import rss_feeds

source_list = list()
source_list.add(national_flowers.get_national_flower)
source_list.add(tweets.get_funny_tweet)
source_list.add(rss_feeds.get_aus_weather)
source_list.add(rss_feeds.get_wotd)
source_list.add(get_onion)
