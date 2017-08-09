# -*- coding:utf-8 -*-

import random


class CaiquanRule(object):
    """
    比赛和一些函数
    """

    def __init__(self):
        self._pingju_flag = False
        self._user_name = ''



    # # 暂时这样子，待交互界面时更改
    # def user_input_choice(self, username, _user_choice):
    #     return _user_choice()

    # 机器产生石头剪子布
    def input_choice(self, user_name, name, _user_choice):
        if user_name == name:
            return [user_name, _user_choice]
        else:
            com_current_choice = random.choice(('5', '2', '0'))
            return [name, com_current_choice]

    # 比赛，确定获胜名单和输出list
    def caiquan_compare(self, first_choice, second_choice):

        if (first_choice[1], second_choice[1]) in (('2', '5'), ('0', '2'), ('5', '0')):
            return first_choice[0]
            # emp1=(list_choice[i][0],list_choice[i][1],list_choice[i+1][0],list_choice[i+1][1])
        elif (first_choice[1], second_choice[1]) in (('5', '2'), ('2', '0'), ('0', '5')):
            return second_choice[0]
        elif first_choice[1] == second_choice[1]:
            return None

    # 开始比赛的黑盒子
    def caiquan_result(self, user_name, name_list, _user_choice):
        if user_name not in name_list:
            name_list.append(user_name)
        random.shuffle(name_list)
        i = 0
        remain_list = []
        game_list = []
        while i < len(name_list) - 1:
            # 最初的猜测。
            temp1 = self.input_choice(user_name, name_list[i], _user_choice)
            temp2 = self.input_choice(user_name, name_list[i + 1], _user_choice)
            # 比赛循环是平局。
            temp_result = self.caiquan_compare(temp1, temp2)

            # 玩家平局
            if (not temp_result) and (user_name in (name_list[i], name_list[i+1])):
                self._pingju_flag = True
                continue

            while not temp_result:
                temp_list = temp1 + temp2
                temp_list.append(-1)
                game_list.append(temp_list)
                temp1 = self.input_choice(user_name, name_list[i], _user_choice)
                temp2 = self.input_choice(user_name, name_list[i + 1], _user_choice)
                temp_result = self.caiquan_compare(temp1, temp2)

                # 比赛不是平局
            if temp_result:
                remain_list.append(temp_result)
                temp_list = temp1 + temp2
                temp_list.append(temp_result)
                game_list.append(temp_list)

            i += 2
        if len(name_list) % 2 == 0:
            pass
        else:
            remain_list.append(name_list[i])
        return remain_list, game_list

    # 黑盒，方便调用
    def black_box(self, user_name, name_list, _user_choice):
        self._user_name = user_name
        x1, x2 = self.caiquan_result(user_name, name_list, _user_choice)

        if self._pingju_flag:
            self._pingju_flag = False

            return (name_list, x2, not self._pingju_flag)
        else:
            return (x1, x2, self._pingju_flag)

    # 输出比赛结果的函数
    def show_game_result(self, user_name, name_list, _user_choice):
        w1, game_list = self.caiquan_result(user_name, name_list, _user_choice)
        for i in range(0, len(game_list)):
            # 如果是平局
            if game_list[i][4] == 0:
                print('Player %s chooses %s,Player %s chooses %s,equal game.  \n' % (
                game_list[i][0], game_list[i][1], game_list[i][2], game_list[i][3]))
            else:
                print('Player %s chooses %s,Player %s chooses %s,%s wins. ' % (
                game_list[i][0], game_list[i][1], game_list[i][2], game_list[i][3], game_list[i][4]))
