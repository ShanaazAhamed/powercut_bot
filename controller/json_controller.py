import json


def getTimes():
    times = []
    with open("data.json", 'r') as json_obj:
        data = dict(json.load(json_obj))
        times = list(data.values())
    # print(times)
    return times


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


if __name__ == "__main__":
    times = get_interrupt_times()
    print(times)
