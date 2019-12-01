import urllib.request
import os, sys
import csv
try:
    os.makedirs( './Data', exist_ok=True )
   
except:
    print('新增資料夾發生錯誤！')
res = "http://pycrawler.cupoy.com/file-download/part02/example.csv"
urllib.request.urlretrieve(res, './data/example.csv')


#open(WAVE_FILE, "r",encoding="utf-8")
#fh = open("./data/example.csv","r",encoding="utf-8")

#f = fh.read()
#str1 = fh.read(10)
#fh.close()

#print(f)



#with open('./data/example.csv', newline='',encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    #rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    
    #for row in rows:
    #    print(row)
    # listem=[]
    # licount=['班次1','班次2','班次3','班次4','班次5']
    # aa = -1
    # for row in rows:
    #   if '班次1' in row:
    #     for index,item in enumerate(row):
    #         if '班次1' == item:
    #             aa = index
    #             print(aa)
    #   elif aa !=-1:
    #     listem.append(row[aa])
    #     print(row[aa])

    #print(listem)
   
 
   
listem=[]
licount=['班次1','班次2','班次3','班次4','班次5']
data={}
aa = -1
for li in licount:
    with open('./data/example.csv', newline='',encoding="utf-8") as csvfile:
         # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        for row in rows:
              if li in row:
                  for index,item in enumerate(row):
                        if li == item:
                            aa = index
              elif aa !=-1:
                  listem.append(row[aa])
                  
        data[li]=listem[1:]
        aa=-1
        listem=[]
        #print(li)
print(data)


# 打开文件
#dirs = os.listdir( './data' )

# 输出所有文件和文件夹
#for file in dirs:
#    print(file)


   
#fh = open("./data/example.csv","r")
# 變數 lines 會儲存 filename.txt 的內容
#lines = fh.readlines()
#
#for line in iter(fh):
#    print(line)
#fp.close()
#print(len(lines))
#fh.close()
# print content
#for i in range(len(lines)):
#     print(lines[i])

#f = fh.read()
#fh.close()
#os.system("pause")

#print(f)
