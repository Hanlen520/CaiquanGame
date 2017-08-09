# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os

class Test_robot_num_judge(unittest.TestCase):

    def setUp(self):
        print 'Testcases_robot_num start'
        self.cp = caiquan_prepare.Caiquan_prepare()

    def tearDown(self):
        print 'Testcases_robot_num over\n'

    def robot_num_judge_check1(self):
        '''
        边界值判断
        :return:
        '''
        print 'check1'
        result = self.cp.robot_num_judge('0')
        self.assertFalse(result, msg="robot_num_judge_check1_Failed")

    def robot_num_judge_check2(self):
        '''
        边界值判断
        :return:
        '''
        print 'check2'
        result = self.cp.robot_num_judge('100')
        self.assertFalse(result, msg="robot_num_judge_check2_Failed")
        print result

    def robot_num_judge_check3(self):
        '''
        边界值判断
        :return:
        '''
        print 'check3'
        result = self.cp.robot_num_judge('99.9')
        self.assertFalse(result, msg="robot_num_judge_check3_Failed")
        print result

    def robot_num_judge_check4(self):
        '''
        边界值判断
        :return:
        '''
        print 'check4'
        result = self.cp.robot_num_judge('0.1')
        self.assertFalse(result, msg="robot_num_judge_check4_Failed")
        print result

    def robot_num_judge_check5(self):
        '''
        无效等价类
        :return:
        '''
        print 'check5'
        result = self.cp.robot_num_judge('1E')
        self.assertFalse(result, msg="robot_num_judge_check4_Failed")
        print result



    def robot_num_judge_check6(self):
        '''
        有效等价类
        :return:
        '''
        print 'check6'
        result = self.cp.robot_num_judge('40')
        self.assertTrue(result, msg="robot_num_judge_check5_Failed")
        print result

    if __name__ == "__main__":
        unittest.main()