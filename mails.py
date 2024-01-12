import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
# i have auto generated this code by using scrapy genspider -t crawl mails x 

class MailsSpider(CrawlSpider):
    name = "mails"
    allowed_domains = ['scrapebay.com']
    start_urls = ["https://scrapebay.com"]

    rules = (Rule(LinkExtractor(), callback="parse_item", follow=True),)

    def parse_item(self, response):
        emails =  re.findall(r'[\w\.]+@[\w\.]+',response.text)
        for email in emails:
            if 'bootstrap' not in email:
                yield{
                    'Email':email
                }