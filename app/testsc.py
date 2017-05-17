from selenium import webdriver
from depot.manager import DepotManager
#from BeautifulSoup import BeautifulSoup

# Hashmap Testing 

import re
from simhash import Simhash

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

# END
def DomSimhashTarget(target):
    depot = DepotManager.get()
    driver = webdriver.PhantomJS()
    driver.get(target)
    html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
#print html

#Hashmap print

    #print '%x' % Simhash(get_features(html)).value

#END


def DomSimhashAgainst(against):
    depot = DepotManager.get()
    driver = webdriver.PhantomJS()
    driver.get(against)
    html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
#print html

#Hashmap print

    #print '%x' % Simhash(get_features(html)).value

#END
