# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:44:58 2020

@author: C09700
"""

import pandas as pd
# %%
df = pd.read_csv('./data/Test.csv', infer_datetime_format=True)


df['start_time'] = pd.to_datetime(df['start_time'], format="%Y-%m-%d %H:%M:%S")
df['end_time'] = pd.to_datetime(df['end_time'], format="%Y-%m-%d %H:%M:%S")

df['login_hour'] = df['start_time'].dt.strftime('%Y-%m-%d %H')
df['logout_hour'] = df['end_time'].dt.strftime('%Y-%m-%d %H')

# 只保留小時部分
df_new = df[['start_time','end_time','login_hour','logout_hour']].sort_values(by='start_time')

# %%
import pandas as pd
from interval import Interval
from dateutil.parser import parse
from datetime import timedelta  
from datetime import datetime

hr_list = ['00','01','02','03','04',
            '05','06','07','08','09',
            '10','11','12','13','14',
            '15','16','17','18','19',
            '20','21','22','23']

startDate_str = '2020-03-18'

time_zoom = {}
# 年-月-日 小時  共24*7 168個日期小時區間
for i in range(7):
    startDate = (parse(startDate_str) + timedelta(days = i)).strftime("%Y-%m-%d")
    for h in hr_list:
        d = parse("{} {}".format(startDate, h))
        d_str = d.strftime("%Y-%m-%d %H")
        time_zoom[d_str] = 0
      
# df = pd.read_csv('sample.csv')        
log_list = df_new[['login_hour','logout_hour']].values.tolist()

for log in log_list:
    # 每筆資料的登入登出、時間
    st = log[0]
    et = log[1]
    
    zoom = Interval(st, et )
    
    key_list = []
    for k, v in time_zoom.items():
        if k in zoom:
            # 該小時區間次數+1
            time_zoom[k]+=1

dictlist = []
for key, value in time_zoom.items():
    temp = [key,value]
    dictlist.append(temp)
# %%
import csv

# 開啟輸出的 CSV 檔案
with open('W13_2020_03_25_loginTimes_hour.csv', 'w', newline='') as csvFile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvFile)
    
    # 1.直接寫出-標題
    writer.writerow(['date_hour','times'])
    for dh, c in dictlist:
        writer.writerow([dh, c])
