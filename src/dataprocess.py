import json
import urllib

import func

class metric:
    def __init__(self, url):
        response = urllib.urlopen(url);
        resp_json = response.readline()
        resp_json = resp_json[1:-1]
        json_data = json.loads(resp_json)

        print json_data
        self.metric_name = json_data["metric"]
        self.value = json_data["dps"]
        self.value = func.dict_sort(self.value)

        print "Metric : " + self.metric_name +" is loaded."