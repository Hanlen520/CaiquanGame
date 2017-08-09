# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os

class Test_result_print(unittest.TestCase):

    def setUp(self):
        print 'Testcases_result_print start'
        self.cp = caiquan_prepare.Caiquan_prepare()

    def tearDown(self):
        print 'Testcases_result_print over\n'

    def result_print_check1(self):
        '''
        第一局比赛结果打印
        :return:
        '''
        print 'check1'
        name_list = self.cp.name_before_game(8,'Tom')
        result_list = [('Tom',5),('Jerry',0),'winner is Jerry']

        self.cp.result_print(name_list, result_list, 'Tom')

    def result_print_check2(self):
        '''
        继续比赛的结果打印
        :return:
        '''
        print 'check2'
        name_list = ['Tom','Bob','jack']
        result_list = [('Tom', 5), ('Jerry', 0), 'winner is Jerry']

        self.cp.result_print(name_list, result_list, 'Tom')

    def result_print_check3(self):
        '''
        总冠军结果打印
        :return:
        '''
        print 'check3'
        name_list = ['Tom']
        result_list = [('Tom',2),('Jerry',5),'winner is Tom']

        self.cp.result_print(name_list,result_list, 'Tom')

    if __name__ == "__main__":
        unittest.main()