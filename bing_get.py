'''
Bing(必应)每日背景定时获取

@author:Siver

www.siverking.online

首次提交:2024/05/27
'''

import urllib.request
import requests
import os.path
import json
import schedule
import time

api_url = "https://api.vvhan.com/api/bing?type=json"#Bing每日一图当天壁纸API 返回格式为json   若api失效在本开源会及时更新可用api
dirname = "D:\\photo"#存储路径   请修改
runTime = "00:24"#预定的获取时间 mm:dd   请修改

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url=api_url):
    print(requests.get(raw_img_url).text)
    r = json.loads(requests.get(raw_img_url).text)
    img_url = r['data']['url']  # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url
# 请求网页，获取当天日期作为图片名字
def get_img_name(raw_img_url=api_url):
    r = json.loads(requests.get(raw_img_url).text)
    img_name = r['data']['date']  # 得到图片文件的网址
    print('img_name:', img_name)
    return img_name
def save_img(img_url, dirname):
    # 保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print('文件夹', dirname, '不存在，重新建立')
            # os.mkdir(dirname)
            os.makedirs(dirname)
        # 获得图片文件名，包括后缀
        basename = "%s.jpg"%get_img_name()
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)
    print("Save", filepath, "successfully!")

    return filepath
def get():
    save_img(get_img_url(), dirname)

schedule.every().day.at(runTime).do(get)#注册定时任务
#get#测试时打开
while True:
        schedule.run_pending()
        time.sleep(1)
'''
r = requests.get("https://api.vvhan.com/api/bing?type=json")
r = json.loads(r.text)
print(r['data']['url'])
'''
