import re

import time


def matchDate(date):
    mat = re.search(r"(\d{1,2}月\d{1,2}日)", date)
    date = mat.group(0)
    year = time.strftime('%Y', time.localtime(time.time()))
    month = re.findall(r"\d+\.?\d*", date)[0]
    day = re.findall(r"\d+\.?\d*", date)[1]
    result = year + "-" + month + "-" + day
    return result


if __name__ == '__main__':
    date = "07月6日  星期五"
    matchDate(date)
