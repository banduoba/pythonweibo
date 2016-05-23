# coding:utf-8
# 从逛丢网抓取的天猫优惠信息
import requests
import urllib.parse
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
    "Accept": "image/png,image/*;q=0.8,*/*;q=0.5",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "",
    "Connection": "keep-alive"
}

class Tmall:
    url = "http://guangdiu.com/cate.php?m=%E5%A4%A9%E7%8C%AB&p="

    def __init__(self):
        pass

    def get_goods(self):
        rlist = []
        g = {}
        res = requests.get(self.url, headers = headers)
        if res.status_code==200:
            soup = BeautifulSoup(res.text.encode("iso-8859-1").decode("utf-8"), "html.parser")
            for i in soup.find_all("div", class_="gooditem"):
                g['title'] = i.find("a", class_="goodname")["title"]
                g['buy'] = i.find("a", class_="innergototobuybtn")['href']
                g['img'] = i.img['src']
                g['summary'] = i.find('a', class_="abstractcontent").text[4:-13]+"..."
                rlist.append(g)
                g = dict()
            return rlist
        else:
            return None


    #将url解析出天猫对应的url
    def url_docode(self, url):
        print(url)
        p = url.split("?")[1].split("&")
        t = {}
        for pp in p:
            tt = pp.split("=")
            t[tt[0]] = tt[1]
        url = t['ct']
        url = url[url.find("http"):]
        url = urllib.parse.unquote(urllib.parse.unquote(url))
        return url


if __name__=="__main__":
    t = Tmall()
    l = t.get_goods()
    for i in l:
        print(i['buy'])
