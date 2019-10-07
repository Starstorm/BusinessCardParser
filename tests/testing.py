# -*- coding: utf-8 -*-
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BusinessCardParser.BusinessCardParser import BusinessCardParser
from BusinessCardParser.ContactInfo import ContactInfo
import unittest


class TestSuite(unittest.TestCase):
    """Test cases."""

    def test_thoughts(self):
        pass

if __name__ == '__main__':
    unittest.main()
