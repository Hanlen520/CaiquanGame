# -*- coding:utf-8 -*-
import os
import sys
import caiquan_rule
import random

class Caiquan_prepare(object):
    def __init__(self):
        self._user_name = ''
        self._robot_num = 0
        self.cr = caiquan_rule.CaiquanRule()
        with open('names.txt', 'r') as file:
            self.robot_names = str(file.read()).split('\n')
        self.remain_list = []

    # 用户昵称合法性检测
    def name_define_and_verify(self, _name):
        if not _name.replace(' ', ''):
            return False
        elif len(_name) <=20:
            # 通过的话需要把用户名存起来
            self._user_name = _name
            return True
        else:
            return False

    # 有没有存档
    def game_type_judge(self,name):
        _file_name = 'savefile_' + name

        # 有存档
        if os.path.exists(_file_name):
            return True
        # 没存档 直接新游戏
        else:
            return False

    # 进行游戏 并返回结果 被ui调用 调用caiquan_rule
    def play_game(self, _flag, _user_choice):
        # 用户是否打算退出
        if _user_choice == 's':
            with open('savefile_' + str(self._user_name), 'w') as file:
                file.write(str(self.remain_list))
                return {'save_done': ''}

        # 读档
        if not _flag:
            with open('savefile_' + str(self._user_name)) as file:
                # 如果平局 剩余名字是比赛前的原序列
                remain_list, game_list, _pingju_flag = \
                    self.cr.black_box(self._user_name, eval(str(file.read())), _user_choice)

                if self._user_name not in remain_list:
                    self.clear_file_and_quit(self._user_name, True)
                    return {'failed': (remain_list, game_list, _pingju_flag)}
                elif len(remain_list) == 1:
                    self.clear_file_and_quit(self._user_name, True)
                    return {'win': (remain_list, game_list, _pingju_flag)}
                else:
                    self.remain_list = remain_list
                    return (remain_list, game_list, _pingju_flag)

        # 新开始
        else:
            remain_list, game_list, _pingju_flag = \
                self.cr.black_box(self._user_name, self.remain_list, _user_choice)

            if self._user_name not in remain_list:
                self.clear_file_and_quit(self._user_name, True)
                return {'failed': (remain_list, game_list, _pingju_flag)}
            elif len(remain_list) == 1:
                return {'win': (remain_list, game_list, _pingju_flag)}

            self.remain_list = remain_list
            return (remain_list, game_list, _pingju_flag)

    # 机器人个数的合理性判断
    def robot_num_judge(self, _num):
        if _num.isdigit() and int(_num) > 0 and int(_num) <= 50:
            # 通过的话需要把机器人个数存起来
            self._robot_num = _num
            self.remain_list = self.name_before_game(_num, self._user_name)
            return True
        else:
            return False

    # 生成对应数目的参赛人员名字列表
    def name_before_game(self, _num, username):
        robot_names = self.robot_names
        # 防止用户名与机器人名重复
        if username in robot_names:
            robot_names.remove(username)
        return random.sample(list(robot_names), int(_num))


    # 程序退出与存档文件清理 for system exit
    def clear_file_and_quit(self, file_name, quit_flag=True):
        sys.path.append('..')
        if os.path.exists(file_name):
            os.remove(file_name)
            self._robot_num = 0
            self._user_name = ''
        if quit_flag:
            print 'successful quit! bye'
            # sys.exit(0)
