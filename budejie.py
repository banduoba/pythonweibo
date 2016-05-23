# coding:utf-8
# 百思不得其姐
import requests
from bs4 import BeautifulSoup

class Budejie:
    url = "http://www.budejie.com/new-text/"

    def __init__(self):
        pass

    def get_duanzi(self):
        res = requests.get(self.url)
        if res.status_code==200:
            soup = BeautifulSoup(res.text, "html.parser")
            rlist =[]
            for l in soup.find_all("div",class_="j-r-list-c-desc"):
                rlist.append(l.text.strip())
            return rlist
        else:
            return None
if __name__=="__main__":
    b = Budejie()
    list = b.get_duanzi()
    print(list)