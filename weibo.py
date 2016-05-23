# coding:utf-8
# 微博相关接口
import requests
import json

class Weibo:

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Accept": "image/png,image/*;q=0.8,*/*;q=0.5",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://m.weibo.cn/",
        "Cookie": "",
        "Connection": "keep-alive"
    }

    def __init__(self, cookie):
        self.headers["Cookie"]=cookie

    def send(self, content):
        if content==None or content=="":
            return False
        else:
            data = {
                "content": content
            }
            res = requests.post("http://m.weibo.cn/mblogDeal/addAMblog", headers=self.headers, data=data)
            js = json.loads(res.text)
            if res.status_code==200 and js['ok']==1:
                return True
            else:
                return False

    def send_with_img(self, content, img):
        pass

if __name__=="__main__":
    testcookie = "SUHB=0z1QSD6NPHGsYt; _T_WM=a506522edde4d5289f7200fe4ed0b4e5; SUB=_2A256EAuhDeTxGeNG6FoU8y3LzDWIHXVZ-pXprDV6PUJbrdBeLXKlkW1LHeuCotsx-20jafpfu6wnfUM7_oWA8A..; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D; gsid_CTandWM=4uMFCpOz5wPOZPrZ3COuVouRTcz; M_WEIBOCN_PARAMS=uicode%3D20000061%26featurecode%3D20000180%26fid%3D3965617230628097%26oid%3D3965617230628097; H5_INDEX=0_all; H5_INDEX_TITLE=%E7%94%9F%E6%B4%BB%E5%BC%80%E5%BF%83%E5%B0%B1%E5%A5%BD%E5%93%88%E5%93%88"
    w = Weibo(testcookie)
    content = input("请输入发送的微博内容：")
    if w.send(content):
        print("发送成功")
    else:
        print("发送失败")