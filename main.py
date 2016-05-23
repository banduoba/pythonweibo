# coding:utf-8
# 入口文件
from weibo import Weibo
from budejie import Budejie
import time
import random
from tmall import Tmall

cookie = "SUHB=0z1QSD6NPHGsYt; _T_WM=a506522edde4d5289f7200fe4ed0b4e5; SUB=_2A256EAuhDeTxGeNG6FoU8y3LzDWIHXVZ-pXprDV6PUJbrdBeLXKlkW1LHeuCotsx-20jafpfu6wnfUM7_oWA8A..; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D; gsid_CTandWM=4uMFCpOz5wPOZPrZ3COuVouRTcz; M_WEIBOCN_PARAMS=uicode%3D20000061%26featurecode%3D20000180%26fid%3D3965617230628097%26oid%3D3965617230628097; H5_INDEX=0_all; H5_INDEX_TITLE=%E7%94%9F%E6%B4%BB%E5%BC%80%E5%BF%83%E5%B0%B1%E5%A5%BD%E5%93%88%E5%93%88"
weibo = Weibo(cookie)
budejie = Budejie()
tmall = Tmall()

#8-24点，每4个小时抓取一次
for i in range(4):
    list_duanzi = budejie.get_duanzi()
    list_goods = tmall.get_goods()
    #抓取的数据在4个小时内发布
    for j in range(4):
        #这是一个小时内的事情
        for k in range(6):
            #一个小时发布6条, 轮流发布商品和段子
            if (k%2==1):
                index = random.randint(0, len(list_duanzi) - 1)
                send_content = list_duanzi[index]
                list_duanzi.remove(send_content)
            else:
                index = random.randint(0, len(list_goods) - 1)
                g = list_goods[index]
                l = len(g["title"]+g["buy"])
                send_content = g['title']+">>"+g["summary"][0:140-l-10]+"..."+g["buy"]
                list_goods.remove(g)
            print("发送->"+send_content)
            weibo.send(send_content)
            # 随机时间睡眠, 范围（9-11分钟）
            t = random.randint(9 * 60, 11 * 60)
            print("睡眠" + str(t) + "秒")
            time.sleep(t)