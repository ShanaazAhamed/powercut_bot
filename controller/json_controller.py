import json


def getTimes():
    times = []
    with open("data.json", 'r') as json_obj:
        data = dict(json.load(json_obj))
        times = list(data.values())
    return times


def getDict():
    with open("data.json", 'r') as json_obj:
        data = dict(json.load(json_obj))
    return data


def get_interrupt_times():
    start_time = []
    for i in getTimes():
        times = i.split(",")
        if len(times) > 1:
            for j in times:
                temp_time = j.split('-')
                start_time.append(temp_time[0])
        else:
            temp_time = times[0].split('-')
            start_time.append(temp_time[0])
    return list(set(start_time))


def get_groups_by_time(time):
    groups = []
    dict_ = dict(getDict())
    for grp, t in dict_.items():
        times = t.split(",")
        if len(times) > 1:
            for j in times:
                temp_time = j.split('-')
                start_time = temp_time[0]
                if start_time == time:
                    groups.append(grp)
        else:
            temp_time = times[0].split('-')
            start_time = temp_time[0]
            if start_time == time:
                groups.append(grp)
    return groups


if __name__ == "__main__":
    times = get_interrupt_times()
    groups = get_groups_by_time('6:00PM')
    print(groups)
