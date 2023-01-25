import scrapy
from ..items import ScrapyTuts2Item
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class AmazonScrapy(scrapy.Spider):
    name = 'amazon'
    page = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    # def login(self, response):
    #     token = response.xpath('//input[@name="csrf_token"]').extract()
    #     FormRequest.from_response(response, formdata={
    #         'csrf_token' : token,
    #         'username' : 'bibek',
    #         'password' : 'bibek123'
    #     }, callback=self.parse)

    def parse(self, response):
        open_in_browser(response)
        data = ScrapyTuts2Item()

        quotes = response.css('.quote')
        for quote in quotes:
            data['title'] = quote.css('span.text::text').extract()
            data['author'] = quote.css('.author::text').extract()
            data['tag'] = quote.css('.tag::text').extract()
            yield data

        # next_page = response.css('li.next a::attr("href")').get()

        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)

        next_page = 'http://quotes.toscrape.com/page/' + str(AmazonScrapy.page) +'/'

        if AmazonScrapy.page < 11:
            AmazonScrapy.page += 1
            yield response.follow(next_page, callback= self.parse)