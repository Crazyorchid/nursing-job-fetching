from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class sahealthSpider(CrawlSpider):
    name = 'sahealth'
    allowed_domains=["careers.pageuppeople.com"]
    start_urls = ["https://careers.pageuppeople.com/532/caw/en/listing"]
    
    rules = (Rule(LinkExtractor(allow="category=&category=nursing")),)
    
    def parse_item(self, response):
        yield{
            "title": response.css(".job-link::text").getall(),
            "location":response.css(".location::text").getall(),
            
        }
    
    
    