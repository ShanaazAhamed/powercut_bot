from datetime import datetime


def format_time(t):
    time_string = t.strftime("%I:%M%p")
    if time_string[0] == '0':
        return time_string[1:]
    else:
        return time_string


def get_now():
    now = datetime.today()
    return format_time(now)


def to_twenty_four(time):
    in_time = datetime.strptime(time, "%I:%M%p")
    out_time = datetime.strftime(in_time, "%H:%M")
    return out_time


def before_an_hour(time):
    time = time.strip()
    hour, minute_p = time.split(":")
    minute = minute_p[:2]
    p = minute_p[2:].strip()
    hour = int(hour)
    if hour > 1 and hour < 12:
        hour -= 1
    elif hour == 1:
        hour = 12
    elif hour == 12:
        hour -= 1
        if p == "AM":
            p = "PM"
        else:
            p = "AM"
    new_time = f"{str(hour)}:{str(minute)}{p}"

    return new_time


if __name__ == "__main__":
    now = get_now()
    sub = before_an_hour('12:01AM')
    print(before_an_hour('6:00PM'))
    # print(sub)
