import time

from selenium.webdriver.support.select import Select
import scrapy
from  scrapy_project.items import ScrapyProjectItem
from ..modules.webdriver import Chrome

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.green-japan.com']
    start_urls = ['http://www.green-japan.com/']
    
    def start_requests(self):
        # 初期設定
        en_url = 'http://www.green-japan.com/'
        ch = Chrome()
        driver = ch.driver

        # 職種リスト
        occupation_list = [
            # {'id': '190', 'name': 'engineers'},
            # {'id': '160', 'name': 'web'},
            # {'id': '170', 'name': 'game'},
            # {'id': '110', 'name': 'marketing'},
            # {'id': '100', 'name': 'sales'},
            # {'id': '230', 'name': 'planning'},
            # {'id': '120', 'name': 'backoffice'},
            # {'id': '130', 'name': 'office'},
            # {'id': '140', 'name': 'service'},
            # {'id': '150', 'name': 'profession'},
            # {'id': '200', 'name': 'electrical'},
            {'id': '220', 'name': 'building'},
        ]

        # 検索一覧URL取得・スクレイピング実行
        for occupation in occupation_list:
            driver.get(en_url)
            id = occupation.get('id')
            name = occupation.get('name')
            select_element = driver.find_element_by_xpath(f'//*[@id="slct_01"]')
            select_object = Select(select_element)
            select_object.select_by_value(id)
            time.sleep(1)
            driver.find_element_by_xpath(f'//*[@id="slct_05"]').click() # 全て選択
            time.sleep(2)
            current_url = driver.current_url
            yield scrapy.Request(current_url, self.parse)
            time.sleep(2)

        driver.quit()
        return

    # 検索一覧の企業情報を各ページ読み取る
    def parse(self, response):
        try:
            count = 0
            while True :
                list = response.xpath('//*[@class="card-info__wrapper js-card-info__wrapper"]')[count].get()
                if list is None:
                    print('break')
                    break
                else:
                    yield ScrapyProjectItem(
                        s1_name = response.xpath('//*[@class="card-info__detail-area__box__title"]/text()')[count].get(),
                        s2_a_url = response.urljoin(response.xpath('//*[@class="js-search-result-box card-info "]/@href')[count].get()),
                        s3_location =  response.xpath('//*[@class="icon-site"]/../text()')[count].get(),
                        )
                    count += 1
        except IndexError as e:
            # 検索一覧ページの企業情報を全て読み取った
            print(e)
        finally:
            #　次のページへ
            next_page = response.xpath('//*[@id="new_user_search"]//*[@class="next_page"]/@href').get()
            if next_page is None:
                # 次のページがなければ終了
                print('finish')
                return
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)