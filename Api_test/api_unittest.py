import unittest
from Api_test.res import Api_requests
from ddt import ddt, file_data
from Api_test.res_yaml import Api_yaml
from Api_test.open_excel import excel_yaml


@ddt()
class Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        excel_yaml()

    def test_01(self):
        re = Api_requests()
        for i in range(1, re.z):
            m = re.res(i)
            a = re.acc(i, m)
            self.assertTrue(a)

    @file_data('case.yaml')
    def test_02(self, **kwargs):
        re = Api_yaml()
        re.res(**kwargs)
        self.assertEqual(str(kwargs['expect']), re.acc(**kwargs))


if __name__ == '__main__':
    unittest.main()


