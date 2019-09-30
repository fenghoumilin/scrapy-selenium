# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import re

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GdBankSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GdBankDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class SeleniumDownloadMiddleware(object):

    def process_request(self, request, spider):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)
        # driver = webdriver.Chrome()
        driver.get(request.url)
        print("*"*120)
        page = -1
        type = '个贷'
        try:
            page = request.meta['page']
            type = request.meta['type']
            print("current page", page)
        except:
            print('page not exit')
        # print(source)
        time.sleep(5)
        # if page == 0:
        #     gjj = driver.find_element_by_xpath("//div[@class='net_main']//li[@class='se']//a")
        #     if gjj is not None:
        #         print(gjj)
        #         gjj.click()
        if page != -1:
            try:
                print("start")
                xpath = "//div[@id='gedai']//div[@class='page text_center']//a"
                print("type", type)
                if type == '公积金':
                    xpath = "//div[@id='gongjijing']//div[@class='page text_center']//a"
                    driver.find_elements_by_xpath("//div[@class='vcc-index_tab_main loan_tab_clear_float']//a")[1].click()
                    time.sleep(1)
                else:
                    driver.find_elements_by_xpath("//div[@class='vcc-index_tab_main loan_tab_clear_float']//a")[0].click()
                    time.sleep(1)
                button_list = driver.find_elements_by_xpath(xpath)
                print(button_list)
                if button_list is not None:
                    for button in button_list:
                        button_num = 0
                        try:
                            print("button", getFirstNumber(button.get_attribute('href')))
                            button_num = getFirstNumber(button.get_attribute('href'))
                        except:
                            print("next", button.get_attribute('href'))
                            continue
                        print("button_num", button_num)
                        if page == (button_num - 1):
                            button.click()
                            break
            except Exception as e:
                print('error', e)
                pass
        time.sleep(2)
        source = driver.page_source
        response = HtmlResponse(url=driver.current_url, body=source, request=request, encoding='utf-8')
        return response

def getFirstNumber(str):
    numList = re.findall(r"\d+", str)
    return int(numList[0])