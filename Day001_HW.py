#!/usr/bin/env python
# coding: utf-8

# In[27]:


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

