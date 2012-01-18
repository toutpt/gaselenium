import time
import urllib
import sys

from selenium import webdriver

BING_URL = "http://www.bing.com/?%s"
BASE_QUERY = {'q':None}

domain = sys.argv[1]
keywords = open(sys.argv[2]).read().split('\n')

browser = webdriver.Firefox() # Get local session of firefox

for keyword in keywords:
    query = BASE_QUERY
    query['q'] = keyword
    url = BING_URL%urllib.urlencode(query)
    browser.get(url)
    browser.find_element_by_name('go').click()
    time.sleep(1)
    results = browser.find_elements_by_class_name('sb_tlst')
    for result in results:
        link = result.find_element_by_tag_name('a')
        rdomain = link.get_attribute('href')
        if rdomain.startswith(domain):
            link.click()
            time.sleep(2)
            break
    time.sleep(2)
    browser.delete_all_cookies()

browser.close()