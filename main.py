import lxml.html
import scraper as sc
import requests


class Scraping:

    def __init__(self):
        self.url = ['http://www.doggiepubs.org.uk/the_pubs.php?searchtown=York&lat=53.95996510000001&long=-1.0872979000000669&view=list', 'http://www.doggiepubs.org.uk/the_pubs.php?searchtown=Worcester&lat=52.193636&long=-2.22157500000003&view=list']
        self.data = []

    def get_data(self):
        for link in self.url:
            self.source = requests.get(link)
            self.tree = lxml.html.fromstring(self.source.content)
            self.etree = self.tree.xpath('//div[@class="tabs-content"]/div//div[@id="searchresultholder"]')
            for element in self.etree:
                self.name = sc.get_text(element.xpath('.//div[@id="pubnameholder"]/p/text()'))
                self.post_code = sc.get_text(element.xpath('.//div[@id="searchtextholder"]/p/text()[2]'))
                self.phone = sc.get_text(element.xpath('.//div[@id="searchtextholder"]/p/text()[3]'))
                print(self.name, '\t', self.post_code, '\t', self.phone)
                self.data.append([self.name, self.post_code, self.phone])
        sc.Database(('name', 'post-code', 'phone')).push_data(self.data)


Scraping = Scraping()
Scraping.get_data()