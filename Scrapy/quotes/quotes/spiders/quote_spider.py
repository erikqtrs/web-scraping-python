import scrapy
from ..items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):

        items = QuotesItem()

        all_dib_quotes = response.css('div.quote')

        for quotes in all_dib_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('small.author::text').extract()
            tags = quotes.css('a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            
            yield items
            
            #yield {
            #    'title': title,
            #    'author': author,
            #    'tags': tags
            #}

            next_page = 'https://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) + '/'

            if QuoteSpider.page_number < 11:
                QuoteSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse)