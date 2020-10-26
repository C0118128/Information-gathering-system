import scrapy
from  scrapy_project.items import ScrapyProjectItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['employment.en-japan.com/search/search_list/?occupation_back=400000&caroute=0701&occupation=401000_401500_402000_402500_403000_403500_404000_404500_405000_405500_409000']
    start_urls = ['http://employment.en-japan.com/search/search_list/?occupation_back=400000&caroute=0701&occupation=401000_401500_402000_402500_403000_403500_404000_404500_405000_405500_409000/']

    def parse(self, response):
        count = 1
        while True :
            data = response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]').extract()[count]
            if data is None:
                break
            else:
                yield ScrapyProjectItem(
                        name = response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]//*[@class="companyName"]/*[@class="company"]/text()').extract()[count],
                        url = response.urljoin(response.xpath('//*[@class="jobSearchListLeftArea"]/*[@class="list"]//*[@class="jobNameArea"]/*[@class="job _aroute_add_param"]/@href').extract()[count])
                    )
                count += 1
