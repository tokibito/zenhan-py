# -*- coding: utf-8 *-

import sys
import unittest

import zenhan


def u(s):
    return s if sys.version_info >= (3, 0) else unicode(s, 'utf8')


class TestZenhan(unittest.TestCase):
    def setUp(self):
        self.original = u("ﾟabcＤＥﾞＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_h2z_ascii_only(self):
        converted = zenhan.h2z(self.original, zenhan.ASCII)
        self.assertEqual(converted, u("ﾟａｂｃＤＥﾞＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"))

    def test_h2z_digit_only(self):
        converted = zenhan.h2z(self.original, zenhan.DIGIT)
        self.assertEqual(converted, u("ﾟabcＤＥﾞＦ１２３４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"))

    def test_h2z_kana_only(self):
        converted = zenhan.h2z(self.original, zenhan.KANA)
        self.assertEqual(converted, u("゜abcＤＥ゛Ｆ123４５６アガサダナバビプペ゜"))

    def test_h2z_ascii_and_digit(self):
        converted = zenhan.h2z(self.original, zenhan.ASCII|zenhan.DIGIT)
        self.assertEqual(converted, u("ﾟａｂｃＤＥﾞＦ１２３４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"))

    def test_h2z_ascii_and_kana(self):
        converted = zenhan.h2z(self.original, zenhan.ASCII|zenhan.KANA)
        self.assertEqual(converted, u("゜ａｂｃＤＥ゛Ｆ123４５６アガサダナバビプペ゜"))

    def test_h2z_digit_and_kana(self):
        converted = zenhan.h2z(self.original, zenhan.DIGIT|zenhan.KANA)
        self.assertEqual(converted, u("゜abcＤＥ゛Ｆ１２３４５６アガサダナバビプペ゜"))

    def test_h2z_all(self):
        converted = zenhan.h2z(self.original, zenhan.ALL)
        self.assertEqual(converted, u("゜ａｂｃＤＥ゛Ｆ１２３４５６アガサダナバビプペ゜"))
        self.assertEqual(zenhan.h2z(self.original, zenhan.ALL),
                         zenhan.h2z(self.original,
                                    zenhan.ASCII|zenhan.DIGIT|zenhan.KANA))

    def test_z2h_ascii_only(self):
        converted = zenhan.z2h(self.original, zenhan.ASCII)
        self.assertEqual(converted, u("ﾟabcDEﾞF123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"))

    def test_z2h_digit_only(self):
        converted = zenhan.z2h(self.original, zenhan.DIGIT)
        self.assertEqual(converted, u("ﾟabcＤＥﾞＦ123456ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"))

    def test_z2h_kana_only(self):
        converted = zenhan.z2h(self.original, zenhan.KANA)
        self.assertEqual(converted, u("ﾟabcＤＥﾞＦ123４５６ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ"))

    def test_z2h_ascii_and_digit(self):
        converted = zenhan.z2h(self.original, zenhan.ASCII|zenhan.DIGIT)
        self.assertEqual(converted, u("ﾟabcDEﾞF123456ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"))

    def test_z2h_ascii_and_kana(self):
        converted = zenhan.z2h(self.original, zenhan.ASCII|zenhan.KANA)
        self.assertEqual(converted, u("ﾟabcDEﾞF123４５６ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ"))

    def test_z2h_digit_and_kana(self):
        converted = zenhan.z2h(self.original, zenhan.DIGIT|zenhan.KANA)
        self.assertEqual(converted, u("ﾟabcＤＥﾞＦ123456ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ"))

    def test_z2h_all(self):
        converted = zenhan.z2h(self.original, zenhan.ALL)
        self.assertEqual(converted, u("ﾟabcDEﾞF123456ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ"))
        self.assertEqual(converted,
                         zenhan.z2h(self.original,
                                    zenhan.ASCII|zenhan.DIGIT|zenhan.KANA))


if __name__ == '__main__':
    unittest.main()
