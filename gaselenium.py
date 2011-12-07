from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import urllib
import sys
from xml.dom.minidom import parseString

import pdb;pdb.set_trace()
url = sys.argv[1]
xml = urllib.urlopen(url).read()
dom = parseString(xml)
urls = dom.getElementsByTagName('loc')

browser = webdriver.Firefox() # Get local session of firefox

for urldom in urls:
    url = str(urldom.firstChild.nodeValue)
    browser.get(url)
    time.sleep(2)

browser.close()