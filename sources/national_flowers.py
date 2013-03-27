import urllib2
from bs4 import BeautifulSoup
import random
import re

def conditional_a_extract(tag):
	if tag.find('a'):
		return tag.find('a').contents[0].strip()
	else:
		return tag.contents[0].strip()

def get_national_flower(addr):
	soup = BeautifulSoup(urllib2.urlopen('http://www.theflowerexpert.com/content/aboutflowers/national-flowers'), 'lxml')
	tbl = soup.find('table', class_='infotable').find('tbody').find_all('tr')
	randidx = random.randint(0, len(tbl) - 1)
	row = tbl[randidx].find_all('td')
	country = conditional_a_extract(row[0])
	flower = conditional_a_extract(row[1])
	return ''.join(['The national flower of ', country, ' is ', flower, ' and today\'s IP is: ', addr])
