# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os

class Test_game_type(unittest.TestCase):

    def setUp(self):
        print 'Testcases_game_type start'
        self.cp = caiquan_prepare.Caiquan_prepare()

    def tearDown(self):
        print 'Testcases_game_type over\n'

    def game_type_check1(self):
        '''
        测试读档
        :return:
        '''
        print 'check1'
        open('savefile_Tom', 'w')
        self.assertTrue(self.cp.game_type_judge('Tom'), msg="game_type_check1_Failed")
        print 'load'

    def game_type_check2(self):
        '''
        测试新游戏
        :return:
        '''
        print 'check2'
        self.cp.clear_file_and_quit('savefile_Tom')
        self.assertFalse(self.cp.game_type_judge('Tom'), msg="game_type_check2_Failed")
        print 'new game'

    if __name__ == '__main__':
        unittest.main()