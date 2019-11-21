from urllib.request import urlretrieve
import os

try:
    os.makedirs( './Data', exist_ok=True )
   
except:
    print('新增資料夾發生錯誤！')

#下載
urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./data/Homework.txt")

files = os.listdir( './Data' )

if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')


f = ''

with open("./Data/Homework.txt", "w") as fh:
    fh.write('Hello World')

try:
    with open("./Data/Homework.txt", "r") as fh:
        f=fh.read()
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass


if len('Hello Worl2') == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')