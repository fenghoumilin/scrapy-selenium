# -*- coding: utf-8 -*-
import scrapy
import time
import re
from gd_bank.items import GdBankItem

class GdSpider(scrapy.Spider):
    name = 'gd'
    allowed_domains = ['ccb.com']
    start_urls = ['http://www.ccb.com/cn/home/map/netPersonalLoan.html?provinceCode=440000']
    # http://www.ccb.com/cn/home/map/netPersonalLoan.html?provinceCode=310000 广东个贷网点
    # http://www.ccb.com/cn/home/map/netPersonalLoan.html?provinceCode=440000 广东公积金贷款网点

    def parse(self, response):

        print("parse")
        aHref = response.xpath("//div[@id='gedai']//div[@class='page text_center']//a/@href").extract_first()
        print("aHref", aHref)
        sum_list = re.findall(r"\d+", aHref)
        total = int(sum_list[-1])
        # 爬取个贷
        for current in range(0, total):
            yield scrapy.Request(response.url, callback=self.parse_content, meta={'page': current, 'type': '个贷'}, dont_filter=True)
        # 爬取公积金
        aHref = response.xpath("//div[@id='gongjijing']//div[@class='page text_center']//a/@href").extract_first()
        print("aHref", aHref)
        sum_list = re.findall(r"\d+", aHref)
        total = int(sum_list[-1])
        for current in range(0, total):
            yield scrapy.Request(response.url, callback=self.parse_content, meta={'page': current, 'type': '公积金'}, dont_filter=True)

    def parse_content(self, response):
        type = '个贷'
        try:
            current_page = response.meta['page']
            type = response.meta['type']
            print("current_page", current_page)
        except:
            print('page not exit')
        url = response.url
        trList = response.xpath("//div[@id='gedai']//table[@class='one_lines_table']//tr[position()>1]")
        if type == '公积金':
            trList = response.xpath("//div[@id='gongjijing']//table[@class='one_lines_table']//tr[position()>1]")
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        table_tr_count = len(trList)
        print("table_tr_count", table_tr_count)
        print("type = ", type)
        for tr in trList[0:table_tr_count]:
            network = tr.xpath(".//td[@class='table_tr_1']/text()").get()
            if network is None:
                print("表头+1")
                continue
            address = tr.xpath(".//td[@class='table_tr_2']/text()").get()
            serviceTime = tr.xpath(".//td[@class='net_workTime']/text()").get()
            phoneNumber = tr.xpath(".//td[@class='table_tr_4']/text()").get()
            province = '广东'
            item = GdBankItem(
                url=url,
                network=network,
                address=address,
                service_time=serviceTime,
                phone_number=phoneNumber,
                province=province,
                type=type,
                created_time=current_time
            )
            print(network)
            # print(item)
            yield item
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