import scrapy
from scrapy_splash import SplashRequest
from stockholder.items import ProfitFeeItem, ProfitIncomeItem


class FundprofitSpider(scrapy.Spider):
    name = 'fundprofit'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://fundf10.eastmoney.com/lrfpb_003064.html']

    def __init__(self, fundcode='', *args, **kwargs):
        super(FundprofitSpider, self).__init__(*args, **kwargs)
        self.fundcode = fundcode
        self.start_urls = [f'http://fundf10.eastmoney.com/lrfpb_{self.fundcode}.html']

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
        # 解析财报周期 //*[@id='cwtable']/div/table/thead/tr/th
        fsrq = response.xpath("//*[@id='cwtable']/div/table/thead/tr/th/text()").extract()
        # 利润数据 //*[@id="cwtable"]/div/table/tbody/tr[1]/td[1]
        row1 = response.xpath("//*[@id='cwtable']/div/table/tbody/tr/td/text()").extract()
        row1 = row1[5:]
        # 利息收入
        interestincome = row1[1:5]
        # 存款利息收入
        row1 = row1[5:]
        interestincomedeposits = row1[1:5]
        # 债券利息收入
        row1 = row1[5:]
        interestincomebonds = row1[1:5]

        # 资产支持证券利息收入
        row1 = row1[5:]
        interestincomesecurities = row1[1:5]
        # 投资收益
        row1 = row1[5:]
        investmentincome = row1[1:5]
        # 股票投资收益
        row1 = row1[5:]
        equityinvestmentincome = row1[1:5]
        # 基金投资收益
        row1 = row1[5:]
        fundinvestmentincome = row1[1:5]
        # 债券投资收益
        row1 = row1[5:]
        bondinvestmentincome = row1[1:5]
        # 资产支持证券投资收益
        row1 = row1[5:]
        investmentincomeasset = row1[1:5]
        # 衍生工具收益
        row1 = row1[5:]
        gainderivativeinstruments = row1[1:5]
        # 股利收益
        row1 = row1[5:]
        dividendincome = row1[1:5]
        # 公允价值变动收益
        row1 = row1[5:]
        gainchangesfairvalue = row1[1:5]
        # 汇兑收益
        row1 = row1[5:]
        foreignexchangegain = row1[1:5]
        # 其他收入
        row1 = row1[5:]
        otherincome = row1[1:5]

        # FEES 费用
        row1 = row1[5:]
        fees = row1[1:5]
        # MANAGERCOMPENSATION 管理人报酬
        row1 = row1[5:]
        managercompensation = row1[1:5]
        # ESCROWFEE 托管费
        row1 = row1[5:]
        escrowfee = row1[1:5]
        # SALESSERVICEFEE 销售服务费
        row1 = row1[5:]
        salesservicefee = row1[1:5]
        # TRANSACTIONFEES 交易费用
        row1 = row1[5:]
        transactionfees = row1[1:5]
        # INTERESTEXPENSE 利息支出
        row1 = row1[5:]
        interestexpense = row1[1:5]
        # EXPENSALEFINANCIALASSETS 其中：卖出回购金融资产支出
        row1 = row1[5:]
        expensalefinancialassets = row1[1:5]
        # OTHERFEES # 其他费用
        row1 = row1[5:]
        otherfees = row1[1:5]
        # INCOMETAXEXPENSE # 所得税费用
        row1 = row1[5:]
        incometaxexpense = row1[1:5]

        for i in range(len(fsrq)):
            item = ProfitIncomeItem()
            # 编码
            item['FUNDCODE'] = self.fundcode
            item['FSRQ'] = fsrq[i]
            # 利息收入
            item['INTERESTINCOME'] = interestincome[i]
            # 存款利息收入
            item['INTERESTINCOMEDEPOSITS'] = interestincomedeposits[i]
            # 债券利息收入
            item['INTERESTINCOMEBONDS'] = interestincomebonds[i]
            # 资产支持证券利息收入
            item['INTERESTINCOMESECURITIES'] = interestincomesecurities[i]
            # 投资收益
            item['INVESTMENTINCOME'] = investmentincome[i]
            # 股票投资收益
            item['EQUITYINVESTMENTINCOME'] = equityinvestmentincome[i]
            # 基金投资收益
            item['FUNDINVESTMENTINCOME'] = fundinvestmentincome[i]
            # 债券投资收益
            item['BONDINVESTMENTINCOME'] = bondinvestmentincome[i]
            # 资产支持证券投资收益
            item['INVESTMENTINCOMEASSET'] = investmentincomeasset[i]
            # 衍生工具收益
            item['GAINDERIVATIVEINSTRUMENTS'] = gainderivativeinstruments[i]
            # 股利收益
            item['DIVIDENDINCOME'] = dividendincome[i]
            # 公允价值变动收益
            item['GAINCHANGESFAIRVALUE'] = gainchangesfairvalue[i]
            # 汇兑收益
            item['FOREIGNEXCHANGEGAIN'] = foreignexchangegain[i]
            # 其他收入
            item['OTHERINCOME'] = otherincome[i]
            # item_list.append(item)
            yield item

        # 费用
        for i in range(len(fsrq)):
            it = ProfitFeeItem()
            # 编码
            it['FUNDCODE'] = self.fundcode
            it['FSRQ'] = fsrq[i]
            # 费用
            it['FEES'] = fees[i]
            # 管理人报酬
            it['MANAGERCOMPENSATION'] = managercompensation[i]
            # 托管费
            it['ESCROWFEE'] = escrowfee[i]
            # 销售服务费
            it['SALESSERVICEFEE'] = salesservicefee[i]
            # 交易费用
            it['TRANSACTIONFEES'] = transactionfees[i]
            # 利息支出
            it['INTERESTEXPENSE'] = interestexpense[i]
            # 其中：卖出回购金融资产支出
            it['EXPENSALEFINANCIALASSETS'] = expensalefinancialassets[i]
            # 其他费用
            it['OTHERFEES'] = otherfees[i]
            # 所得税费用
            it['INCOMETAXEXPENSE'] = incometaxexpense[i]
            yield it
