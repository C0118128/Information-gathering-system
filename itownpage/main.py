from modules.reader import Csv
from modules.webdriver import Chrome


def getTel(target_url, corp_name, corp_location):

    ch = Chrome()
    driver = ch.driver
    driver.get(target_url)
    ch.end()


if __name__ == "__main__":
    target_url = 'https://itp.ne.jp/'

    csv_reader = Csv()
    csv_contens = csv_reader.readCsv('./input.csv', [0,2])
    for content in csv_contens:
        print(content)
        corp_name = content[0]
        corp_location = content[3]
        getTel(target_url, corp_name, corp_location)
        