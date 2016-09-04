import json
import urllib
import csv
import func
import dataprocess as dp

url_suggest = "http://202.30.29.209:14242/api/suggest?type=metrics"

def getMetricList():
    response = urllib.urlopen(url_suggest);
    resp_json = response.readline()
    json_data = json.loads(resp_json)
    print "Get metrics from server!"

    return json_data

def getData(metric, start_date, end_date, tags):

    server_url = "http://202.30.29.209:14242/" # OpenTSDB Server Address
    query_url = "api/query?start="+start_date+"&end="+end_date+"&m=sum:"+metric

    url = []

    for i in range(0,len(tags)):
        url.append(server_url+query_url+"{sensor="+tags[i]+"}")

    #TODO : FIX HERE - Dynamically input
    for i in range(0, len(tags)):
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
    writer.writerow(['unix_ts','real_ts']+tags)

    #TODO: Handle 'invalild key' situation
    for i in range(int(mints), int(maxts)):
        ts = str(i).decode("utf-8")
        try:
            writer.writerow([ts, func.unixtime2realtime(ts), hr.value[ts], acc_x.value[ts], acc_y.value[ts], acc_z.value[ts]])
        except KeyError:
            print ts ,"error"