# -*- coding: utf-8 -*-
import unittest
import sys, os, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BusinessCardParser.BusinessCardParser import BusinessCardParser
from BusinessCardParser.ContactInfo import ContactInfo
class TestSuite(unittest.TestCase):
    """Test cases."""

    def test_parser(self):
        my_parser = BusinessCardParser()
		
    def test_contact(self):
        my_info = ContactInfo("Arthur Wilson","17035551259","awilson@abctech.com")
        self.assertIsInstance(my_info.getName(), str)
        self.assertIsInstance(my_info.getPhoneNumber(), str)
        self.assertIsInstance(my_info.getEmailAddress(), str)
        self.assertEqual("Arthur Wilson", my_info.getName())
        self.assertEqual("17035551259", my_info.getPhoneNumber())
        self.assertEqual("awilson@abctech.com", my_info.getEmailAddress())

if __name__ == '__main__':
	unittest.main()
