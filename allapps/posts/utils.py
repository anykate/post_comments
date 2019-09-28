from django.utils.text import slugify
import datetime


def calc_slug(title):
    year = str(datetime.datetime.now().date().year)

    # month = str(datetime.datetime.now().date().month)
    month = str(datetime.datetime.now().date().strftime("%m"))

    # day = str(datetime.datetime.now().date().day)
    day = str(datetime.datetime.now().date().strftime("%d"))

    # hour = str(datetime.datetime.now().hour)
    hour = str(datetime.datetime.now().strftime("%H"))

    # minute = str(datetime.datetime.now().minute)
    minute = str(datetime.datetime.now().strftime("%M"))

    # second = str(datetime.datetime.now().second)
    second = str(datetime.datetime.now().strftime("%S"))

    time = year + ' ' + month + ' ' + day + \
        ' ' + hour + ' ' + minute + ' ' + second

    return slugify(title + ' ' + time)
