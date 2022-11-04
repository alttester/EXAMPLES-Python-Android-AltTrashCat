import unittest

from alttester import AltDriver


class AltTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltDriver(enable_logging=False)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
