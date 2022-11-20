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
