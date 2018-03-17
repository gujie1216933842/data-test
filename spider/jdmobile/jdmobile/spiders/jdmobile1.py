#Author:Bob
import scrapy


class jdmobile:
    name = "jdmobile"
    allowed_domains = ["jd.com"]
    start_urls = (
        "https://item.jd.com/11334636448.html"
    )

    def parse(self,response):
        item = JdmobileItem()
        #提取手机,xpath表达式
        item['title'] = response.xpath("//meta[@name='keywords']/@content").extract()
        print(item['title'])