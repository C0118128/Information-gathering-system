from modules.scrapTel import ScrapTel
from modules.reader import CsvReader

if __name__ == '__main__':
    # scrap_tel = ScrapTel()
    # scrap_tel.scrapingTel()
    csv_reader = CsvReader()
    csv_contens = csv_reader.readCsv('./input.csv', [0,2])

    for content in csv_contens:
        # self.scraping(content)
        print(content)