import scrapy
from lxml.html import open_in_browser

from stockholder.items import AssetItem
from stockholder.items import LiabeilitiesItem
from stockholder.items import OwnerEquityItem
from scrapy.http import Request
from scrapy.selector import Selector
import json


class Assetliabequity(scrapy.Spider):
    name = 'assetliabequity'
    allowed_domains = ['eastmoney.com']
    # start_urls = ['http://fund.eastmoney.com/js/fundcode_search.js']
    # 请求资产负债表返回数据url showtype =1 按半年返回 showtype=2 按年返回
    start_urls = ['http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=zcfzb&code=003064&showtype=1']

    def __init__(self, fundcode='', *args, **kwargs):
        super(Assetliabequity, self).__init__(*args, **kwargs)
        self.fundcode = fundcode
        self.start_urls = [f'http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=zcfzb&code={self.fundcode}&showtype=1']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, self.parse)

    # 解析资产负债表
    def parse(self, response):
        # print("res-encoding="+response.encoding)
        # print(response.text)
        fundcode = self.start_urls[0].split('code=')[1]
        fundcode = fundcode[0:6]
        # print("fundcode="+fundcode)
        # print(response.xpath("/html/body/div/table[1]/thead/tr/th/text()").extract())
        itemAseets = []  # 资产数组集合
        try:
            th1 = response.xpath("/html/body/div/table[1]/thead/tr/th/text()").extract()
            fsrq = th1[1:]  # '日期
            print(fsrq)
            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[2]/td/text()").extract()
            bankdeposits = rowall[1:]  # '银行存款

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[3]/td/text()").extract()
            settallowance = rowall[1:]  # '结算备付金

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[4]/td/text()").extract()
            deposit = rowall[1:]  # '存出保证金

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[5]/td/text()").extract()
            asserttrading = rowall[1:]  # '交易性金融资产

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[6]/td/text()").extract()
            stockinvestment = rowall[1:]  # '其中：股票投资

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[7]/td/text()").extract()
            fundinvestment = rowall[1:]  # '其中：基金投资

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[8]/td/text()").extract()
            bondinvestment = rowall[1:]  # '其中：债券投资

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[9]/td/text()").extract()
            investsecurities = rowall[1:]  # '其中：资产支持证券投资'

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[10]/td/text()").extract()
            derivativeassert = rowall[1:]  # '衍生金融资产

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[11]/td/text()").extract()
            buybackassets = rowall[1:]  # '买入返售金融资产

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[12]/td/text()").extract()
            securclearreceivable = rowall[1:]  # '应收证券清算款

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[13]/td/text()").extract()
            interestreceivable = rowall[1:]  # '应收利息

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[14]/td/text()").extract()
            dividendreceivable = rowall[1:]  # '应收股利

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[15]/td/text()").extract()
            requisitionreceivables = rowall[1:]  # '应收申购款

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[16]/td/text()").extract()
            deferredtaxassets = rowall[1:]  # '递延所得税资产

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[17]/td/text()").extract()
            otherassets = rowall[1:]  # '其他资产

            rowall = response.xpath("/html/body/div/table[1]/tbody/tr[18]/td/text()").extract()
            totalassets = rowall[1:]  # '资产总计

            for i in range(0, len(fsrq)):
                item = AssetItem()
                item['FUNDCODE'] = fundcode
                item['FSRQ'] = fsrq[i]  # '日期	              '
                item['BANKDEPOSITS'] = bankdeposits[i]  # '银行存款	          '
                item['SETTALLOWANCE'] = settallowance[i]  # '结算备付金	          '
                item['DEPOSIT'] = deposit[i]  # '存出保证金	          '
                item['ASSERTTRADING'] = asserttrading[i]  # '交易性金融资产	      '
                item['STOCKINVESTMENT'] = stockinvestment[i]  # '其中：股票投资	      '
                item['FUNDINVESTMENT'] = fundinvestment[i]  # '其中：基金投资	      '
                item['BONDINVESTMENT'] = bondinvestment[i]  # '其中：债券投资	      '
                item['INVESTSECURITIES'] = investsecurities[i]  # '其中：资产支持证券投资
                item['DERIVATIVEASSERT'] = derivativeassert[i]  # '衍生金融资产
                item['BUYBACKASSETS'] = buybackassets[i]  # '买入返售金融资产
                item['SECURCLEARRECEIVABLE'] = securclearreceivable[i]  # '应收证券清算款
                item['INTERESTRECEIVABLE'] = interestreceivable[i]  # '应收利息
                item['DIVIDENDRECEIVABLE'] = dividendreceivable[i]  # '应收股利
                item['REQUISITIONRECEIVABLES'] = requisitionreceivables[i]  # '应收申购款
                item['DEFERREDTAXASSETS'] = deferredtaxassets[i]  # '递延所得税资产
                item['OTHERASSETS'] = otherassets[i]  # '其他资产
                item['TOTALASSETS'] = totalassets[i]  # '资产总计
                print(item)
                yield item
                # itemAseets.append(item)
            th1 = response.xpath("/html/body/div/table[2]/thead/tr/th/text()").extract()
            fsrq = th1[1:]  # '日期',

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[2]/td/text()").extract()
            shorttermborrowings = rowall[1:]  # '短期借款

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[3]/td/text()").extract()
            tradingliabilit = rowall[1:]  # '交易性金融负债

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[4]/td/text()").extract()
            derivativeliabilit = rowall[1:]  # '衍生金融负债

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[5]/td/text()").extract()
            selfrepuassert = rowall[1:]  # '卖出回购金融资产款

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[6]/td/text()").extract()
            seculiqupayables = rowall[1:]  # '应付证券清算款

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[7]/td/text()").extract()
            redemptionspayable = rowall[1:]  # '应付赎回款

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[8]/td/text()").extract()
            comppayadmin = rowall[1:]  # '应付管理人报酬

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[9]/td/text()").extract()
            escrfeepayable = rowall[1:]  # '应付托管费

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[10]/td/text()").extract()
            saleservfeepay = rowall[1:]  # '应付销售服务费

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[11]/td/text()").extract()
            taxespayable = rowall[1:]  # '应付税费

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[12]/td/text()").extract()
            interestpayable = rowall[1:]  # '应付利息

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[13]/td/text()").extract()
            profitreceivable = rowall[1:]  # '应收利润

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[14]/td/text()").extract()
            defincomtaxliab = rowall[1:]  # '递延所得税负债

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[15]/td/text()").extract()
            otherliabilities = rowall[1:]  # '其他负债

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[16]/td/text()").extract()
            totalliabilities = rowall[1:]  # '负债合计

            for i in range(0, len(fsrq)):
                item = LiabeilitiesItem()
                item['FUNDCODE'] = fundcode
                item['FSRQ'] = fsrq[i]  # '日期',
                item['SHORTTERMBORROWINGS'] = shorttermborrowings[i]  # '短期借款	          '
                item['TRADINGLIABILIT'] = tradingliabilit[i]  # '交易性金融负债	      '
                item['DERIVATIVELIABILIT'] = derivativeliabilit[i]  # '衍生金融负债	      '
                item['SELFREPUASSERT'] = selfrepuassert[i]  # '卖出回购金融资产款	  '
                item['SECULIQUPAYABLES'] = seculiqupayables[i]  # '应付证券清算款	      '
                item['REDEMPTIONSPAYABLE'] = redemptionspayable[i]  # '应付赎回款	          '
                item['COMPPAYADMIN'] = comppayadmin[i]  # '应付管理人报酬	      '
                item['ESCRFEEPAYABLE'] = escrfeepayable[i]  # '应付托管费	          '
                item['SALESERVFEEPAY'] = saleservfeepay[i]  # '应付销售服务费	      '
                item['TAXESPAYABLE'] = taxespayable[i]  # '应付税费	          '
                item['INTERESTPAYABLE'] = interestpayable[i]  # '应付利息	          '
                item['PROFITRECEIVABLE'] = profitreceivable[i]  # '应收利润	          '
                item['DEFINCOMTAXLIAB'] = defincomtaxliab[i]  # '递延所得税负债	      '
                item['OTHERLIABILITIES'] = otherliabilities[i]  # '其他负债	          '
                item['TOTALLIABILITIES'] = totalliabilities[i]  # '负债合计	          '
                yield item
                # itemAseets.append(item)

            th1 = response.xpath("/html/body/div/table[2]/thead/tr/th/text()").extract()
            fsrq = th1[1:]

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[18]/td/text()").extract()
            paidinfunds = rowall[1:]

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[19]/td/text()").extract()
            totalownequity = rowall[1:]

            rowall = response.xpath("/html/body/div/table[2]/tbody/tr[20]/td/text()").extract()
            totalliabownequity = rowall[1:]

            for i in range(0, len(fsrq)):
                item = OwnerEquityItem()
                item['FUNDCODE'] = fundcode
                item['FSRQ'] = fsrq[i]  # '日期',
                item['PAIDINFUNDS'] = paidinfunds[i]  # '实收基金	'           ,
                item['TOTALOWNEQUITY'] = totalownequity[i]  # '所有者权益合计	'       ,
                item['TOTALLIABOWNEQUITY'] = totalliabownequity[i]  # '负债和所有者权益合计'	,  	,         '
                yield item
                # itemAseets.append(item)

        except Exception as error:
            print(error)


class ParseAssetLiabeQuity():
    # 解析资产
    def parseAsset(self, response, fundcode):

        th1 = response.xpath("/html/body/div/table[1]/thead/tr/th/text()").extract()
        fsrq = th1[1:]  # '日期
        print("fsrq=" + fsrq)
        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[2]/td/text()").extract()
        bankdeposits = rowall[1:]  # '银行存款

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[3]/td/text()").extract()
        settallowance = rowall[1:]  # '结算备付金

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[4]/td/text()").extract()
        deposit = rowall[1:]  # '存出保证金

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[5]/td/text()").extract()
        asserttrading = rowall[1:]  # '交易性金融资产

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[6]/td/text()").extract()
        stockinvestment = rowall[1:]  # '其中：股票投资

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[7]/td/text()").extract()
        fundinvestment = rowall[1:]  # '其中：基金投资

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[8]/td/text()").extract()
        bondinvestment = rowall[1:]  # '其中：债券投资

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[9]/td/text()").extract()
        investsecurities = rowall[1:]  # '其中：资产支持证券投资'

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[10]/td/text()").extract()
        derivativeassert = rowall[1:]  # '衍生金融资产

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[11]/td/text()").extract()
        buybackassets = rowall[1:]  # '买入返售金融资产

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[12]/td/text()").extract()
        securclearreceivable = rowall[1:]  # '应收证券清算款

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[13]/td/text()").extract()
        interestreceivable = rowall[1:]  # '应收利息

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[14]/td/text()").extract()
        dividendreceivable = rowall[1:]  # '应收股利

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[15]/td/text()").extract()
        requisitionreceivables = rowall[1:]  # '应收申购款

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[16]/td/text()").extract()
        deferredtaxassets = rowall[1:]  # '递延所得税资产

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[17]/td/text()").extract()
        otherassets = rowall[1:]  # '其他资产

        rowall = response.xpath("/html/body/div/table[1]/tbody/tr[18]/td/text()").extract()
        totalassets = rowall[1:]  # '资产总计

        itemAseets = []  # 资产数组集合
        for i in len(fsrq):
            item = AssetItem()
            item['FUNDCODE'] = fundcode
            item['FSRQ'] = fsrq[i]  # '日期	              '
            item['BANKDEPOSITS'] = bankdeposits[i]  # '银行存款	          '
            item['SETTALLOWANCE'] = settallowance[i]  # '结算备付金	          '
            item['DEPOSIT'] = deposit[i]  # '存出保证金	          '
            item['ASSERTTRADING'] = asserttrading[i]  # '交易性金融资产	      '
            item['STOCKINVESTMENT'] = stockinvestment[i]  # '其中：股票投资	      '
            item['FUNDINVESTMENT'] = fundinvestment[i]  # '其中：基金投资	      '
            item['BONDINVESTMENT'] = bondinvestment[i]  # '其中：债券投资	      '
            item['INVESTSECURITIES'] = investsecurities[i]  # '其中：资产支持证券投资
            item['DERIVATIVEASSERT'] = derivativeassert[i]  # '衍生金融资产
            item['BUYBACKASSETS'] = buybackassets[i]  # '买入返售金融资产
            item['SECURCLEARRECEIVABLE'] = securclearreceivable[i]  # '应收证券清算款
            item['INTERESTRECEIVABLE'] = interestreceivable[i]  # '应收利息
            item['DIVIDENDRECEIVABLE'] = dividendreceivable[i]  # '应收股利
            item['REQUISITIONRECEIVABLES'] = requisitionreceivables[i]  # '应收申购款
            item['DEFERREDTAXASSETS'] = deferredtaxassets[i]  # '递延所得税资产
            item['OTHERASSETS'] = otherassets[i]  # '其他资产
            item['TOTALASSETS'] = totalassets[i]  # '资产总计	                   '
            itemAseets.append(item)
            print("itemAssets=" + itemAseets)
        yield itemAseets

    # 负债
    def parseLiabities(self, response, fundcode):

        th1 = response.xpath("/html/body/div/table[2]/thead/tr/th/text()").extract()
        fsrq = th1[1:]  # '日期',

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[2]/td/text()").extract()
        shorttermborrowings = rowall[1:]  # '短期借款

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[3]/td/text()").extract()
        tradingliabilit = rowall[1:]  # '交易性金融负债

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[4]/td/text()").extract()
        derivativeliabilit = rowall[1:]  # '衍生金融负债

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[5]/td/text()").extract()
        selfrepuassert = rowall[1:]  # '卖出回购金融资产款

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[6]/td/text()").extract()
        seculiqupayables = rowall[1:]  # '应付证券清算款

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[7]/td/text()").extract()
        redemptionspayable = rowall[1:]  # '应付赎回款

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[8]/td/text()").extract()
        comppayadmin = rowall[1:]  # '应付管理人报酬

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[9]/td/text()").extract()
        escrfeepayable = rowall[1:]  # '应付托管费

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[10]/td/text()").extract()
        saleservfeepay = rowall[1:]  # '应付销售服务费

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[11]/td/text()").extract()
        taxespayable = rowall[1:]  # '应付税费

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[12]/td/text()").extract()
        interestpayable = rowall[1:]  # '应付利息

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[13]/td/text()").extract()
        profitreceivable = rowall[1:]  # '应收利润

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[14]/td/text()").extract()
        defincomtaxliab = rowall[1:]  # '递延所得税负债

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[15]/td/text()").extract()
        otherliabilities = rowall[1:]  # '其他负债

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[16]/td/text()").extract()
        totalliabilities = rowall[1:]  # '负债合计
        itemLiability = []
        for i in range(0, len(fsrq)):
            item = LiabeilitiesItem()
            item['FUNDCODE'] = fundcode
            item['FSRQ'] = fsrq[i]  # '日期',
            item['SHORTTERMBORROWINGS'] = shorttermborrowings[i]  # '短期借款	          '
            item['TRADINGLIABILIT'] = tradingliabilit[i]  # '交易性金融负债	      '
            item['DERIVATIVELIABILIT'] = derivativeliabilit[i]  # '衍生金融负债	      '
            item['SELFREPUASSERT'] = selfrepuassert[i]  # '卖出回购金融资产款	  '
            item['SECULIQUPAYABLES'] = seculiqupayables[i]  # '应付证券清算款	      '
            item['REDEMPTIONSPAYABLE'] = redemptionspayable[i]  # '应付赎回款	          '
            item['COMPPAYADMIN'] = comppayadmin[i]  # '应付管理人报酬	      '
            item['ESCRFEEPAYABLE'] = escrfeepayable[i]  # '应付托管费	          '
            item['SALESERVFEEPAY'] = saleservfeepay[i]  # '应付销售服务费	      '
            item['TAXESPAYABLE'] = taxespayable[i]  # '应付税费	          '
            item['INTERESTPAYABLE'] = interestpayable[i]  # '应付利息	          '
            item['PROFITRECEIVABLE'] = profitreceivable[i]  # '应收利润	          '
            item['DEFINCOMTAXLIAB'] = defincomtaxliab[i]  # '递延所得税负债	      '
            item['OTHERLIABILITIES'] = otherliabilities[i]  # '其他负债	          '
            item['TOTALLIABILITIES'] = totalliabilities[i]  # '负债合计	          '
            itemLiability.append(item)
        print("itemLiability=" + itemLiability)
        yield itemLiability

    # 所有者权益
    def parseEquity(self, response, fundcode):

        th1 = response.xpath("/html/body/div/table[2]/thead/tr/th/text()").extract()
        fsrq = th1[1:]

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[18]/td/text()").extract()
        paidinfunds = rowall[1:]

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[19]/td/text()").extract()
        totalownequity = rowall[1:]

        rowall = response.xpath("/html/body/div/table[2]/tbody/tr[20]/td/text()").extract()
        totalliabownequity = rowall[1:]
        print("totalliabownequity=" + totalliabownequity)
        itemEquity = []
        for i in range(0, len(fsrq)):
            item = OwnerEquityItem()
            item['FUNDCODE'] = fundcode
            item['FSRQ'] = fsrq[i]  # '日期',
            item['PAIDINFUNDS'] = paidinfunds[i]  # '实收基金	'           ,
            item['TOTALOWNEQUITY'] = totalownequity[i]  # '所有者权益合计	'       ,
            item['TOTALLIABOWNEQUITY'] = totalliabownequity[i]  # '负债和所有者权益合计'	,  	,         '
            itemEquity.append(item)
        print("itemEquity=" + itemEquity)
        yield itemEquity
