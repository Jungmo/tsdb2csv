import tsdb
import easygui as eg

def getParameterFromGUI():
    # GUI
    metric_require_message = "Please select a metric."
    metric_require_title = "Choice a metric"
    metric_list = tsdb.getMetricList()
    chosen_metric = eg.choicebox(metric_require_message,metric_require_title,metric_list)
    print chosen_metric

    tags_number_require_message = "Please input number of tags"
    tags_number = 0
    tags_number = eg.enterbox(tags_number_require_message, tags_number_require_message)
    print tags_number

    tags_require_message = "Please input tags."
    tags_require_title = "Input tags."
    tags_require_fieldNames = []
    for i in range(0, int(tags_number)):
        tags_require_fieldNames.append("TAG"+str(i))
    tags_require_fieldValues = []
    tags_require_fieldValues = eg.multenterbox(tags_require_message, tags_require_title, tags_require_fieldNames)


    start_require_message = "Please input start time."
    start_require_title = "Input start time"
    ts_require_fieldNames = ["Year", "Month", "Day", "Hour(24)", "Minute", "Second"]
    start_require_fieldValues = []
    start_require_fieldValues = eg.multenterbox(start_require_message, start_require_title, ts_require_fieldNames)

    end_require_message = "Please input end time."
    end_require_title = "Input end time"
    end_require_fieldValues = []
    end_require_fieldValues = eg.multenterbox(end_require_message, end_require_title, ts_require_fieldNames)

    start_date = start_require_fieldValues[0]+"/"+start_require_fieldValues[1]+"/"+start_require_fieldValues[2]\
                 +"-"+start_require_fieldValues[3]+":"+start_require_fieldValues[4]+":"+start_require_fieldValues[5]
    end_date = end_require_fieldValues[0] + "/" + end_require_fieldValues[1] + "/" + end_require_fieldValues[2]\
               + "-" + end_require_fieldValues[3] + ":" + end_require_fieldValues[4] + ":" + end_require_fieldValues[5]


    ret = [chosen_metric, start_date, end_date, tags_require_fieldValues]
    return ret