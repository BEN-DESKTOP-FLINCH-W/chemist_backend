from datetime import datetime

def timestamp_conversion():
    unformated_time=datetime.now()
    formated_time=unformated_time.strftime("%Y%m%d%H%M%S")
    return formated_time