import unittest
from datetime import timedelta
from alfred_db.helpers import now


class NowTests(unittest.TestCase):

    def setUp(self):
        self.date = now()

    def test_is_aware(self):
        self.assertIsNotNone(self.date.tzinfo)
        self.assertIsNotNone(self.date.tzinfo.utcoffset(self.date))

    def test_in_utc(self):
        self.assertEqual(self.date.tzinfo.utcoffset(self.date), timedelta(0))
