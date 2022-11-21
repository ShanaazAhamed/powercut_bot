from datetime import datetime


def format_time(t):
    time_string = t.strftime("%I:%M%p")
    if time_string[0] == '0':
        return time_string[1:]
    else:
        return time_string


def get_now():
    now = datetime.today()
    return format_time(datetime.today())


if __name__ == "__main__":
    now = get_now()
    print(now)
