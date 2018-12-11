# -*- coding: utf-8 -*-
import scrapy


class ToysSpider(scrapy.Spider):
    name = 'toys'
    allowed_domains = ['mytoys.ru']
    start_urls = ['https://www.mytoys.ru/Игрушки/KID/ru-mt.to/?filter=standardAgeRange.A&page=1']

    # //A[@class='next ddl_campaign_link']
    # jbacca_36d9065#z0_m_product_3702462 > div > div > div.prodInfo > span > a
    # z0_m_category_3x_content > div.categoryBottom > div > ul > li.pagination-next > a

    # z0_m_product_3702462 > div > div > div.prodInfo > span > a
    def parse(self, response):
        for toy_url in response.css("div > div.prodInfo > span > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(toy_url), callback=self.parse_toys_page)
        next_page = response.css("li.pagination-next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_toys_page(self, response):
        item = {}
        # product = response.css("div.product_main")
        # item['category'] = response.xpath(
        # "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        # ).extract_first()
        item["title"] = response.css("div#content_xl h1 ::text").extract_first()
        item['art'] = response.css("div#content_xl div.grid_5.pdp__info > p:nth-child(3) ::text").extract_first()
        item['price'] = response.css("# content_xl div.price_section > div > span > meta ::attr(content)").extract()
        item['brand'] = response.css('div#content_xl a > span ::text').extract_first()
        yield item
