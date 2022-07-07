import datetime
import requests
from pdfminer.high_level import extract_text


class LinkAnalyzer():
    def __init__(self, data):
        self.data = data
        self.link_dict = {}

    def collect_links(self):
        links = []
        for link in self.data:
            links.append(link)
        print(f"received links: {self.data}")
        return links

    def review_link(self, link=""):
        if len(link) == 0:
            link = self.data[0]
        try:
            r = requests.get(link)
            if r.ok:
                return True
            else:
                return False
        except:
            return False

    def review_links(self, links=[]):
        if len(links) == 0:
            links = self.data
        for link in links:
            try:
                r = requests.get(link)
                if r.ok:
                    self.link_dict[link] = r.status_code
                else:
                    self.link_dict[link] = f"{r.status_code}: warning"
            except:
                self.link_dict[link] = f"{r.status_code}: fail"
        return self.link_dict

    def clean(self):
        self.data = []
        self.link_dict = {}

    def make_report(self):
        with open("report_date_time_number_of_links.txt", "w") as f:
            for key in self.link_dict:
                now = datetime.datetime.now().strftime("%y-%m-%d_%H:%m")
                f.write("{}>>>{}>>>{}\n".format(now, key, self.link_dict[key]))


class PDFAnalyzer:
    def __init__(self, path):
        self.path = path
        self.text = self.read()
        self.text_turning = self.split_text()
        self.link_analyzer = LinkAnalyzer(self.text_turning)

    def read(self):

        return extract_text(self.path)

    def split_text(self):
        text = []
        text_tmp = self.text.split(" ")
        for str in text_tmp:
            if len(str.strip()) != 0:
                text.append(str.strip())
        return text


pDFAnalyzer = PDFAnalyzer("D:\Links.pdf")

# links = pDFAnalyzer.link_analyzer.collect_links()
# print(f"<<<<<<<{links}>>>>>>>")
# print(pDFAnalyzer.link_analyzer.review_link(links[2]))
print(pDFAnalyzer.link_analyzer.review_links())
pDFAnalyzer.link_analyzer.make_report()

