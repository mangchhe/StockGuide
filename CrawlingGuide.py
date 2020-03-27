import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

class CrawlingGuide():

    def __init__(self):

        self.bsObject = ''

    def get_url(self, url):

        url = requests.get(url)
        self.bsObject =  BeautifulSoup(url.content, "html.parser")

    def t_get(self, tagName):

        tmp = []

        for val in self.bsObject.find_all(tagName):
            tmp.append(val)

        return tmp

    def c_get(self, className):

        tmp = []

        for val in self.bsObject.find_all(class_= className):
            tmp.append(val)

        return tmp

    def c_get_plus(self, className, option):

        tmp = []

        for val in self.bsObject.find_all(class_= className):
            tmp.append(val[option])

        return tmp

if __name__ == '__main__':

    crawlingGuide = CrawlingGuide()

    crawlingGuide.get_url('https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0')

    a = crawlingGuide.c_get_plus('_sp_each_title', 'title')
    b = crawlingGuide.c_get_plus('_sp_each_url', 'href')

    c = a + b
    for i in range(len(c)//2):
        print(c[i] , c[i+10])
