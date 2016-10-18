
import unittest
import sys
from copy import deepcopy

import numpy as np

sys.path.append("../miscpy/")
from miscpy import hstr


class TestHString(unittest.TestCase):

    def setUp(self):
        np.random.seed(12345)

    def test_sort_hstr(self):
        sorted_str = [hstr("chr1"), hstr("chr2"), hstr("chr10"), hstr("chr10"), hstr("chr1x3"),hstr("chr1x23")]
        shuffled_str = deepcopy(sorted_str)

        for i in range(10):
            # shuffle
            np.random.shuffle(shuffled_str)
            self.assertEqual(sorted_str, sorted(shuffled_str))


if __name__ == '__main__':
    unittest.main()