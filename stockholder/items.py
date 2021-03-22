# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 财务指标
class StockholderItem(scrapy.Item):
    # define the fields for your item here like:
    # 编码
    FUNDCODE = scrapy.Field()
    # 本期已实现收益
    COMPROFIT = scrapy.Field()
    # 本期利润
    NETPROFIT = scrapy.Field()
    # 加权平均基金份额本期利润
    UNITPROFIT = scrapy.Field()
    # 本期加权平均净值利润率
    NGROWTH = scrapy.Field()
    # 本期基金份额净值增长率
    FNGROWTH = scrapy.Field()
    # 期末可供分配利润
    DISPROFIT = scrapy.Field()
    # 期末可供分配基金份额利润
    DIFUNTIPROFIT = scrapy.Field()
    # 期末基金资产净值
    ENDNAV = scrapy.Field()
    # 期末基金份额净值
    ENDUNITNAV = scrapy.Field()
    # 基金份额累计净值增长率
    FCNGROWTH = scrapy.Field()
    # 财务指标大类
    FIELDTYPE = scrapy.Field()
    # 报告周期
    FSRQ = scrapy.Field()


# 利润收入
class ProfitIncomeItem(scrapy.Item):
    # define the fields for your item here like:
    # 编码
    FUNDCODE = scrapy.Field()
    # 报告周期
    FSRQ = scrapy.Field()
    # 利息收入
    INTERESTINCOME = scrapy.Field()
    # 存款利息收入
    INTERESTINCOMEDEPOSITS = scrapy.Field()
    # 债券利息收入
    INTERESTINCOMEBONDS = scrapy.Field()
    # 资产支持证券利息收入
    INTERESTINCOMESECURITIES = scrapy.Field()
    # 投资收益
    INVESTMENTINCOME = scrapy.Field()
    # 股票投资收益
    EQUITYINVESTMENTINCOME = scrapy.Field()
    # 基金投资收益
    FUNDINVESTMENTINCOME = scrapy.Field()
    # 债券投资收益
    BONDINVESTMENTINCOME = scrapy.Field()
    # 资产支持证券投资收益
    INVESTMENTINCOMEASSET = scrapy.Field()
    # 衍生工具收益
    GAINDERIVATIVEINSTRUMENTS = scrapy.Field()
    # 股利收益
    DIVIDENDINCOME = scrapy.Field()
    # 公允价值变动收益
    GAINCHANGESFAIRVALUE = scrapy.Field()
    # 汇兑收益
    FOREIGNEXCHANGEGAIN = scrapy.Field()
    # 其他收入
    OTHERINCOME = scrapy.Field()


# 利润费用
class ProfitFeeItem(scrapy.Item):
    # define the fields for your item here like:
    # 编码
    FUNDCODE = scrapy.Field()
    # 报告周期
    FSRQ = scrapy.Field()
    # 费用
    FEES = scrapy.Field()
    # 管理人报酬
    MANAGERCOMPENSATION = scrapy.Field()
    # 托管费
    ESCROWFEE = scrapy.Field()
    # 销售服务费
    SALESSERVICEFEE = scrapy.Field()
    # 交易费用
    TRANSACTIONFEES = scrapy.Field()
    # 利息支出
    INTERESTEXPENSE = scrapy.Field()
    # 其中：卖出回购金融资产支出
    EXPENSALEFINANCIALASSETS = scrapy.Field()
    # 其他费用
    OTHERFEES = scrapy.Field()
    # 所得税费用
    INCOMETAXEXPENSE = scrapy.Field()


# 资产负债表-资产
class AssetItem(scrapy.Item):
    FUNDCODE = scrapy.Field()  # 基金代码
    FSRQ = scrapy.Field()  # '日期	              '
    BANKDEPOSITS = scrapy.Field()  # '银行存款	          '
    SETTALLOWANCE = scrapy.Field()  # '结算备付金	          '
    DEPOSIT = scrapy.Field()  # '存出保证金	          '
    ASSERTTRADING = scrapy.Field()  # '交易性金融资产	      '
    STOCKINVESTMENT = scrapy.Field()  # '其中：股票投资	      '
    FUNDINVESTMENT = scrapy.Field()  # '其中：基金投资	      '
    BONDINVESTMENT = scrapy.Field()  # '其中：债券投资	      '
    INVESTSECURITIES = scrapy.Field()  # '其中：资产支持证券投资
    DERIVATIVEASSERT = scrapy.Field()  # '衍生金融资产
    BUYBACKASSETS = scrapy.Field()  # '买入返售金融资产
    SECURCLEARRECEIVABLE = scrapy.Field()  # '应收证券清算款
    INTERESTRECEIVABLE = scrapy.Field()  # '应收利息
    DIVIDENDRECEIVABLE = scrapy.Field()  # '应收股利
    REQUISITIONRECEIVABLES = scrapy.Field()  # '应收申购款
    DEFERREDTAXASSETS = scrapy.Field()  # '递延所得税资产
    OTHERASSETS = scrapy.Field()  # '其他资产
    TOTALASSETS = scrapy.Field()  # '资产总计


# 资产负债表-负债
class LiabeilitiesItem(scrapy.Item):
    FUNDCODE = scrapy.Field()  # '基金代码',
    FSRQ = scrapy.Field()  # '日期',
    SHORTTERMBORROWINGS = scrapy.Field()  # '短期借款	          '
    TRADINGLIABILIT = scrapy.Field()  # '交易性金融负债	      '
    DERIVATIVELIABILIT = scrapy.Field()  # '衍生金融负债	      '
    SELFREPUASSERT = scrapy.Field()  # '卖出回购金融资产款	  '
    SECULIQUPAYABLES = scrapy.Field()  # '应付证券清算款	      '
    REDEMPTIONSPAYABLE = scrapy.Field()  # '应付赎回款	          '
    COMPPAYADMIN = scrapy.Field()  # '应付管理人报酬	      '
    ESCRFEEPAYABLE = scrapy.Field()  # '应付托管费	          '
    SALESERVFEEPAY = scrapy.Field()  # '应付销售服务费	      '
    TAXESPAYABLE = scrapy.Field()  # '应付税费	          '
    INTERESTPAYABLE = scrapy.Field()  # '应付利息	          '
    PROFITRECEIVABLE = scrapy.Field()  # '应收利润	          '
    DEFINCOMTAXLIAB = scrapy.Field()  # '递延所得税负债	      '
    OTHERLIABILITIES = scrapy.Field()  # '其他负债	          '
    TOTALLIABILITIES = scrapy.Field()  # '负债合计	          '


class OwnerEquityItem(scrapy.Item):
    FUNDCODE = scrapy.Field()  # '基金代码',
    FSRQ = scrapy.Field()  # '日期',
    PAIDINFUNDS = scrapy.Field()  # '实收基金	'           ,
    TOTALOWNEQUITY = scrapy.Field()  # '所有者权益合计	'       ,
    TOTALLIABOWNEQUITY = scrapy.Field()  # '负债和所有者权益合计'	,
