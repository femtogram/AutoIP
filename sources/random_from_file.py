'''
Created on Mar 27, 2013

@author: lucky
'''
import os
import random
import re


def get_dictator(ip_addr):
    dict_file = open(os.path.join(os.path.dirname(os.getcwd()), "resources", "list_of_dictators"), 'r')
    dict_list = dict_file.readlines()
    todays = random.choice(dict_list)
    todays = re.sub("\[\d+\]", "", todays)
    [name, place, years, dtype] = re.split("\t", todays)
    byear = re.split("-", years)[0]
    return "".join(["Dictator ", name.strip(), " from ", place.strip(),
                    " was born in ", byear.strip(),
                    " and today's IP is: ", ip_addr])

if __name__ == "__main__":
    print get_dictator("123.1234.1")