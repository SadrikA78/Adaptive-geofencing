import xlwt
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.write(0, 0,'id',style0)
ws.write(0, 1,'date',style0)
ws.write(0, 2,'text',style0)
if 'response' in p:
    while i < len(p['response']['items']):
        if 'text' in p['response']['items'][i]:
            #a='https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))+'@@@'+str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S'))+ '@@@' + (p['response']['items'][i]['text']).decode('utf8')
            ws.write(i, 0, str('https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))))
            ws.write(i, 1, str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
            ws.write(i, 2,(p['response']['items'][i]['text']).decode('utf8'))
        else:
            #a='https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))+'@@@'+str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S'))
            ws.write(i, 0, str('https://vk.com/id'+str(int(p['response']['items'][i]['user_id']))))
            ws.write(i, 1, str(datetime.datetime.fromtimestamp(int(p['response']['items'][i]['date'])).strftime('%d-%m-%Y %H:%M:%S')))
        i=i+1
wb.save('example.xls')
