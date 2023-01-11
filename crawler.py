import urllib.request as urllib2
from html.parser import HTMLParser

class HtmlParser(HTMLParser):

    def reset_values(self):
        self.table_start = False
        self.table = []
        self.current_row = 0
        self.current_col = 0

    def handle_starttag(self, tag, attrs):
        if tag == "tbody" and not self.table_start:
            self.table_start = True

        if not self.table_start:
            return

        if tag == "tr":
            self.table.append([])
            self.current_col = 0

        if tag == "td":
            self.table[self.current_row].append("")


    def handle_endtag(self, tag):

        if tag == "tbody" and self.table_start:
            self.table_start = False

        if not self.table_start:
            return

        if tag == "tr":
            self.current_row += 1

        if tag == "td":
            self.current_col += 1

    def handle_data(self, data):
        if not self.table_start:
            return
        self.table[self.current_row][self.current_col] += data


class BnrCrawler:
    parser = HtmlParser()
    url = "https://www.bnr.ro/Cursul-de-schimb-524-Mobile.aspx"

    def run(self):
        self.parser.reset_values()
        self.parser.reset()
        request = urllib2.urlopen(self.url)
        raw_page: str = request.read()
        self.page = raw_page.decode("utf-8")
        self.parser.feed(self.page)

        result = {}
        for row in self.parser.table:
            result[row[1]] = [float(i.replace(",", ".")) for i in row[2:7]]
        return result
