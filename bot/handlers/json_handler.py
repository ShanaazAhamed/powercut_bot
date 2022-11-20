import json


class json_handler():

    def __init__(self):
        self.load_json()

    def load_json(self):
        with open('data.json', 'r') as open_file:
            self.data = json.load(open_file)

    def get_time(self, group):
        try:
            grp = group.upper()
            if (self.data[grp]):
                return self.data[grp]
        except:
            return -1

    def format_data(self):
        new_data = {}
        for key, val in self.data.items():
            new_data[key] = val.split('-')
            new_list = []
            for t in new_data[key]:
                if ',' in t:
                    new_list.extend(t.split(','))
                else:
                    new_list.append(t)
                new_data[key] = new_list

        return new_data

    def get_all_today_time(self):
        new_list = []
        new_data = self.format_data()
        for i in new_data.values():
            for t in i:
                if t not in new_list:
                    new_list.append(t)

        return list(set(new_list))

    def get_groups_by_time(self, t):
        all_times = self.get_all_today_time()
        groups = []
        if t not in all_times:
            return -1
        else:
            new_data = self.format_data()
            for key, values in new_data.items():
                for i in values:
                    if t == i:
                        groups.append(key)

            return list(set(groups))


if __name__ == '__main__':
    obj = json_handler()
    print(obj.get_groups_by_time('3:00AM'))
