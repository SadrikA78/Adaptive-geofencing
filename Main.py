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
import xlwt
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0
s = sched.scheduler(time.time, time.sleep)
latitude1= "59.949354"
longitude1="30.313432"
#s = "01-12-2011 21:23:11"
#print int(time.mktime(datetime.datetime.strptime(s, "%d-%m-%Y %H:%M:%S").timetuple()))


#https://vk.com/dev/users.getNearby?params[latitude]=30.313496&params[longitude]=59.938531&params[timeout]=7200&params[radius]=1&params[v]=5.68
#https://vk.com/dev/places.getCheckins?params[latitude]=59.943136&params[longitude]=30.476495&params[offset]=3&params[count]=50&params[friends_only]=0&params[need_places]=0&params[v]=5.68
#https://vk.com/dev/places.getCheckins?params[latitude]=59&params[longitude]=30&params[offset]=3&params[count]=3&params[timestamp]=1503767399&params[friends_only]=0&params[need_places]=0&params[v]=5.68
def get_vk(latitude,longitude):


    get_request =  '/method/places.getCheckins?latitude=' + latitude
    get_request+= '&longitude=' + longitude
    get_request+= '&offset=3&count=100&friends_only=0&need_places=0&v=5.68'
    get_request+= '&access_token='

    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)

    a=local_connect.getresponse().read()

    return a
"""
cc=get_vk(latitude1,longitude1)
p = ast.literal_eval(cc)
i=1
mydict={}
data=list()
data1=list()
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.write(0, 0,'id',style0)
ws.write(0, 1,'date',style0)
ws.write(0, 2,'text',style0)
if 'response' in p:
    while i < len(p['response']['items']):
        if 'text' in p['response']['items'][i]:
            a='https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))+'@@@'+str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S'))+ '@@@' + (p['response']['items'][i]['text']).decode('utf8')
            ws.write(i, 0, str('https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))))
            ws.write(i, 1, str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
            ws.write(i, 2,(p['response']['items'][i]['text']).decode('utf8'))
        else:
            a='https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))+'@@@'+str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S'))
            ws.write(i, 0, str('https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))))
            ws.write(i, 1, str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
        #print i, a
        i=i+1


        
    #print type(p['response']['count'])
    #print p['response']['items'][0]['user_id']['text']['place_id']['post_id']['date']
    #print str(int(p['response']['items'][0]['user_id']))
    #print (p['response']['items'][0]['text']).decode('utf8')
    #print type(p['response']['items'][0]['date'])
    #print datetime.datetime.fromtimestamp(int(p['response']['items'][0]['date'])).strftime('%d-%m-%Y %H:%M:%S')
wb.save('example.xls')
"""
distance1=300
min_timestamp1=int(time.mktime(datetime.datetime.strptime("26-08-2017 18:00:00", "%d-%m-%Y %H:%M:%S").timetuple()))
max_timestamp1=int(time.mktime(datetime.datetime.strptime("26-08-2017 21:00:00", "%d-%m-%Y %H:%M:%S").timetuple()))
def get_vk_foto(location_latitude, location_longitude, distance, min_timestamp, max_timestamp):
    get_request =  '/method/photos.search?lat=' + str(location_latitude)
    get_request+= '&long=' + str(location_longitude)
    get_request+= '&count=300'
    get_request+= '&radius=' + str(distance)
    get_request+= '&start_time=' + str(min_timestamp)
    get_request+= '&end_time=' + str(max_timestamp)
    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    return local_connect.getresponse().read()
ccc=get_vk_foto(latitude1, longitude1, distance1, min_timestamp1, max_timestamp1)
pp = ast.literal_eval(ccc)
j=1
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.write(0, 0,'x',style0)
ws.write(0, 1,'y',style0)
ws.write(0, 2,'time',style0)
ws.write(0, 3,'id',style0)
ws.write(0, 4,'fotolink',style0)
f = open('helloworld3333.html','w')
xx=list()
yy=list()
#file_inst = open('vk GEO:'+str(location_latitude)+str(location_longitude)+'.html','w')
#file_inst.write('<html>')
if 'response' in pp:
    #print pp['response'][0]
    #print pp['response'][1]['src_small']

    while j < 287:#int(pp['response'][0])
        y=str(pp['response'][j]['long'])
        x=str(pp['response'][j]['lat'])
        print j, y
        yy.append(y)
        xx.append(x)

             

        ws.write(j, 0, x)
        ws.write(j, 1, y)
        ws.write(j, 2, str(datetime.datetime.fromtimestamp(int(pp['response'][j]['created'])).strftime('%d-%m-%Y %H:%M:%S')))
        ws.write(j, 3, str(int(pp['response'][j]['owner_id'])))
        ws.write(j, 4, str(pp['response'][j]['src_small']))                      
        print j, pp['response'][j]['src_small']
        #file_inst.write('<br>')
        j=j+1
#print yy
iii=0
while iii < 27:
    #print xx[iii]
    markersCode11 = "\n".join(
            [ """new google.maps.Marker({{
                position: new google.maps.LatLng({lat}, {lon}),
                map: map
            }});""".format(lat=xx[iii], lon=yy[iii])
               ])
    iii=iii+1
markersCode ="""
            <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
            <div id="map-canvas" style="height: 100%; width: 100%"></div>
            <script type="text/javascript">
                var locations = [
    ['<p align="center"><b>ОРКЕСТР</b></p><video width="400" height="300" controls="controls" poster="22.jpg"><source src="4.mp4"></video>', 59.932461, 30.326791, 3],
	['<p align="center"><a href="https://vk.com/id560561"><b>Ссылка</b></a><p align="center"><b>27-08-2017 00:32:12</b></p><p align="center">Если можно, то мне эспрессо</p></p><p><IMG BORDER="0" ALIGN="Left" SRC="22.jpg"></p>', 59.932463, 30.329791, 2],
      ['<p align="center"><b>АЭРОПОРТ</b></p><iframe width="130" height="100" src="https:\\/\\/pp.userapi.com\\/c840423\\/v840423691\\/953\\/isvd4y_st_Q.jpg" frameborder="0" allowfullscreen></iframe>', 59.933572, 30.329791, 1]
    ];

                var map;
                function show_map() {{
                    map = new google.maps.Map(document.getElementById("map-canvas"), {{
                        zoom: 16,
                        center: new google.maps.LatLng({centerLat}, {centerLon})
                    }});
                    {markersCode}
                }}
                google.maps.event.addDomListener(window, 'load', show_map);
            </script>
""".format(centerLat=latitude1, centerLon=longitude1, markersCode=markersCode11)
f.write(markersCode)
f.close()
wb.save('coordinate2.xls')
