# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os

class Test_name_before_game(unittest.TestCase):

    def setUp(self):
        print 'Testcases_name_before_game start'
        self.cp = caiquan_prepare.Caiquan_prepare()

    def tearDown(self):
        print 'Testcases_name_before_game over\n'

    def name_before_game_check1(self):
        '''
        测试正常功能
        :return:
        '''
        print 'check1'
        print self.cp.name_before_game(10,'Tom')

    def name_before_game_check2(self):
        '''
        测试边界值
        :return:
        '''
        print 'check2'
        print self.cp.name_before_game(49,'Liu')

    def name_before_game_check3(self):
        '''
        测试是否把用户名同名的机器人明删掉
        :return:
        '''
        print 'check3'
        print self.cp.name_before_game(49,'Tom')

    if __name__ == "__main__":
        unittest.main()