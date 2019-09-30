# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

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
        # options = Options()
        # options.add_argument('--headless')
        # driver = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Chrome()
        driver.get(request.url)
        print("*"*120)
        page = 0
        try:
            page = request.meta['page']
            print("current page", page)
        except:
            print('page not exit')
        # print(source)
        if page != 0:
            try:
                time.sleep(5)
                print("start")
                button_list = driver.find_elements_by_xpath("//div[@class='page text_center']//a")
                print(button_list)
                if button_list is not None:
                    for button in button_list:
                        button_num = 0
                        try:
                            button_num = int(button.text)
                        except:
                            print("next")
                            continue
                        print("button_num", button_num)
                        if page == (button_num - 1):
                            button.click()
                            break
            except Exception as e:
                print('error', e)
                pass
        time.sleep(5)
        source = driver.page_source
        response = HtmlResponse(url=driver.current_url, body=source, request=request, encoding='utf-8')
        return response