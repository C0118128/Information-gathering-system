import time
import multiprocessing
from multiprocessing import Pool

from modules.fileIO import Csv
from modules.webdriver import Chrome


def get_list_url(target_url, corp_name, corp_location):
    ch = Chrome()
    with ch.driver as driver:
        driver.get(target_url)
        time.sleep(2)
        driver.find_element_by_id('keyword-suggest').find_element_by_class_name('a-text-input').send_keys(corp_name)
        driver.find_element_by_id('area-suggest').find_element_by_class_name('a-text-input').send_keys(corp_location)
        driver.find_element_by_class_name('m-keyword-form__button').click()
        time.sleep(2)
        current_url = driver.current_url
        return current_url

def passContent(content):
    print('start thread')
    corp_name = content[0]
    green_url = content[1]
    corp_location = content[2]
    try:
        list_url = get_list_url(target_url, corp_name, corp_location)
        content = [corp_name, corp_location, green_url,list_url]
        fileIO.addCsv(output_path, content)
    except Exception as e:
        print(e)
        pass



if __name__ == "__main__":
    list = [
        "building",
        "backoffice",
        # "electrical",
        # "engineers",
        # "game",
        # "marketing",
        # "office",
        # "planning",
        # "profession",
        # "sales",
        # "service",
        # "web",
    ]

    for file_name in list:
        # file_name = 'building'
        target_url = 'https://itp.ne.jp/'
        input_path = './in/'+ file_name +'.csv'
        output_path = './out/' + file_name + '.csv'
        target_row = [0,1,2]
        # process_num = multiprocessing.cpu_count()
        process_num = 6

        fileIO = Csv()
        csv_contents = fileIO.readCsv(input_path, target_row)
        process = Pool(process_num)
        process.map(passContent, csv_contents)
        process.close()
        process.join()
