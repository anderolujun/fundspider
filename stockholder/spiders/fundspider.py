import scrapy
from lxml.html import open_in_browser

from stockholder.items import StockholderItem
from scrapy.http import Request
from scrapy.selector import Selector
import json
from scrapy_splash import SplashRequest


class Fundspider(scrapy.Spider):
    name = 'fundspider'
    allowed_domains = ['eastmoney.com']
    # start_urls = ['http://fund.eastmoney.com/js/fundcode_search.js']
    start_urls = ['http://fundf10.eastmoney.com/cwzb_003064.html']

    def __init__(self, fundcode='', *args, **kwargs):
        super(Fundspider, self).__init__(*args, **kwargs)
        self.fundcode = fundcode
        self.start_urls = [f'http://fundf10.eastmoney.com/cwzb_{self.fundcode}.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'timeout': 24, 'images': 0})

    # 解析财务指标（按报告期)。
    def parse(self, response):
        # if rs.get('message') == 'success':
        # 期末数据 //*[@id="cwtable"]/div/table[2]/thead/tr   //*[@id="cwtable"]/div/table[2]/tbody tr td
        # 累计数据 //*[@id="cwtable"]/div/table[3]/thead/tr //*[@id="cwtable"]/div/table[3]/tbody/tr
        # 期间数据和指标 head //*[@id="cwtable"]/div/table[1]/thead/tr //*[@id="cwtable"]/div/table[1]/tbody/tr
        item_list = []
        # 存放财务周期
        fsrq = []
        # 解析财报周期 //*[@id="cwtable"]/div/table/thead/tr/th[2]
        head = response.xpath("//*[@id='cwtable']/div/table[1]/thead/tr/th/text()").extract()
        fsrq = head[1:]

        # 期间数据
        row1 = response.xpath("//*[@id='cwtable']/div/table[1]/tbody/tr/td/text()").extract()
        # 本期已实现收益
        comprofit = row1[1:5]
        # 本期利润
        row1 = row1[5:]
        netprofit = row1[1:5]
        # 加权平均基金份额本期利润
        row1 = row1[5:]
        unitprofit = row1[1:5]
        # 本期加权平均净值利润率
        row1 = row1[5:]
        ngrowth = row1[1:5]
        # 本期基金份额净值增长率
        row1 = row1[5:]
        fngrowth = row1[1:5]

        # 期末数据表头的报表日期不解析了
        # 期末数据解析
        row2 = response.xpath("//*[@id='cwtable']/div/table[2]/tbody/tr/td[@class='tor']/text()").extract()
        # 期末可供分配利润
        disprofit = row2[0:4]
        # 期末可供分配基金份额利润
        difunitprofit = row2[4:8]
        # 期末基金资产净值
        endnav = row2[8:12]
        # 期末基金份额净值
        endunitnav = row2[12:16]

        # 累计数据列头不解析
        # 累计数据
        row3 = response.xpath("//*[@id='cwtable']/div/table[3]/tbody/tr/td[@class='tor']/text()").extract()

        for i in range(len(fsrq)):
            item = StockholderItem()
            item['FUNDCODE'] = self.fundcode
            item['FSRQ'] = fsrq[i]
            item['COMPROFIT'] = comprofit[i]
            item['NETPROFIT'] = netprofit[i]
            item['UNITPROFIT'] = unitprofit[i]
            item['NGROWTH'] = ngrowth[i]
            item['FNGROWTH'] = fngrowth[i]
            item['DISPROFIT'] = disprofit[i]
            item['DIFUNTIPROFIT'] = difunitprofit[i]
            item['ENDNAV'] = endnav[i]
            item['ENDUNITNAV'] = endunitnav[i]
            item['FCNGROWTH'] = row3[i]
            item['FIELDTYPE'] = 'dl'
            item_list.append(item)
            yield item

    # def parseDetail(self):
    #     pass
