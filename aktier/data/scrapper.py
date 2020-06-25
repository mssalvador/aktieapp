import scrapy

class AktieSpider(scrapy.Spider):
    name = "aktie_spider"
    start_urls = ["https://npinvestor.dk/kursinfo/vis-aktie/172.1.BAVA:2"]