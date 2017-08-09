# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os

class Test_play_game(unittest.TestCase):

    def setUp(self):
        print 'Testcases_play_game start'
        self.cp = caiquan_prepare.Caiquan_prepare()
        self.username = 'Tom'
        self.remain_list = []

    def tearDown(self):
        print 'Testcases_play_games over\n'

    def play_game_check1(self):
        '''
        测试保存
        :return:
        '''
        print 'check1'
        _user_choice = 's'
        _flag = True
        self.remain_list.append(self.username)
        result = self.cp.play_game(_flag, _user_choice)
        print result
        self.assertEqual(result, {'save_done': ''}, msg='play_game_check1_Failed')

    def play_game_check2(self):
        '''
        根据白盒，调换输入顺序，测试保存
        :return:
        '''
        print 'check2'
        _flag = True
        _user_choice = 's'
        self.remain_list.append(self.username)
        result = self.cp.play_game(_flag, _user_choice)
        print result
        self.assertEqual(result, {'save_done': ''}, msg='play_game_check2_Failed')

    def play_game_check3(self):
        '''
        测试读档后的继续游戏
        :return:
        '''
        print 'check3'
        self.remain_list.append('Tom')
        self.remain_list.append('Jerry')
        _flag = True
        _user_choice = '2'
        print self.cp.play_game(_flag, _user_choice)

    def play_game_check4(self):
        '''
        测试读档后的胜利
        :return:
        '''
        print 'check4'
        self.remain_list.append('Tom')
        _flag = True
        _user_choice = '2'
        print self.cp.play_game(_flag, _user_choice)

    def play_game_check5(self):
        '''
        测试读档后的失败
        :return:
        '''
        print 'check5'
        self.remain_list.append('Jerry')
        _flag = True
        _user_choice = '2'
        print self.cp.play_game(_flag, _user_choice)

    def play_game_check6(self):
        '''
        测试新游戏的继续游戏
        :return:
        '''
        print 'check6'
        self.remain_list.append('Tom')
        self.remain_list.append('Jerry')
        _flag = False
        _user_choice = '22'
        print self.cp.play_game(_flag, _user_choice)

    def play_game_check7(self):
        '''
        测试新游戏的胜利
        :return:
        '''
        print 'check7'
        self.remain_list.append('Tom')
        _flag = False
        _user_choice = '22'
        print self.cp.play_game(_flag, _user_choice)

    def play_game_check8(self):
        '''
        测试新游戏的失败
        :return:
        '''
        print 'check8'
        self.remain_list.append('Jerry')
        _flag = False
        _user_choice = '22'
        print self.cp.play_game(_flag, _user_choice)

    if __name__ == '__main__':
        unittest.main()
