'''
Created on Mar 26, 2013

@author: lucky
'''
import urllib2
import xml.etree.ElementTree as ET


def get_aus_weather():
    fetch = urllib2.urlopen("http://rss.weatherzone.com.au/?u=12994-1285&lt=aploc&lc=624&obs=1&fc=1&warn=1")
    result = fetch.read()
    try:
        tree = ET.fromstring(result)
    except:
        print "Except"
    for element in tree:
        print "NEW ELEMENT"
        print ET.tostring(element, method="text")
    print "DONE"