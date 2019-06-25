import os
from altunityrunner import AltrunUnityDriver
import unittest
import pytest

class TestBase(unittest.TestCase):
    plaform = os.getenv('TESTS_PLATFORM', 'android')

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltrunUnityDriver(None, cls.plaform)

    @classmethod    
    def tearDownClass(cls):
        cls.altdriver.stop()