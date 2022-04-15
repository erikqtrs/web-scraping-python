import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/-/es/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=1&language=es&qid=1647567463&rnid=1250225011&ref=sr_pg_2'
    ]

    def parse(self, response):

        items = AmazonItem()

        product_name = response.css('.a-size-medium a-color-base a-text-normal::text').extract()
        product_author = response.css('.a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()
        
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.com/-/es/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+str(AmazonSpiderSpider.page_number)+'&language=es&qid=1647567463&rnid=1250225011&ref=sr_pg_2'

        if AmazonSpiderSpider.page_number < 100:
            yield response.follow(next_page, callback=self.parse)