'''
Bing(必应)每日背景定时获取

@author:Siver

www.siverking.online

首次提交:2024/05/27
最新提交:2024/05/29 (修改打印json内容会请求两次问题)
'''

import urllib.request
import requests
import os.path
import json
import schedule
import time

api_url = "https://api.vvhan.com/api/bing?type=json" # Bing每日一图当天壁纸API 返回格式为json   若api失效在本开源会及时更新可用api
dirname = "D:\\MY\T" # 所有图片存储路径   请修改
dirname2 = "D:\\MY\P" # 第二条存储位置 存放当天的图片 每日更新
runTime = "00:24" # 预定的获取时间 mm:dd   请修改


# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url=api_url):
    r = requests.get(raw_img_url).text
    print(r)
    r = json.loads(r)
    img_url = r['data']['url']  # 得到图片文件的网址
    global img_date # 全局
    img_date = r['data']['date'] # 得到日期
    print('img_url:', img_url)
    print('img_date:', img_date)
    return img_url

def save_img(img_url, dirname):
    # 保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print('文件夹', dirname, '不存在，重新建立')
            # os.mkdir(dirname)
            os.makedirs(dirname)
        if not os.path.exists(dirname2):
            print('文件夹', dirname2, '不存在，重新建立')
            # os.mkdir(dirname)
            os.makedirs(dirname2)
        # 获得图片文件名，包括后缀
        basename = "%s.jpg"%img_date
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filepath)
        print("Save", filepath, "successfully!")

        # 获得图片文件名，包括后缀
        basename = "everyday.jpg" # 固定一个文件为今天的照片
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname2, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filepath)
        print("Save", filepath, "successfully!")
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)
    #print("Save", filepath, "successfully!")

    return filepath
def get():
    save_img(get_img_url(), dirname)

schedule.every().day.at(runTime).do(get)#注册定时任务
get()#测试时打开
while True:
        schedule.run_pending()
        time.sleep(1)

