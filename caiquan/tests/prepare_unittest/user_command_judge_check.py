# -*- coding:utf-8 -*-
import sys
sys.path.append("..\..")
from utils import caiquan_prepare
import unittest
import os
#########这个模块更改了，未使用此用例集


class Test_user_command_judge_check(unittest.TestCase):

    def setUp(self):
        print 'Testcases_user_command start'
        self.cp = caiquan_prepare.Caiquan_prepare()
        self.command = []

    def tearDown(self):
        print 'Testcases_user_command over\n'

    def command_judge_check1(self):
        self.command.append('q')
        self.cp.user_command_judge(self.command,'Tom')
        result = os.path.exists('savefile_Tom')
        self.assertFalse(result, msg = 'Failed')
        print self.command

    def command_judge_check2(self):
        self.command.append('sq')
        self.cp.user_command_judge(self.command, 'Tom')
        result = os.path.exists('savefile_Tom')
        self.assertTrue(result, msg = 'Failed')
        print self.command

    def command_judge_check3(self):
        self.command.append('aksjdkqjwei')
        self.cp.user_command_judge(self.command, 'Tommy')
        result = os.path.exists('savefile_Tommy')
        self.assertFalse(result, msg='Failed')
        print self.command

    if __name__ == '__main__':
        unittest.main()