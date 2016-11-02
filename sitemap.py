#coding: utf-8
__author__ = 'Magdum'

import requests
import gzip
from StringIO import StringIO
from bs4 import BeautifulSoup


def parseXmlSitemap():
    url = "http://www.dentystapoleca.pl/sitemap.xml.gz"
    ur = requests.get(url)
    data = ur.text
    soup = BeautifulSoup(data)
    urls = []
    for url in soup.findAll("loc"):
        urls.append(url.text)
    return urls


print parseXmlSitemap()


def gzSitemapParse():
    r = requests.get('http://www.dentystapoleca.pl/sitemap-1-1.xml.gz')
    sitemap = gzip.GzipFile(fileobj=StringIO(r.content)).read()
    return sitemap


print gzSitemapParse()

