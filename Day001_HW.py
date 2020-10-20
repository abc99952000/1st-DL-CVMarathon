#!/usr/bin/env python
# coding: utf-8

# # 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？

# 1. 檔案
# 
# 資料包成檔案，格式可能包含CSV、JSON等等
# 
# 2. 開放接口（API）
# 
# 提供程式化的連接的接口，讓工程師/分析師可以選擇資料中要讀取的特定部分，而不需要把整批資料事先完整下載回來
# 
# 3. 網頁爬蟲
# 
# 在網頁上的資料，可以利用爬蟲爬蟲程式，將網頁的資料解析所需的部分。

# # 2.（實作）完成一個程式，需滿足下列需求：
# 
# 「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址：https://www.w3.org/TR/PNG/iso_8859-1.txt 或任一個 .txt 的檔案網址
# 
# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
# 
# 將「Hello World」字串覆寫到 Homework.txt 檔案
# 
# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

# In[28]:


#引入library
from urllib.request import urlretrieve 
import os
#下載檔案
urlretrieve('https://www.w3.org/TR/PNG/iso_8859-1.txt',"C:/Users/abc99/Desktop/Data/Homework.txt")
#開啟Homework並改寫
with open ("C:/Users/abc99/Desktop/Data/Homework.txt",'w') as hw :
    hw.write("Hellow Word")

#讀取並確認字數
with open ("C:/Users/abc99/Desktop/Data/Homework.txt",'r')as hw:
    x = hw.read()
print(len(x))


# In[ ]:




