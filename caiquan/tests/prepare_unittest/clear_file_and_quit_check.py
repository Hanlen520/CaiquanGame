# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os

class Test_clear_file_and_quit(unittest.TestCase):

    def setUp(self):
        print 'Testcases_clear_file_and_quit_check start'
        self.cp = caiquan_prepare.Caiquan_prepare()
        #新建savefile_Tom文件
        open('savefile_Tom', 'w')

    def tearDown(self):
        print 'Testcases_clear_file_and_quit_check over\n'

    def clear_file_and_quit_check1(self):
        '''
        测试清除功能
        :return:
        '''
        print 'check1'
        #检查是否生成savefile_Tom
        print os.path.exists('savefile_Tom')
        self.cp.clear_file_and_quit('savefile_Tom')
        result = os.path.exists('savefile_Tom')
        self.assertFalse(result, msg='clear_file_and_quit_check1_Failed')

    if __name__ == '__main__':
        unittest.main()