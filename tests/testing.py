# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BusinessCardParser import ContactInfo, BusinessCardParser
import unittest


class TestSuite(unittest.TestCase):
    """Test cases."""

    def test_thoughts(self):
        my_info = ContactInfo("Derp","Derp","Derp")
        print(str(my_info))

if __name__ == '__main__':
    unittest.main()
