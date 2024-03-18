'''
    第一个简单的爬取图片程序，使用python3.x和urllib与re库 
'''  
import urllib.request  
import re             #正则表达式
import os
def getHtmlCode(url):  # 该方法传入url，返回url的html的源码  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'  
    }  
    url1 = urllib.request.Request(url, headers=headers) # Request函数将url添加头部，模拟浏览器访问  
    page = urllib.request.urlopen(url1).read()  # 将url页面的源代码保存成字符串  
    page = page.decode('GB2312','ignore')  # 字符串转码  
    return page  
  
def getImg(page):  # 该方法传入html的源码，经过截取其中的img标签，将图片保存到本机  
    #imgList = re.findall(r'(https:[^\s]*?(jpg|png|gif))"',page) 一些网站采用https协议
    imgList = re.findall(r'(http:[^\s]*?(jpg|png|gif))"',page)  
    x = 0
    if not os.path.exists('C:/img1'):    #不存在则创建E:/img1文件夹
        os.mkdir('C:/img1')
    for imgUrl in imgList:  # 列表循环
        try:
            print('正在下载：%s'%imgUrl[0])  
            # urlretrieve(url,local)方法根据图片的url将图片保存到本机  
            #urllib.request.urlretrieve(imgUrl[0],'E:/img1/%d.jpg'%x)
            urllib.request.urlretrieve(imgUrl[0],'C:/img1/%d.%s'%(x,imgUrl[1]))
            x+=1
        except:
             continue   
  
if __name__ == '__main__':    
    url = 'http://www.dangdang.com'      #指定网址页面
    #url = 'http://search.dangdang.com/?key=python&act=input'
    page = getHtmlCode(url)  
    getImg(page)
