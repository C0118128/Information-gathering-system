from reader import CsvReader
from webdriver import Chrome


class ScrapTel:
    # def scraping(self, content):
        # url = 'https://itp.ne.jp/'
        # ch = Chrome()
        # driver = ch.driver
        # driver.get(url)

    
    def scrapingTel(self):
        csv_reader = CsvReader()
        csv_contens = csv_reader.readCsv('./input.csv', [0,2])

        for content in csv_contens:
            # self.scraping(content)
            print(content)