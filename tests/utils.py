import unittest

from altunityrunner import AltUnityDriver


class AltUnityTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltUnityDriver(enable_logging=False)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
