import time
from unittest import TestCase


class Sample(TestCase):
    def test_sameple_with_big_timeout(self):
        print("Testing false assert")
        self.assertEquals(1, 2)
