# -*- coding: utf-8 -*-
import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BusinessCardParser.BusinessCardParser import BusinessCardParser
from BusinessCardParser.ContactInfo import ContactInfo
class TestSuite(unittest.TestCase):
    """Test cases."""

    def test_parser(self):
        my_info = BusinessCardParser()
		
    def test_contact(self):
        my_info = ContactInfo("Derp","Derp","Derp")

if __name__ == '__main__':
	unittest.main()
