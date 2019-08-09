

def readable_sec(seconds):
    """
    :param seconds: int seconds
    :returns: string e.g. 12 days, 4 hours, 3 min, 4 sec
    """
    c = int(c)
    days = (c // 86400)
    hours = (c // 3600) % 24
    minutes = (c // 60) % 60
    seconds = c % 60
    result = ""
    if days > 0:
        result += str(days) + " days, "
    if hours > 0:
        result += str(hours) + " hrs, "
    if minutes > 0:
        result += str(minutes) + " min, "
    result += str(seconds) + " sec"
    return result