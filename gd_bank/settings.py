# -*- coding: utf-8 -*-

# Scrapy settings for gd_bank project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gd_bank'

SPIDER_MODULES = ['gd_bank.spiders']
NEWSPIDER_MODULE = 'gd_bank.spiders'
LOG_LEVEL="WARNING"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gd_bank (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    'Cookie':"null=891486986.20480.0000; cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82; cityCode=310000; bankName=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%88%86%E8%A1%8C; bankCode=310000000; ticket=; cs_cid=; custName=; userType=; lastLoginTime=; cityCodeFlag=2; ccbcustomid=25cfabb5c9c4903fgP8mJ8wRX3ti7ZOmsY5l1569294593633De97HMGXsOAhk2zwtScc2596d68feb122685ce8967401bd38736; ccbdatard=1; cookieidTagFlag=1; tagInfoId=%26_000094%3D1%26_000050%3D09; center123=1; ccbsessionid=w9809B7ZaZU0a5ca61c5172cfd0-20190926163911; diffTime2=-9915; lastUpdateTime=2019-09-26%2016%3A43%3A44; JSESSIONID=FrJw3LDy5CIILbezaFrRP_ai_xZE00y3eA1GSnqb37Vi-dN_natc!1031700443; INFO=9j9e|XY2IY; tranFAVOR=JdCiogbCsTo%2Clm6QWbM%2Cwm7Qhbo%2CQmkQob8%2C7m9QZbu%2CAm%2CQqbY%2CefjefeKQJAr5ho",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'gd_bank.middlewares.SeleniumDownloadMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'gd_bank.middlewares.SeleniumDownloadMiddleware': 543,
}

LOG_FORMAT = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'gd_bank.pipelines.GdBankPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# 连接数据MySQL
# 数据库地址
MYSQL_HOST = 'localhost'
# 数据库用户名:
MYSQL_USER = 'root'
# 数据库密码
MYSQL_PASSWORD = 'root'
# 数据库端口
MYSQL_PORT = 3306
# 数据库名称
MYSQL_DBNAME = 'gdjs'
# 数据库编码
MYSQL_CHARSET = 'utf8'