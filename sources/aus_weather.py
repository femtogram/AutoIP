'''
Created on Mar 26, 2013

@author: lucky
'''
import urllib2
import xml.etree.ElementTree as ET
import re
import HTMLParser


def _parse_title(title_text):
    title = re.sub("</?p>", "", title_text)
    return str(title)


def _parse_desc(desc_text):
    desc_text = re.sub("<img.+/>", "", desc_text)
    desc_text = re.sub("</?b>", "", desc_text)
    desc_text = re.sub("<br />", "", desc_text)
    desc_text = re.sub("\s{2,}", "\n", desc_text)
    desc_text = HTMLParser.HTMLParser().unescape(desc_text)
    return str(desc_text)


def get_aus_weather():
    fetch = urllib2.urlopen("http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=624&obs=1&fc=1&warn=1")
    result = fetch.read()
    try:
        tree = ET.fromstring(result)
    except:
        print "Except"
    for element in tree:
        #print ET.tostring(element, method="text")
        items = element.findall("item")
        for item in items:
            titles = item.findall("title")
            for title in titles:
                if title.text.startswith("Current"):
                    desc = item.findtext("description")
                    title = _parse_title(title.text)
                    desc = _parse_desc(desc)
                    return "".join([title, " is:", desc, "And today's ip is: "])

if __name__ == "__main__":
    print get_aus_weather()