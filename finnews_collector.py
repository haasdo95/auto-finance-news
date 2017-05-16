# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

news_lib = open("news_lib.txt", "w")
resultStr = ""

for pageNum in range(10):
    url = "http://stock.10jqka.com.cn/bktt_list/index_" + str(pageNum) + ".shtml"
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    newsList = soup.select(".list-con ul")

    newsList = newsList[0]

    news = newsList.find_all("li")

    for story in news:
        storylink = story.select("span a")
        storylink = storylink[0]
        storylink = storylink["href"]
        storyHtml = urllib2.urlopen(storylink).read()
        storySoup = BeautifulSoup(storyHtml, "html.parser")
        newsText = storySoup.select(".atc-content p")
        for nt in newsText:
            resultStr += nt.text.strip()

news_lib.write(resultStr)
