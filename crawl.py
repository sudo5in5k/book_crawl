# -*- coding: utf-8 -*-

import os
from selenium import webdriver
import sys

# fetch abs path
dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    book_title = ""
    for index, arg in enumerate(sys.argv):
        # 空白がある本を検索する場合、タイトルがすべて取得できないため修正
        if not index == 0:
            book_title += " " + str(arg)
except IndexError:
    with open("title.txt") as f:
        book_title = str(f.read())

if "#" in book_title:
    book_title = book_title.replace("#", "%23")

# fetch titles crawling
with open("crawl_urls.txt") as f:
    urls = [v.rstrip() for v in f.readlines()]

driver = webdriver.Chrome(executable_path=dir_path + '/chromedriver')

for index, url in enumerate(urls):
    if index == 0:
        target_url = url.format(book_title)
        print(target_url)
        driver.get(target_url)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to_window(driver.window_handles[index])
        driver.get(url.format(book_title))
