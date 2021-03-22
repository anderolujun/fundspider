# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from stockholder.items import StockholderItem, ProfitFeeItem, ProfitIncomeItem, OwnerEquityItem, AssetItem, \
    LiabeilitiesItem
from stockholder.utils.utils import DbUtils


class MySQLPipeline:

    def __init__(self):
        self.dbutil = DbUtils()

    def process_item(self, item, spider):
        # 财务指标
        if item.__class__ == StockholderItem:
            try:
                self.dbutil.insert(
                    """insert into FINANCIAL_INDICATORS(FUNDCODE,FSRQ,COMPROFIT,NETPROFIT,UNITPROFIT,NGROWTH,
                        FNGROWTH, DISPROFIT,DIFUNTIPROFIT,ENDNAV,ENDUNITNAV,FCNGROWTH,FIELDTYPE) value (%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    *(item['FUNDCODE'],
                      item['FSRQ'],
                      item['COMPROFIT'],
                      item['NETPROFIT'],
                      item['UNITPROFIT'],
                      item['NGROWTH'],
                      item['FNGROWTH'],
                      item['DISPROFIT'],
                      item['DIFUNTIPROFIT'],
                      item['ENDNAV'],
                      item['ENDUNITNAV'],
                      item['FCNGROWTH'],
                      item['FIELDTYPE']
                      ))
            except Exception as error:
                print(error)
        # 利润-费用
        elif item.__class__ == ProfitFeeItem:
            try:
                self.dbutil.insert(
                    """insert into PROFIT_STATEMENT_FEES(FUNDCODE,FSRQ,FEES,MANAGERCOMPENSATION,ESCROWFEE,
                    SALESSERVICEFEE, TRANSACTIONFEES,INTERESTEXPENSE,EXPENSALEFINANCIALASSETS,OTHERFEES,
                    INCOMETAXEXPENSE) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    *(item['FUNDCODE'],
                      item['FSRQ'],
                      item['FEES'],
                      item['MANAGERCOMPENSATION'],
                      item['ESCROWFEE'],
                      item['SALESSERVICEFEE'],
                      item['TRANSACTIONFEES'],
                      item['INTERESTEXPENSE'],
                      item['EXPENSALEFINANCIALASSETS'],
                      item['OTHERFEES'],
                      item['INCOMETAXEXPENSE']
                      ))
            except Exception as error:
                print(error)
        # 利润-收入
        elif item.__class__ == ProfitIncomeItem:
            try:
                self.dbutil.insert(
                    """insert into PROFIT_STATEMENT_INCOME(FUNDCODE,FSRQ,INTERESTINCOME,INTERESTINCOMEDEPOSITS, 
                        INTERESTINCOMEBONDS,INTERESTINCOMESECURITIES, INVESTMENTINCOME,EQUITYINVESTMENTINCOME, 
                        FUNDINVESTMENTINCOME,BONDINVESTMENTINCOME, INVESTMENTINCOMEASSET,GAINDERIVATIVEINSTRUMENTS, 
                        DIVIDENDINCOME,GAINCHANGESFAIRVALUE,FOREIGNEXCHANGEGAIN,OTHERINCOME) value (%s,%s, %s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)""",
                    *(item['FUNDCODE'],
                      item['FSRQ'],
                      item['INTERESTINCOME'],
                      item['INTERESTINCOMEDEPOSITS'],
                      item['INTERESTINCOMEBONDS'],
                      item['INTERESTINCOMESECURITIES'],
                      item['INVESTMENTINCOME'],
                      item['EQUITYINVESTMENTINCOME'],
                      item['FUNDINVESTMENTINCOME'],
                      item['BONDINVESTMENTINCOME'],
                      item['INVESTMENTINCOMEASSET'],
                      item['GAINDERIVATIVEINSTRUMENTS'],
                      item['DIVIDENDINCOME'],
                      item['GAINCHANGESFAIRVALUE'],
                      item['FOREIGNEXCHANGEGAIN'],
                      item['OTHERINCOME']
                      ))
            except Exception as error:
                print(error)
        elif item.__class__ == AssetItem:  # 资产
            print("inset assetitem ")
            try:
                self.dbutil.insert(
                    """INSERT INTO BALANCE_SHEET_ASSETS (FUNDCODE,FSRQ                      ,
                                  BANKDEPOSITS              ,
                                  SETTALLOWANCE             ,
                                  DEPOSIT                   ,
                                  ASSERTTRADING             ,
                                  STOCKINVESTMENT           ,
                                  FUNDINVESTMENT            ,
                                  BONDINVESTMENT            ,
                                  INVESTSECURITIES          ,
                                  DERIVATIVEASSERT          ,
                                  BUYBACKASSETS             ,
                                  SECURCLEARRECEIVABLE      ,
                                  INTERESTRECEIVABLE        ,
                                  DIVIDENDRECEIVABLE        ,
                                  REQUISITIONRECEIVABLES    ,
                                  DEFERREDTAXASSETS         ,
                                  OTHERASSETS               ,
                                  TOTALASSETS      	        ) 
                                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    *(item['FUNDCODE'],
                      item['FSRQ'],
                      item['BANKDEPOSITS'],
                      item['SETTALLOWANCE'],
                      item['DEPOSIT'],
                      item['ASSERTTRADING'],
                      item['STOCKINVESTMENT'],
                      item['FUNDINVESTMENT'],
                      item['BONDINVESTMENT'],
                      item['INVESTSECURITIES'],
                      item['DERIVATIVEASSERT'],
                      item['BUYBACKASSETS'],
                      item['SECURCLEARRECEIVABLE'],
                      item['INTERESTRECEIVABLE'],
                      item['DIVIDENDRECEIVABLE'],
                      item['REQUISITIONRECEIVABLES'],
                      item['DEFERREDTAXASSETS'],
                      item['OTHERASSETS'],
                      item['TOTALASSETS']
                      ))
            except Exception as error:
                print(error)
            print("inset assetitem  finished")
        elif item.__class__ == LiabeilitiesItem:  # 负债
            try:
                self.dbutil.insert(
                    """INSERT INTO BALANCE_SHEET_LIABILITIES(
                          FUNDCODE            ,
                          FSRQ                ,
                          SHORTTERMBORROWINGS ,
                          TRADINGLIABILIT     ,
                          DERIVATIVELIABILIT  ,
                          SELFREPUASSERT      ,
                          SECULIQUPAYABLES    ,
                          REDEMPTIONSPAYABLE  ,
                          COMPPAYADMIN        ,
                          ESCRFEEPAYABLE      ,
                          SALESERVFEEPAY      ,
                          TAXESPAYABLE        ,
                          INTERESTPAYABLE     ,
                          PROFITRECEIVABLE    ,
                          DEFINCOMTAXLIAB     ,
                          OTHERLIABILITIES    ,
                          TOTALLIABILITIES    )
                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    *(
                        item['FUNDCODE'],
                        item['FSRQ'],
                        item['SHORTTERMBORROWINGS'],
                        item['TRADINGLIABILIT'],
                        item['DERIVATIVELIABILIT'],
                        item['SELFREPUASSERT'],
                        item['SECULIQUPAYABLES'],
                        item['REDEMPTIONSPAYABLE'],
                        item['COMPPAYADMIN'],
                        item['ESCRFEEPAYABLE'],
                        item['SALESERVFEEPAY'],
                        item['TAXESPAYABLE'],
                        item['INTERESTPAYABLE'],
                        item['PROFITRECEIVABLE'],
                        item['DEFINCOMTAXLIAB'],
                        item['OTHERLIABILITIES'],
                        item['TOTALLIABILITIES']
                    ))
            except Exception as error:
                print(error)
        elif item.__class__ == OwnerEquityItem:  # 所有者权益
            try:
                self.dbutil.insert(
                    """INSERT INTO BALANCE_SHEET_OWNER_EQUITY(
                          FUNDCODE            ,
                          FSRQ                ,
                          PAIDINFUNDS         , 
                          TOTALOWNEQUITY      ,
                          TOTALLIABOWNEQUITY )
                      VALUES (%s,%s,%s,%s,%s)""",
                    *(
                        item['FUNDCODE'],
                        item['FSRQ'],
                        item['PAIDINFUNDS'],
                        item['TOTALOWNEQUITY'],
                        item['TOTALLIABOWNEQUITY']
                    ))
            except Exception as error:
                print(error)
            return item

    def close_spider(self, spider):
        self.dbutil.opencon().close()
        print("db connection closed by dbutils....")
