# -*- coding: utf-8 -*-

import os
from selenium import webdriver
import sys

# fetch abs path
dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    book_title = sys.argv[1]
except IndexError:
    with open("title.txt") as f:
        book_title = f.read()

# fetch titles crawling
with open("crawl_urls.txt") as f:
    urls = [v.rstrip() for v in f.readlines()]

driver = webdriver.Chrome(executable_path=dir_path + '/chromedriver')

for index, url in enumerate(urls):
    if index == 0:
        driver.get(url.format(book_title))
    else:
        driver.execute_script("window.open('');")
        driver.switch_to_window(driver.window_handles[index])
        driver.get(url.format(book_title))
