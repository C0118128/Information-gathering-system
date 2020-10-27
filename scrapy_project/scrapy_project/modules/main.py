import pprint
import os, time, math, threading, re

from modules.webdriver import Chrome

def main():
    try:
        # 初期設定
        en_url = 'https://employment.en-japan.com/'
        ch = Chrome()
        driver = ch.driver

        # 2. 職種リスト
        occupation_list = [
            {'id': '1', 'name': 'sales'},
            {'id': '2', 'name': 'planning'},
            {'id': '3', 'name': 'service'},
            {'id': '4', 'name': 'professional'},
            {'id': '5', 'name': 'profession'},
            {'id': '6', 'name': 'creative'},
            {'id': '7', 'name': 'engineers'},
            {'id': '8', 'name': 'electrical'},
            {'id': '9', 'name': 'building'},
            {'id': '10', 'name': 'medical'},
            {'id': '11', 'name': 'facility'},
            # {'id': '12', 'name': 'public'},　# 未実装
        ]

        for occupation in occupation_list:
            driver.get(en_url)
            id = occupation.get('id')
            name = occupation.get('name')
            # 業種選択
            driver.find_element_by_xpath(f'//*[@class="searchUnit searchUnitJob"]/ul[@class="categoryList"]/li[{id}]/a[@class="link"]').click() # 業種
            time.sleep(2)
            driver.find_element_by_xpath(f'//*[@id="jobIndexSearchList"]/*[@class="content"]/*[@class="btn"]/button[@class="searchBtn"]').click() # 全て選択
            time.sleep(2)
            current_url = driver.current_url
            print(current_url)
            time.sleep(2)
            
        driver.quit()

        
        return

    except Exception as e:
        print(e)
        return

if __name__ == '__main__':
    main()