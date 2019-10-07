# -*- coding: utf-8 -*-

import ../BusinessCardParser as bcp
import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(bcp.hmm())


if __name__ == '__main__':
    unittest.main()