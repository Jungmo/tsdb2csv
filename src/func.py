import collections

import time

import datetime


def dict_sort(dict):
    od = collections.OrderedDict(sorted(dict.items()))
    return od


# ----- time converter ------
def realtime2unixtime(realtime):
    ts = time.mktime(datetime.datetime.strptime(realtime, "%Y/%m/%d-%H:%M:%S").timetuple())
    return ts

def unixtime2realtime(unixtime):
    ts =  datetime.datetime.fromtimestamp(int(unixtime)).strftime('%Y/%m/%d-%H:%M:%S')
    return ts