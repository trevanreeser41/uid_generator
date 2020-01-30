from unittest import TestCase
from baseX import BaseXConverter
from uid import unpack, generate, pack
import time

def dbuid():
    uid = generate()
    return uid

# Run this from its parent directory:
#
#    python3 -m unittest tests/test_baseX
#

class BaseXTester(TestCase):

    def test_base2(self):
        conv = BaseXConverter('01')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0b}'.format(i))    # test against python's builtin
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_base16(self):
        conv = BaseXConverter('0123456789ABCDEF')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0X}'.format(i))
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_base58(self):
        conv = BaseXConverter('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')
        i = 1234567890
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_uid(self):
        uids = set(dbuid() for i in range(100))
        self.assertEqual(len(uids), 100)

    def test_unpack_pack(self):
        uid1 = dbuid()
        uid2 = dbuid()
        #unpack
        dt, counter, shard_id = unpack(uid1)
        print(dt, counter, shard_id)
        dt2, counter2, shard_id2 = unpack(uid2)
        print(dt2, counter2, shard_id2)
        self.assertLess((dt2-dt)/1000, 10)
        self.assertLess(int(round(time.time())) - (dt/1000), 10)
        #pack
        self.assertEqual(uid1, pack(dt, counter, shard_id))
        self.assertEqual(uid2, pack(dt2, counter2, shard_id2))