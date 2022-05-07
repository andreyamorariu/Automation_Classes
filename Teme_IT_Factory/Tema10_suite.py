'''
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la intalnirea 10
(care au clasa). Generati raportul
'''

import unittest
import HtmlTestRunner # pip install html-testRunner

from Teme_IT_Factory.Tema9 import Login
from Cursuri_IT_Factory.Curs10.test3_Alerts import Alerts
from Cursuri_IT_Factory.Curs10.test4_Authentication import Authentication
from Cursuri_IT_Factory.Curs10.test5_ContextMenu import ContextMenu
from Cursuri_IT_Factory.Curs10.test6_KeyBoard import Keyboard


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)