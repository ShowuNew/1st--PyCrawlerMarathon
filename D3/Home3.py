import xml.dom.minidom
import xml.etree.ElementTree as ET
#import xmltodict

##下載檔案
# 下載檔案
#import urllib.request
#import zipfile
##下載檔案
#res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
#urllib.request.urlretrieve(res, "./data/example.zip")
#f = zipfile.ZipFile('./data/example.zip')
#f.extractall('./data')

import os, sys

# 打开文件
data=[]
dirs = os.listdir( './data' )

# 输出所有文件和文件夹

for file in dirs:
    #print(file)
    a="./data/"+file
    #print(os.path.splitext(file)[1])
    #if os.path.splitext(file)[1]==".xml":
    #   # if file=="09007_Week24_CH.xml" :
    #   doc = xml.dom.minidom.parse("./data/"+file)
    if os.path.splitext(file)[1]==".xml":
        with open(a, "r",encoding="utf-8") as fdd:
            xml = fdd.read()
            if "高雄"  in xml:
                data.append(file)
       
    #print(a)  

print(data) 
        
# 讀檔案
#fh = open("./data/64_72hr_CH.xml", "r",encoding="utf-8")
#xml = fh.read()
#fh.close()
#
#print(xml)
##第一種
## 存取檔案
#doc = xml.dom.minidom.parse("./data/sample.xml")
#
## 存取我們的資訊
#print(doc.getElementsByTagName("Title")[0].firstChild.nodeValue)
#
## 用迴圈存取我們的資訊
#chapters = doc.getElementsByTagName("Chapter")
#for chapter in chapters:
#    print (chapter.getAttribute('name'), chapter.firstChild.nodeValue)

##第二種
## 存取檔案
#tree = ET.parse('./data/sample.xml') 
#root = tree.getroot()
#
## 存取我們的資訊
#print(root[0].text)
#
## 用迴圈存取我們的資訊
#chapters = root[2]
#for chapter in chapters:
#    print (chapter.attrib['name'], chapter.text)    

##第三種
# 存取檔案

#with open('./data/sample.xml', "r",encoding="utf-8") as fd:
#    doc = dict(xmltodict.parse(fd.read()))
#
## 存取我們的資訊
#print(doc['CUPOY']['Title'])
#
## 用迴圈存取我們的資訊
#chapters = doc['CUPOY']['Chapters']['Chapter']
#for chapter in chapters:
#    print (chapter['@name'], chapter['#text'])