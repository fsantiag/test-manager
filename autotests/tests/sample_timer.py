import time
from unittest import TestCase


class Sample(TestCase):
    def test_sameple_with_big_timeout(self):
        print("Starting to sleep for 60 seconds now!")
        time.sleep(60)
        print("Sleep completed! Exiting...")
