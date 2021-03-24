import scrapy
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from stockholder.utils.utils import Logger
import logging
from stockholder.utils.stack import FundStack
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# 总的入口爬虫，调用其它爬虫。爬取财务报表相关数据
class CwzbSpider(scrapy.Spider):
    name = 'cwzb'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/js/fundcode_search.js']

    def __init__(self, fundcode='', *args, **kwargs):
        super(CwzbSpider, self).__init__(*args, **kwargs)
        self.fundcode = fundcode
        # 财务指标
        self.cwzburl = "http://fundf10.eastmoney.com/cwzb_" + self.fundcode + ".html"
        # 利润表
        self.profiturl = "http://fundf10.eastmoney.com/lrfpb_" + self.fundcode + ".html"
        # 资产负债表
        self.asseturl = "http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=zcfzb&code=" + self.fundcode + "&showtype=1"
        self.process = CrawlerProcess(get_project_settings())

    # 实例化浏览器对象
    # def __init__(self):
    #     # 调用超类的构造函数
    #     super().__init__()
    #     self.timeout = 20
    #     options = webdriver.ChromeOptions()
    #     # 设置无图加载，提高速度
    #     prefs = {"profile.managed_default_content_settings.images": 2}
    #     options.add_experimental_option("prefs", prefs)
    #     # 设置无头浏览器
    #     options.add_argument('--headless')
    #     self.browser = webdriver.Chrome(chrome_options=options)
    #     self.wait = WebDriverWait(self.browser,self.timeout)

    # 爬虫结束后关闭浏览器
    # def close(self,spider):
    #     self.browser.quit()

    def start_requests(self):
        # url = "http://fundf10.eastmoney.com/cwzb_003064.html"
        # /html/body/pre
        print(self.cwzburl)
        response = scrapy.Request(self.start_urls[0], callback=self.parse)
        yield response

    # 解析response.命令行传递fundcode=‘ALL’爬取所有基金数据；输入特定编号则爬取特定基金数据
    def parse(self, response):
        if self.fundcode != 'ALL':
            self.process.crawl('fundspider', domain='eastmoney.com', fundcode=self.fundcode)
            self.process.crawl('fundprofit', domain='eastmoney.com', fundcode=self.fundcode)
            self.process.crawl('assetliabequity', domain='eastmoney.com', fundcode=self.fundcode)
            self.process.start()  # the script will block here until the crawling is finished
        else:
            # 所有基金信息
            div_list = response.xpath("/html/body/p/text()").extract()
            # 截取首尾字符串
            fund_arr = div_list[0][div_list[0].find("["):div_list[0].rfind(";")]

            stack = FundStack()
            i = 0
            arr_length = len(fund_arr)
            fundarr = []  # 备用数组
            # 遍历所有基金
            while i <= arr_length:
                if fund_arr[i] == "]":
                    fundstr = ""
                    # 遇到]就开始把栈里的元素弹出，直到遇到[就停止弹出。
                    while stack.peek() != "[":
                        ele = stack.peek()
                        fundstr = fundstr + ele
                        stack.pop()
                    # 弹出[
                    stack.pop()
                    # 字符串反转
                    fundstr = fundstr[::-1]
                    arr = fundstr.split(",")
                    # 截取arr[0]基金编号
                    fundcode = arr[0][arr[0].find("\"") + 1:arr[0].rfind("\"")]
                    yield self.process.crawl('fundspider', domain='eastmoney.com', fundcode=fundcode)
                    yield self.process.crawl('fundprofit', domain='eastmoney.com', fundcode=fundcode)
                    yield self.process.crawl('assetliabequity', domain='eastmoney.com', fundcode=fundcode)
                    # self.process.start()  # the script will block here until the crawling is finished
                else:
                    stack.push(fund_arr[i])
                i = i + 1
            self.process.start()
            yield response
