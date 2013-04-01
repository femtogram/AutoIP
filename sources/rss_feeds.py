'''
Created on Mar 26, 2013

@author: lucky
'''
import urllib2
import xml.etree.ElementTree as ET
import re
import HTMLParser


def get_aus_weather(ip_addr):
    fetch = urllib2.urlopen("http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=624&obs=1&fc=1&warn=1")
    result = fetch.read()
    tree = ET.fromstring(result)
    for element in tree:
        #print ET.tostring(element, method="text")
        items = element.findall("item")
        for item in items:
            titles = item.findall("title")
            for title in titles:
                if title.text.startswith("Current"):
                    desc = item.findtext("description")
                    desc = re.findall("(?<=Temperature:</b> )[\d\.&#;CF]{3,20}(?=\n)", desc)[0]
                    desc = HTMLParser.HTMLParser().unescape(desc)
                    return "".join(["Right now, in Sydney, Australia, the temperature is ", desc,
                                    ", and today's IP is: ", ip_addr])


def get_wotd(ip_addr):
    fetch = urllib2.urlopen("http://dictionary.reference.com/wordoftheday/wotd.rss")
    result = fetch.read()
    tree = ET.fromstring(result)
    for element in tree:
        #print ET.tostring(element, method="text")
        items = element.findall("item")
        for item in items:
            if item.find("pubDate") is not None:
                word = item.findtext("description")
                parts = re.split(":", word)
                parts[0] = parts[0].capitalize()
                parts[1] = re.sub("\.", "", parts[1])
                return "".join(["The Word of the Day is '", parts[0], ",", parts[1],
                                "' and today's IP is: ", ip_addr])


def get_onion(ip_addr):
    fetch = urllib2.urlopen("http://feeds.theonion.com/theonion/daily")
    result = fetch.read()
    tree = ET.fromstring(result)
    for element in tree:
        items = element.findall("item")
        for item in items:
            title = item.findtext("title")
            return "".join(["In the news today, ", title,
                            " and today's IP is: ", ip_addr])


def get_chinese(ip_addr):
    fetch = urllib2.urlopen("http://www.mdbg.net/chindict/chindict_feed.php?feed=hsk_1")
    result = fetch.read()
    tree = ET.fromstring(result)
    for element in tree:
        titles = element.findall("{http://www.w3.org/2005/Atom}title")
        for title in titles:
            return "".join(["Today's Chinese word is '", title.text,
                            "' and today's IP is: ", ip_addr])


if __name__ == "__main__":
    print get_aus_weather("129.161.209.87")
    print get_wotd("129.161.209.87")
    print get_onion("124.1234.1234.1")
    print get_chinese("123.14141.141")