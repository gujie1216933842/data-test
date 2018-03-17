#Author:Bob
import scrapy
from jdmobile.items import JdmobileItem

class jdmobile(scrapy.Spider):
    name = "jdmobile"
    allowed_domains = ["jd.com"]
    start_urls = (
        "https://item.jd.com/11334636448.html"
    )

    def parse(self,response):
        item = JdmobileItem()
        print(2)
        #提取手机,xpath表达式
        item['title'] = response.xpath("//meta[@name='keywords']/@content").extract()
        print(1)
        print(item['title'])