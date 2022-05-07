import unittest
import HtmlTestRunner # pip install html-testRunner

from Cursuri_IT_Factory.Curs9.test4_Unittest import Test
from Cursuri_IT_Factory.Curs9.test5_Exemple import Test2


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test2),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)