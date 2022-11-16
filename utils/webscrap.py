from selenium import webdriver
from bs4 import BeautifulSoup
from json import dumps


class WebScrap:
    def __init__(self, url):
        self.__url = url

    def get_content(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        browser = webdriver.Chrome(options=op)
        browser.get(self.__url)
        html = browser.page_source
        browser.close()
        return html

    def get_soup(self, html_elem, html_cls):
        content = self.get_content()
        soup = BeautifulSoup(content, "html.parser")
        return soup.find_all(html_elem, class_=html_cls)

    def json_export(self, data_list):
        class_time_dict = {}
        for i in range(0, len(data_list)-1, 2):
            time = [j for j in data_list[i].text]

            for t in range(len(time)):
                if time[t] == "M":
                    time.insert(t+1, "-")
                    break

            if data_list[i+1].text not in class_time_dict.keys():
                class_time_dict[data_list[i+1].text] = "".join(time)
            else:
                prev_time = class_time_dict[data_list[i+1].text]
                class_time_dict[data_list[i +
                                          1].text] = prev_time + ","+"".join(time)

        with open("data.json", "w") as outfile:
            outfile.write(dumps(class_time_dict))


if __name__ == "__main__":
    url = "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule"
    web_scrap = WebScrap(url)
    data = web_scrap.get_soup('span', 'fw-500')
    web_scrap.json_export(data)

    [print(i.text) for i in data]
    print(len(data)/2)
