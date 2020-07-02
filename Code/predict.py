import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from Data_Preprocessing import *
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import accuracy_score
from model import *
import requests
from bs4 import BeautifulSoup
import datetime
import time

#tiến hành đọc dữ liệu đầu vào từ giao diện sau đó tiến hành các bước pre_processing dữ liệu văn bản
def Predict_data(input): 
    a = []
    a.append([])
    a[0].append(input)
    text = pre_processing(a)
    model1 = pickle.load(open("model.p", 'rb'))
    number = pickle.load(open("number.p", 'rb'))
    prediction = model1.predict(text)
    prediction = number.inverse_transform(prediction)
    prediction1 = str(prediction)
    prediction1 = prediction1.replace("['", "")
    prediction1 = prediction1.replace("']", "")
    return prediction1

#hàm kiểm tra năm nhuận
def leap_year(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return 1
        else:
            return 0
    elif (year % 4 == 0):
        return 1
    else:
        return 0

#hàm lùi về 1 ngày từ thời gian cho trước
def decrease_time(day, month, year):
    day1 = day
    month1 = month
    year1 = year
    if (day==1):
        if (month == 2 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11):
            month1 = month-1
            day1 = 31
        elif (month == 1):
            month1 = 12
            day1 = 31
            year1 = year - 1
        elif (month == 5 or month == 7 or month == 10 or month == 12):
            month1 = month-1
            day1 = 30
        elif (month == 3):
            month1 = 2
            if (leap_year(year)==1):
                day1 = 29
            else:
                day1 = 28
    else:
        day1 = day-1
    return day1, month1, year1

#lấy link bài viết mới nhất từ trang web The Sun
def url_the_sun(year, month, day):
    if (month<10):
        month = "0"+str(month)
    else:
        month = str(month)
    if (day<10):
        day = "0"+str(day)
    else:
        day = str(day)
    URL = "https://www.thesun.co.uk/sitemap.xml?yyyy="+str(year)+"&mm="+str(month)+"&dd="+str(day) # đổi ngày và tháng để cập nhật mới nhất
    requests.get(URL)
    web_page = BeautifulSoup(requests.get(URL, {}).text, "lxml")
    test = web_page.find_all("loc")
    url1=[]
    for i in range(len(test)):
        tr=str(test[i])
        tr1=tr.replace("<loc>","")
        tr2=tr1.replace("</loc>","")
        url1.append(tr2)
    return url1

#lấy link bài viết mới nhất từ trang web telegraph
def url_telegraph_1(link1):
    URL2 = link1
    requests.get(URL2)
    web_page = BeautifulSoup(requests.get(URL2, {}).text, "lxml")
    test = web_page.find_all("loc")
    return test

def url_telegraph(test_link):
    test1 = str(test_link)
    test1 = test1.replace("<loc>", "")
    test1 = test1.replace("</loc>", "")
    requests.get(test1)
    web_page = BeautifulSoup(requests.get(test1, {}).text, "lxml")
    test_web = web_page.find_all("loc")
    url3=[]
    for j in range(len(test_web)):
        tr=str(test_web[j])
        tr1=tr.replace("<loc>","")
        tr2=tr1.replace("</loc>","")
        url3.append(tr2)
    return url3

#lấy danh sách link theo lựa chọn từ combobox trong giao diện, sl_link 
def list_link(link, sl_link):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    list_links = []
    link1 = link
    count = 0
    url1 = [] 
    count1 = 0
    start_time = time.time()
    seconds = 7
    if (sl_link == "The Sun"):
        while (count1==0):
            url1 = url_the_sun(year, month, day)
            for i in range(len(url1)):
                if (link1 in url1[i]):
                    count1+=1
            if (count1!=0):
                break
            else:
                day, month, year = decrease_time(day, month, year)
        while (count<10):
            for i in range(len(url1)):
                if count>9:
                    break
                if ((link1 in url1[i])==True):
                    count+=1
                    list_links.append(url1[i])
                    print(url1[i])
            if (count > 10):
                break
            day, month, year = decrease_time(day, month, year)
            url1 = url_the_sun(year, month, day)
            current_time = time.time()
            elapsed_time = current_time - start_time
            if (elapsed_time > seconds):
                break
        return list_links
    else:
        count2 = 10
        i = 0
        test = url_telegraph_1(link1)
        start_time = time.time()
        seconds = 7
        while (count2>=0):
            link2 = test[i]
            url3 = url_telegraph(link2)
            link1 = link1.replace("/sitemap.xml", "")
            i+=1
            for j in range(0, len(url3)-1):
                if (count2==0):
                    break
                if (link1 in url3[j])==True:
                    count2-=1
                    list_links.append(url3[j])
            current_time = time.time()
            elapsed_time = current_time - start_time
            if (elapsed_time > seconds):
                break
    return list_links

#hàm trả về danh sách link dựa trên chủ đề dự đoán được
def Link_Suggestion(prediction, sl_link):
    if (prediction=='tvshowbiz'):
        return list_link("https://www.thesun.co.uk/tvandshowbiz/", sl_link)
    if (prediction=='femail' and sl_link):
        if (sl_link=="The Sun"):
            return list_link("https://www.thesun.co.uk/femail/", sl_link)
        elif (sl_link=='Telegraph'):
            return list_link("https://www.telegraph.co.uk/women/sitemap.xml", sl_link)
    if (prediction =='films'):
        if (sl_link=="The Sun"):
            return list_link("https://www.thesun.co.uk/films/", sl_link)
        elif (sl_link=='Telegraph'):
            return list_link("https://www.telegraph.co.uk/films/sitemap.xml", sl_link)
    if (prediction == 'health'):
        if (sl_link=="The Sun"):
            return list_link("https://www.thesun.co.uk/fabulous/health-and-fitness/", sl_link)
        elif (sl_link=='Telegraph'):
            return list_link("https://www.telegraph.co.uk/global-health/sitemap.xml", sl_link)
    if (prediction == "lifestyle"):
            return list_link("https://www.telegraph.co.uk/lifestyle/sitemap.xml", sl_link)
    if (prediction == 'sport'):
        if (sl_link=="The Sun"):
            return list_link("https://www.thesun.co.uk/sport/", sl_link)
        elif (sl_link=='Telegraph'):
            return list_link("https://www.telegraph.co.uk/sport/sitemap.xml", sl_link)
    if (prediction == 'technology'):
        if (sl_link=="The Sun"):
            return list_link("https://www.thesun.co.uk/tech/", sl_link)
        elif (sl_link=='Telegraph'):
            return list_link("https://www.telegraph.co.uk/technology/sitemap", sl_link)
    if (prediction=='travel'):
        if (sl_link=="The Sun"):
            return list_link("https://www.thesun.co.uk/travel", sl_link)
        elif (sl_link=='Telegraph'):
            return list_link("https://www.telegraph.co.uk/travel/sitemap.xml", sl_link)