# -*- coding: utf-8 -*-

from BusinessCardParser import BusinessCardParser
import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(bcp.hmm())


if __name__ == '__main__':
    unittest.main()
