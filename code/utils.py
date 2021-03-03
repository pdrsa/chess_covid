from datetime import datetime

# Receives a unix time format and returns a string in ISO format
def toDate(unix):
    return datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')

