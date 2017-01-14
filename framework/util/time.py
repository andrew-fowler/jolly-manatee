from time import strftime, gmtime


def current_time():
    return str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))