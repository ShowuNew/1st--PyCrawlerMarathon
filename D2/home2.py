import urllib.request
import os, sys
try:
    os.makedirs( './Data', exist_ok=True )
   
except:
    print('新增資料夾發生錯誤！')
res = "http://pycrawler.cupoy.com/file-download/part02/example.csv"
urllib.request.urlretrieve(res, './data/example.csv')

print('111')


# 打开文件
#dirs = os.listdir( './data' )

# 输出所有文件和文件夹
#for file in dirs:
#    print(file)


   
fh = open("./data/example.csv")

f = fh.read()
#fh.close()
#os.system("pause")

print(f)
