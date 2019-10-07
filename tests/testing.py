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
        my_info = my_parser.getContactInfo("""
            Arthur Wilson
            Software Engineer
            Decision & Security Technologies
            ABC Technologies
            123 North 11th Street
            Suite 229
            Arlington, VA 22209
            Tel: +1 (703) 555-1259
            Fax: +1 (703) 555-1200
            awilson@abctech.com
		""")
        self.assertEqual("Arthur Wilson", my_info.getName())
        self.assertEqual("17035551259", my_info.getPhoneNumber())
        self.assertEqual("awilson@abctech.com", my_info.getEmailAddress())
		
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
