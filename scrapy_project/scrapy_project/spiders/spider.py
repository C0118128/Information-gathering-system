import scrapy
from  scrapy_project.items import ScrapyProjectItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['employment.en-japan.com']
    start_urls = ['http://employment.en-japan.com/search/search_list/?occupation_back=400000&caroute=0701&occupation=401000_401500_402000_402500_403000_403500_404000_404500_405000_405500_409000/']

    def parse(self, response):
        try:
            count = 1
            while True :
                list = response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]')[count].get()
                if list is None:
                    break
                else:
                    yield ScrapyProjectItem(
                            a_url = response.urljoin(response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]//*[@class="jobNameArea"]/*[@class="job _aroute_add_param"]/@href')[count].get()),
                            name = response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]//*[@class="companyName"]/*[@class="company"]/text()')[count].get(),
                            url = None
                        )
                    count += 1
        except IndexError as e:
            print(e)
        finally:
            next_page = response.xpath('//*[@id="jobSearchListNum"]//a[@class="next page next"]/@href').extract_first()
            if next_page is None:
                print('finish')
                return
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

