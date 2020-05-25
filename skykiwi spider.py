  #-*- coding:utf-8 -*- python 3.6.2
import http.cookiejar
import urllib.request
import re
import csv
import time
import random

import json

import os
from urllib.request import urlretrieve
from PIL import Image
import pytesseract
from datetime import datetime, timedelta, date

from bs4 import BeautifulSoup

howmany = 20
msgtext = "%E6%82%A8%E5%A5%BD%EF%BC%8C%E6%88%91%E4%BB%AC%E6%B3%A8%E6%84%8F%E5%88%B0%E6%82%A8%E5%8F%91%E5%B8%83%E6%96%B0%E7%9A%84%E7%A7%9F%E6%88%BF%EF%BC%8CRental%20NZ%E5%85%8D%E8%B4%B9%E5%8F%91%E5%B8%83%E7%A7%9F%E6%88%BF%EF%BC%8C%E7%BD%91%E5%9D%80%EF%BC%9A%20http%3A%2F%2Frentalnz.co.nz%2F%20%E5%AE%A2%E6%9C%8D%E5%BE%AE%E4%BF%A1%EF%BC%9ARentalNZ"
url = "http://bbs.skykiwi.com/forum.php?mod=forumdisplay&fid=19&orderby=dateline&sortid=287&filter=author&page=1"
#url = "https://www.google.com"
request = urllib.request.Request(url)
#模拟Mozilla浏览器进行爬虫
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print ("server statues: "+str(response2.getcode()))
html_doc = response2.read().decode("utf8")
#print (mystr)

#创建一个BeautifulSoup解析对象
soup1 = BeautifulSoup(html_doc,"lxml")#"html.parser",from_encoding="utf-8")

csvfile = []
stopneed=0
print ("-------主页连接获取-------")
link_node = soup1.find_all('a',"xst")
for link in link_node:
    onepage = []
    #创建一个BeautifulSoup解析对象
    print (link.name,link['href'],link['class'],link.get_text())

    req = urllib.request.Request("http://bbs.skykiwi.com/"+link['href'])
    req.add_header("user-agent","Mozilla/5.0")
    resp = urllib.request.urlopen(req)
    print ("server statues: "+str(resp.getcode()))
    html_doc1 = resp.read().decode("utf8")

    soup = BeautifulSoup(html_doc1,features="lxml")#"html.parser",from_encoding="utf-8")

    print ("-----------标题----------")
    onepage.append(str(soup.find('a',id="thread_subject").get_text()))
    print(soup.find('a',id="thread_subject").get_text())

    imgname = './TmpImg1.png'
    startOcr = False
    tables = soup.findAll('table',bordercolor="#fff")
    tab = tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            if(td.getText() == "联系电话:"):
                startOcr = True
            if not(td.getText() in ["类型:","每周租金:","微信:","联系电话:"]):
                if (td.getText()=="") and (startOcr) :
                    #print ("http://bbs.skykiwi.com/"+td.find('image')["src"])
                    print("---------电话图片链接-------")
                    print("image link: http://bbs.skykiwi.com/"+td.find('image')["src"])
                    urlretrieve("http://bbs.skykiwi.com/"+td.find('image')["src"], imgname)
                    try:
                        phonenum=pytesseract.image_to_string(Image.open(imgname))#,lang='chi_sim')
                        onepage.append(str(phonenum))
                        print(phonenum)
                        os.remove(imgname)
                    except:
                        print("电话Ocr识别出错 phone img recnize error")
                    txtapi="http://101.100.3.114:8778/sendsms?username=smsuser&password=itauckland0903&phonenumber="+phonenum+"&message="+msgtext
                    txtreq=urllib.request.Request(txtapi)
                    txtresp=urllib.request.urlopen(txtreq)
                    txtdata=txtresp.read().decode('utf-8')
                    txtjson = json.loads(txtdata)
                    onepage.append(str(txtjson["report"][0]["1"][0]["time"]))
                    onepage.append(str(txtjson["report"][0]["1"][0]["result"]))
                    print(txtjson["report"][0]["1"][0]["result"])
                else:
                    onepage.append(str(td.getText()))
                    print (td.getText())

    print ("内容")
    contex=""
    text = soup.find('td',class_="t_f")
    contex=contex+text.contents[0].strip()
    for tx in text.contents:
        if isinstance(tx, str):
            contex=contex+str(tx.strip())
           # print(tx.strip())
    onepage.append(contex)
    csvfile.append(onepage)
    stopneed = stopneed+1
    if stopneed == howmany:
        break
    time.sleep(18+random.randint(3,9))

import codecs
if(not(os.path.exists("log"))):
    os.makedirs("log")

currentTime = datetime.now().strftime("%d_%m_%Y %H.%M.%S %f")
with open("log/"+currentTime+".csv","w") as files: 
    writer = csv.writer(files)
    #先写入columns_name
    writer.writerow(["title","type","Rent per week","Wechat","phone","time","statue","Content"])
    print(csvfile)
    writer.writerows(csvfile)
    #写入多行用writerows
    #writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
   
# with open("log/"+currentTime+".csv","wb") as files: 
#     files.write(codecs.BOM_UTF8)
#     writer = csv.writer(files, dialect='excel')
#     #先写入columns_name
#     writer.writerow(["标题","类型","每周租金","微信","联系电话","内容"])
#     #print(csvfile)
#     writer.writerows(csvfile)

#     #写入多行用writerows
#     #writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
