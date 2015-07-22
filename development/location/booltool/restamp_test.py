import unittest

import restamp
class TestRestamp(unittest.TestCase):
    def setUp(self):
        self.d1 = []
        self.d2 = []
        for i in xrange(10):
            self.d1.append({"t": i, "d": i})
            self.d2.append({"t": i+0.3, "d": i})
    def test_findtime(self):
        self.assertEqual(restamp.findtime(self.d1,3.3)["t"],3)
    def test_restamp(self):
        v = restamp.restamp(self.d1,self.d2)
        self.assertEqual(v[0]["t"],1)
        self.assertEqual(v[0]["d"],1)
        self.assertEqual(v[0]["d2"],0)
        self.assertEqual(len(v),9)

if __name__=="__main__":
    unittest.main()