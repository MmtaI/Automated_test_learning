import unittest
from Api_test.api_unittest import Testcase
from BeautifulReport import BeautifulReport


# 添加测试用例
discover = unittest.defaultTestLoader.discover(start_dir='./', pattern='api_unittest.py')
# 生成BR，filename=file.rep 是测试报告的路径带文件名
bp = BeautifulReport(discover)
bp.report(description='测试报告的desc', filename='report.html', report_dir='./report_html')
