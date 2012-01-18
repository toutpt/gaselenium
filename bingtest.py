from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import urllib
import urlparse
import sys

GOOGLE_URL = "http://www.bing.com/?%s"
BASE_QUERY = {'q':None}

domain = sys.argv[1]
keywords = open(sys.argv[2]).read().split('\n')

def check_domain(url):
    if not url.startswith('http://www.bing'):
        return url.startswith(domain)
    o = urlparse.urlparse(url)
    params = o.query.split('&')
    for param in params:
        if param.startswith('url='):
            rdomain = urllib.unquote(param[4:])
            return domain == rdomain
    return False

browser = webdriver.Firefox() # Get local session of firefox
for keyword in keywords:
    query = BASE_QUERY
    query['q'] = keyword
    url = GOOGLE_URL%urllib.urlencode(query)
    browser.get(url)
    browser.find_element_by_name('go').click()
    time.sleep(1)
    results = browser.find_elements_by_class_name('sb_tlst')
    for result in results:
        link = result.find_element_by_tag_name('a')
        rdomain = link.get_attribute('href')
        if check_domain(rdomain):
            link.click()
            time.sleep(2)
            break
    time.sleep(2)
    browser.delete_all_cookies()
browser.close()