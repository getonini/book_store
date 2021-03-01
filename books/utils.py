import datetime


def days_between_today_and_param(date_param):
    delta = datetime.datetime.today().date() - date_param.date()
    return delta.days
