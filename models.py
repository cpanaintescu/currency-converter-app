import json
from crawler import BnrCrawler

class AppModel:
    data = {}
    valutes_list = []

    def __init__(self):
        crawler = BnrCrawler()
        self.data = crawler.run()
        self.data['RON'] = [1] * 5
        self.valutes_list = list(self.data)

    def save_data(self, data):
        with open("values.json", "w") as file:
            json.dump(data, file, indent=2)

    def open_data(self):
        with open("values.json", "r") as file:
            return json.load(file)
