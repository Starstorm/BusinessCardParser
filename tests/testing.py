# -*- coding: utf-8 -*-
import sys, os, spacy, names_dataset, unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BusinessCardParser.BusinessCardParser import BusinessCardParser

class TestSuite(unittest.TestCase):
    """Test cases."""

    def test_thoughts(self):
        my_info = BusinessCardParser()
        print(str(my_info))

if __name__ == '__main__':
    unittest.main()
