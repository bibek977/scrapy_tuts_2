import scrapy
from ..items import ScrapyTuts2Item

class AmazonScrapy(scrapy.Spider):

    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1674651207&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response):

        item = ScrapyTuts2Item()

        book_title = response.css('.a-size-medium::text').extract()
        book_price = response.css('.a-price-fraction , .s-price-instructions-style .a-price-fraction , .s-price-instructions-style .a-price-whole , .a-spacing-mini:nth-child(1) .a-price-whole').css('::text').extract()
        book_image = response.css('.s-image').css('::attr(src)').extract()
        book_voter = response.css('.a-color-secondary .a-size-base.s-link-style , .a-color-secondary .a-row .a-size-base:nth-child(2)').css("::text").extract()

        item['title'] = book_title
        item['price'] = book_price
        item['image'] = book_image
        item['voter'] = book_voter

        yield item