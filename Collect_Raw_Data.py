# coding: utf8
import calendar
import time
import datetime
import httplib
import urllib
import json
import ast
import csv
import sys
import codecs
import sched, time
import threading

latitude1= ""
longitude1=""
radius1=""
access_token=""

def get_vk(latitude,longitude,radius):


    get_request =  '/method/places.getCheckins?latitude=' + latitude
    get_request+= '&longitude=' + longitude
    get_request+= '&offset=3&count=100&friends_only=0&need_places=0&v=5.68'
    et_request+= '&access_token='+ access_token
    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    a=local_connect.getresponse().read()
    return a

cc=get_vk(latitude1,longitude1)
p = ast.literal_eval(cc)
i=1
data=list()
if 'response' in p:
   
    while i < len(p['response']['items']):
        if 'text' in p['response']['items'][i]:
            a='https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))+u' Время: '+str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S'))+ ' ' + (p['response']['items'][i]['text']).decode('utf8')
            data.append(i)
            data.append('https://vk.com/id'+str(int(p['response']['items'][i]['user_id'])))
            data.append(str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
            #data.append((p['response']['items'][i]['text']).decode('utf8'))
        else:
            a='https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))+u' Время: '+str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S'))
            data.append(i)
            data.append('https://vk.com/id'+str(int(p['response']['items'][i]['user_id'])))
            data.append(str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
        #print data
        with open('test.csv', 'wb') as fp:
            f = csv.writer(fp, delimiter=';')
            f.writerows(data)

                
        i=i+1
