import time

import scrapy
from  scrapy_project.items import ScrapyProjectItem
from ..modules.webdriver import Chrome

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['employment.en-japan.com']
    start_urls = ['http://employment.en-japan.com/']
    
    def start_requests(self):
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
            time.sleep(3)
            current_url = driver.current_url
            yield scrapy.Request(current_url, self.parse)
            time.sleep(2)

        driver.quit()
        return

    def parse(self, response):
        try:
            count = 1
            while True :
                list = response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]')[count].get()
                if list is None:
                    break
                else:
                    a_url = response.urljoin(response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]//*[@class="jobNameArea"]/*[@class="job _aroute_add_param"]/@href')[count].get())
                    yield scrapy.Request(a_url, callback=self.detail_parse)
                    count += 1
        except IndexError as e:
            print(e)
        finally:
            print('finish')
            return
            next_page = response.xpath('//*[@id="jobSearchListNum"]//a[@class="next page next"]/@href').extract_first()
            if next_page is None:
                print('finish')
                return
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def detail_parse(self, response):
        yield ScrapyProjectItem(
            a_url = response.url, 
            name = response.xpath('//*[@id="descCompanyName"]/div[@class="base"]//span[@class="text"]/text()').get(),
            url = response.xpath('//*[@class="previewOption scrollTrigger"]/text()').get()
            )