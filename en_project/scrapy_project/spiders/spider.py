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

        # 職種リスト
        occupation_list = [
            # {'id': '1', 'name': 'sales'},
            # {'id': '2', 'name': 'planning'},
            # {'id': '3', 'name': 'service'},
            # {'id': '4', 'name': 'professional'},
            # {'id': '5', 'name': 'profession'},
            # {'id': '6', 'name': 'creative'},
            # {'id': '7', 'name': 'engineers'},
            # {'id': '8', 'name': 'electrical'},
            # {'id': '9', 'name': 'building'},
            # {'id': '10', 'name': 'medical'},
            {'id': '11', 'name': 'facility'},
            # {'id': '12', 'name': 'public'},　# 未実装
        ]

        # 検索一覧URL取得・スクレイピング実行
        for occupation in occupation_list:
            driver.get(en_url)
            id = occupation.get('id')
            name = occupation.get('name')
            driver.find_element_by_xpath(f'//*[@class="searchUnit searchUnitJob"]/ul[@class="categoryList"]/li[{id}]/a[@class="link"]').click() # 業種
            time.sleep(2)
            driver.find_element_by_xpath(f'//*[@id="jobIndexSearchList"]/*[@class="content"]/*[@class="btn"]/button[@class="searchBtn"]').click() # 全て選択
            time.sleep(3)
            current_url = driver.current_url
            yield scrapy.Request(current_url, self.parse)
            time.sleep(2)

        driver.quit()
        return

    # 検索一覧の企業情報を各ページ読み取る
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
            # 検索一覧ページの企業情報を全て読み取った
            print(e)
        finally:
            #　次のページへ
            next_page = response.xpath('//*[@id="jobSearchListNum"]//a[@class="next page next"]/@href').extract_first()
            if next_page is None:
                # 次のページがなければ終了
                print('finish')
                return
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # 詳細から各情報を読み取る
    def detail_parse(self, response):
        resolt = None 
        try:
            text = response.xpath('//*[@class="addressUnit"]/..').get()
            s = text.split('\t\t\t')
            resolt = s[1].replace('<br>', '/') 
        except Exception as e:
            # 検索一覧ページの企業情報を全て読み取った
            print(e)
            print(resolt) 
            resolt = '読み取り不可避エラー'
        finally:
            yield ScrapyProjectItem(
                企業情報_1_名前 = response.xpath('//*[@id="descCompanyName"]/div[@class="base"]//span[@class="text"]/text()').get(),
                企業情報_2_サイト = response.xpath('//*[@class="previewOption scrollTrigger"]/text()').get(),
                企業情報_3_求人サイト企業情報 = response.url,
                連絡先_1_住所 = resolt,
                # xpath結構使えるかも　response.xpath('//*[@class="descArticleArea descSubArticle"][2]/*[@class="descArticleUnit dataCompanyInfoSummary"]').get(),
                連絡先_2 = response.xpath('//*[@class="addressUnit"][1]/span[@class="text"]/text()').get(),
                連絡先_3 = response.xpath('//*[@class="addressUnit"][2]/span[@class="text"]/text()').get(),
                連絡先_4 = response.xpath('//*[@class="addressUnit"][3]/span[@class="text"]/text()').get(),
                )