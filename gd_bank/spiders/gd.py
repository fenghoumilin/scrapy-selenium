# -*- coding: utf-8 -*-
import scrapy
import time
import re
from gd_bank.items import GdBankItem

class GdSpider(scrapy.Spider):
    name = 'gd'
    allowed_domains = ['ccb.com']
    start_urls = ['http://www.ccb.com/cn/home/map/netPersonalLoan.html?provinceCode=440000']


    def parse(self, response):
        print("parse")
        aHref = response.xpath("//div[@class='page text_center']//a/@href").extract_first()
        print(aHref)
        sum_list = re.findall(r"\d+", aHref)
        total = int(sum_list[-1])
        for current in range(1, total):
            print(current)
            yield scrapy.Request(response.url, callback=self.parse_content, meta={'page': current}, dont_filter=True)
        """模拟浏览器实现翻页，并解析每一个话题列表页的url_list
               """

    def parse_content(self, response):

        url = response.url
        trList = response.xpath("//table[@class='one_lines_table']//tr[position()>1]")
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        table_tr_count = len(trList)
        print("table_tr_count", table_tr_count)
        end_line = table_tr_count
        current_page = 2
        try:
            current_page = response.meta['page']
            print("current_page", current_page)
        except:
            print('page not exit')
        if current_page > 1:
            end_line -= 10
        for tr in trList[0:end_line]:
            network = tr.xpath(".//td[@class='table_tr_1']/text()").get()
            if network is None:
                print("表头+1")
                continue
            address = tr.xpath(".//td[@class='table_tr_2']/text()").get()
            serviceTime = tr.xpath(".//td[@class='net_workTime']/text()").get()
            phoneNumber = tr.xpath(".//td[@class='table_tr_4']/text()").get()
            item = GdBankItem(
                url=url,
                network=network,
                address=address,
                service_time=serviceTime,
                phone_number=phoneNumber,
                created_time=current_time
            )
            print(network)
            # print(item)
            # yield item
        # nameList = response.xpath("//div[@class='cbga']//a/text()").extract()
        # print(nameList)
        # nextUrl = "http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&TXCODE=NZX004&Province_Code=440000&City_Code=&Type_Ploan=1&Type_Afund=0&Outlet_Name=&StartNum=1&EndNum=10"
        #
        # #print(response.text)
        # cookie = response.headers.getlist('Set-Cookie')
        # print('Cookie', cookie)
        # jess_cookie = self.parse_cookies(cookie[0])
        # print(jess_cookie)
        # time.sleep(2)
        # yield scrapy.Request(url=nextUrl, callback=self.parse_content, headers=self.headers, meta={'cookiejar': response.meta['cookiejar']})
        # with open("./file.html", "w", encoding='utf-8') as f:
        #     f.write(response.text)
        # pass