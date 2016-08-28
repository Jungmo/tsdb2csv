# -*- coding: utf-8 -*-

import csv
import func
import dataprocess as dp

import easygui

#TODO:get metric name on GUI from HTTP API
# http://serverurl/api/suggest?type=metrics&max=20
#metric = ["wearable.hr", "wearable.acc_x", "wearable.acc_y", "wearable.acc_z"]
metric = "0828still"
tag = ["hr", "x", "y", "z"]
#FIXME:Sometimes easygui doesn't work well. Use tkinter.
# http://stackoverflow.com/questions/29783090/how-to-use-the-calendar-module-with-tkinter
#start_date = easygui.enterbox('start_date (YYYY/MM/DD-hh:mm:ss) : ')
#end_date = easygui.enterbox('end_date (YYYY/MM/DD-hh:mm:ss) : ')

start_date = "1d-ago" #""2016/08/05-16:23:00"
end_date = "1s-ago" #"2016/08/05-16:30:00"

server_url = "http://202.30.29.209:14242/" # OpenTSDB Server Address
query_url = "api/query?start="+start_date+"&end="+end_date+"&m=sum:"+metric

url = []

for i in range(0,len(tag)):
    url.append(server_url+query_url+"{host="+tag[i]+"}")

hr = dp.metric(url[0])
acc_x = dp.metric(url[1])
acc_y = dp.metric(url[2])
acc_z = dp.metric(url[3])


print "Set minimum and maximum timestamp"
mints = min(min(hr.value.keys()),
            min(acc_x.value.keys()),
            min(acc_y.value.keys()),
            min(acc_z.value.keys()))

maxts = max(max(hr.value.keys()),
            max(acc_x.value.keys()),
            max(acc_y.value.keys()),
            max(acc_z.value.keys()))
print "mints : ", mints,"maxts : ",maxts

# From mints to maxts


f = open('../output/file.csv','wb')

writer = csv.writer(f, delimiter=',')
writer.writerow(['unix_ts','real_ts']+tag)

#TODO: Handle 'invalild key' situation
for i in range(int(mints), int(maxts)):
    ts = str(i).decode("utf-8")
    try:
        writer.writerow([ts, func.unixtime2realtime(ts), hr.value[ts], acc_x.value[ts], acc_y.value[ts], acc_z.value[ts]])
    except KeyError:
        print ts ,"error"