# -*- coding: utf-8 -*-
import string
import urllib2


def baidu_tieba(url, beginPage, endPage):
    for i in range(beginPage, endPage):
        stringName = string.zfill(i, 5) + ".html"
        print "Downloading " + "page" + i + " and it will be saved to " + stringName + "......"
        htmlFile = open(stringName, 'w+')
        content = urllib2.urlopen(url + str(i)).read()
        htmlFile.write(content)
        htmlFile.close()


if __name__ == "__main__":
    bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
    beginPage = 1
    endPage = 100

    baidu_tieba(bdurl, beginPage = beginPage, endPage = endPage)