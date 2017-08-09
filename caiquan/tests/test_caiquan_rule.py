# -*- coding:utf-8 -*-

from utils.caiquan_rule import CaiquanRule
import unittest
import random

class CaiquanRuleTest(unittest.TestCase):
    def setUp(self):
        self.caiquanrule = CaiquanRule()
        self._user_choice = random.choice(('2', '5', '0'))

    def tearDown(self):
        pass

    def test_input_choice(self):
        #测试机器名与人名不同时
        choice_result1 = self.caiquanrule.input_choice('Young','Nick', self._user_choice)
        self.assertTrue(choice_result1 in (['Nick','5'],['Nick','2'],['Nick','0']))

        #测试机器名与人名相同时
        choice_result2 = self.caiquanrule.input_choice('Young', 'Young', self._user_choice)
        self.assertEqual(choice_result2, ['Young', self._user_choice])

    def test_caiquan_compare(self):
        l1 = ['Nick','5']
        l2 = ['James','2']
        l3 = ['Kobe','2']

        #测试猜拳结果不同时的反馈
        caiquan_result1 = self.caiquanrule.caiquan_compare(l1,l2)
        self.assertEqual(caiquan_result1,'James')

        #测试猜拳结果相同时的反馈
        caiquan_result2 = self.caiquanrule.caiquan_compare(l2, l3)
        self.assertEqual(caiquan_result2, None)

    def test_caiquan_result(self):

        #测试总姓名为偶数时情况
        namelist2 = ['Young','Nick','Kobe','Wade','Duncun']
        username2 = 'James'
        remain_name2, gamelist2 = self.caiquanrule.caiquan_result(username2, namelist2,self._user_choice)
        namelist2.append(username2)
        self.assertTrue([True for c in namelist2 if c in remain_name2])

        #测试总姓名为奇数时情况
        namelist1 = ['Young','Nick']
        username1 = 'James'
        remain_name1,gamelist1 = self.caiquanrule.caiquan_result(username1,namelist1,self._user_choice)
        namelist1.append(username1)
        self.assertTrue( [True for c in namelist1 if c in remain_name1])



if __name__ == '__main__':
    unittest.main()