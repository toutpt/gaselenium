from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import urllib
from xml.dom.minidom import parseString

browser = webdriver.Firefox() # Get local session of firefox
url = 'http://monsite.com/sitemap.xml'
xml = urllib.urlopen(url).read()
dom = parseString(xml)
urls = dom.getElementsByTagName('loc')

for urldom in urls:
    url = str(urldom.firstChild.nodeValue)
    browser.get(url)
    time.sleep(2)

browser.close()