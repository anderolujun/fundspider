from stockholder.utils.utils import DbUtils


class DbTests:
    def __init__(self):
        self.inst = DbUtils()

    def testexecsql(self):
        self.inst.executesql("delete from FINANCIAL_INDICATORS where id=1")
        print("delete success..")


if __name__ == "__main__":
    test = DbTests()
    test.testexecsql()
