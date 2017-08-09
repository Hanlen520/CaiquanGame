# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest

class Test_name_define(unittest.TestCase):

    def setUp(self):
        print 'Testcases_name start'
        self.cp = caiquan_prepare.Caiquan_prepare()

    def tearDown(self):
        print 'Testcases_name over\n'

    def name_define_check1(self):
        '''
        为空校验
        :return:
        '''
        print 'check1'
        name = '   '
        result = self.cp.name_define_and_verify(name)
        self.assertFalse(result, msg="name_define_check1_Failed")
        print name

    def name_define_check2(self):
        '''
        有效等价类
        :return:
        '''
        print 'check2'
        name = 'Tom 123 ,./'
        result = self.cp.name_define_and_verify(name)
        self.assertTrue(result, msg="name_define_check2_Failed")
        print name

    def name_define_check3(self):
        '''
        长度校验
        :return:
        '''
        print 'check3'
        name = 'Tom ChruseTom ChruseTom ChruseTom ChruseTom ChruseTom Chruse'
        result = self.cp.name_define_and_verify(name)
        self.assertFalse(result, msg="name_define_check3_Failed")
        print name

    if __name__ == '__main__':
        unittest.main()