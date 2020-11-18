import time

from modules.reader import Csv
from modules.webdriver import Chrome


def getTel(target_url, corp_name, corp_location):

    ch = Chrome()
    with ch.driver as driver:
        driver.get(target_url)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="keyword-suggest"]/input').send_keys(corp_name)
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div/div[2]/form/button').click
        current_url = driver.current_url
        print(current_url)



if __name__ == "__main__":
    target_url = 'https://itp.ne.jp/'

    csv_reader = Csv()
    csv_contens = csv_reader.readCsv('./input.csv', [0,2])
    for content in csv_contens:
        print(content)
        corp_name = content[0]
        corp_location = content[1]
        getTel(target_url, corp_name, corp_location)
        