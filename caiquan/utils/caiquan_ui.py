# -*- coding:utf-8 -*-

from Tkinter import *
import caiquan_prepare
import os

class Caiquan_ui(object):
    # 是否为新游戏 默认为True
    _new_game = True
    # 一个字典映射
    _num2word = {'2': '剪刀', '5': '布', '0': '石头'}

    def __init__(self):
        self.cp = caiquan_prepare.Caiquan_prepare()
        self._caiquan_conf_ui_build()
        self.user_name = ''

    # 配置界面
    def _caiquan_conf_ui_build(self):
        '''
        创建配置界面供用户输入相关配置信息
        :return: nothing
        '''
        # 用于指示进度 0为刚开始 1为输入机器人个数阶段
        self._index = 0
        self._top = Tk()
        self._top.title('Python caiquan!')
        self._top.geometry('350x150')

        # 提示文本
        self._intro_text = Label(self._top, text='请输入您的用户名')
        self._intro_text.pack()

        # 输入框
        self._var = StringVar()
        Entry(self._top, textvariable=self._var).pack()

        # 按钮
        Button(self._top, text='confirm', command=self._confirm_button_press).pack()

        self._top.mainloop()

    # 游戏界面
    def _caiquan_play_ui_build(self, _new_game=True):
        '''
        创建游戏窗口相关组件并配置
        :param _new_game: bool 是否为新游戏 默认为True
        :return: nothing
        '''

        self._index = 1
        # 新游戏 or 读档
        if not _new_game:
            self._new_game = False

        # 确保之前的窗口都已销毁
        try:
            self._root.destroy()
            self._top.destroy()
        except:
            pass

        # 窗口信息
        self._game_top = Tk()
        self._game_top.title('Python caiquan!')

        # 提示文本
        self._game_intro_text = Label(self._game_top, text='请做出选择：')
        self._game_intro_text.pack()

        # 三个选择按钮
        self.button_jiandao = Button(self._game_top, text='剪刀', \
                                     command=lambda :self.caiquan_judge('jiandao')).pack()
        self.button_shitou = Button(self._game_top, text='石头', \
                                    command=lambda: self.caiquan_judge('shitou')).pack()
        self.button_bu = Button(self._game_top, text='布', \
                                command=lambda: self.caiquan_judge('bu')).pack()
        self.button_save = Button(self._game_top, text='保存', \
                                  command=lambda: self.caiquan_judge('save')).pack()

        # 开始新游戏
        self._game_top.mainloop()

    # 按钮监听，调用caiquan_prepare模块 开始游戏
    def caiquan_judge(self, _flag):
        '''
        根据按钮种类的不同进行参数选择来控制游戏
        :param _flag: str，用于标识按钮类型
        :return: nothing
        '''

        if _flag == 'jiandao':
            # 一个输入，然后获得结果 有下一轮直接改label 没有下一轮进行弹窗
            # 返回值需要考虑一下
            self._cq_result_judge(self.cp.play_game(self._new_game, '2'))
            # self._intro_text['text'] = ''
        elif _flag == 'shitou':
            self._cq_result_judge(self.cp.play_game(self._new_game, '0'))
        elif _flag == 'bu':
            self._cq_result_judge(self.cp.play_game(self._new_game, '5'))
        elif _flag == 'save':
            self._cq_result_judge(self.cp.play_game(self._new_game, 's'))
        else:
            pass # default

        # 最多执行一次非新游戏
        self._new_game = True

    # 处理caiquan_prepare过来的反馈
    def _cq_result_judge(self, _result):
        '''
            :param _result: {'', ()} or ([])
            :return: nothing
        '''

        # 有最终结果
        if isinstance(_result, dict):
            if _result.has_key('save'):
                self._tanchuang('保存成功！下次再见！')
                self._game_top.destroy()
            elif _result.has_key('failed'):
                for i in _result.get('failed')[1]:
                    if self._user_name in (i[0], i[2]):
                        self._tanchuang('{} : {} vs {} : {} , YOU LOSE!'\
                                        .format(i[0], self._num2word.get(i[1]), i[2], \
                                                self._num2word.get(i[3])))
                        break
                self._end_game()
                self._game_top.destroy()
            elif _result.has_key('win'):
                for i in _result.get('win')[1]:
                    if self._user_name in (i[0], i[2]):
                        self._tanchuang('{} : {} vs {} : {} , YOU WIN!'\
                                        .format(i[0], self._num2word.get(i[1]), i[2], \
                                                self._num2word.get(i[3])))
                        break
                self._end_game()
                self._game_top.destroy()
            elif _result.has_key('save_failed'):
                self._tanchuang('保存失败！')
                self._end_game()
            elif _result.has_key('save_done'):
                self._tanchuang('保存成功')
                self._game_top.destroy()

        # 还没有结果，大部分判定
        elif isinstance(_result, tuple):
            if _result[2]:
                self._tanchuang('平局！请重新输入！')
                self._game_intro_text['text'] = self._show_result(_result, True)
            else:
                self._tanchuang('这一轮是你赢了！')
                self._game_intro_text['text'] = self._show_result(_result)

    # 展示结果
    def _show_result(self, _result, _player_pingshou=False):
        '''
            :param _result: [remain_name_list, game_result_list]
            :param _pingshou: 该轮是否发生玩家与电脑平手的情况，bool
            :return: 显示到label上的str内容
        '''

        if _player_pingshou:
            return '请继续选择：'
        else:
            _remain_name = list()
            # 本轮剩余选手
            for i in list(_result[0]):
                _remain_name.append(i)

            _battle_result = ''
            # 本轮比赛结果
            for i in list(_result[1]):
                if str(i[4]) == '-1':
                    _battle_result += '{}: {} vs {}: {}, 平手.\n'\
                        .format(i[0], self._num2word.get(i[1]), \
                                i[2], self._num2word.get(i[3]))
                else:
                    _battle_result += '{}: {} vs {}: {}, {} 胜.\n'\
                        .format(i[0], self._num2word.get(i[1]), \
                                i[2], self._num2word.get(i[3]), i[4])

            _battle_result += '剩余对手名单：{}'.format(_remain_name)
            return _battle_result

    # 按钮监听
    def _confirm_button_press(self):
        '''
            用于对用户输入的鉴定，调用caiquan_prepare中的鉴定函数。鉴定结果通过更新UI反馈，不进行返回。
            :return: nothing
        '''

        # 用户名鉴定
        if self._index == 0:
            _user_name = self._var.get()
            if self.cp.name_define_and_verify(_user_name):
                self._user_name = _user_name
                self._intro_text['text'] = '请输入机器人个数'
                if self.cp.game_type_judge(_user_name):
                    self._tanchuang('检测到存档，是否继续？', 2)

                self._index += 1
                self._var.set('')
            else:
                self._tanchuang('您的输入有误，请重新输入。')

        # 机器人鉴定
        elif self._index == 1:
            _num_of_robot = self._var.get()
            if self.cp.robot_num_judge(_num_of_robot) and self._index == 1:
                # 配置结束 进入比赛页面
                self._top.destroy()
                self._caiquan_play_ui_build(True)
            else:
                self._tanchuang('您的输入有误，请重新输入。')

    # 弹窗用
    def _tanchuang(self, label_content, button_num=1):
        '''
            :param label_content: 弹窗的主内容
            :param button_num: 按钮数，默认为1，如果让用户选择则为2
            :return: nothing，直接显示对话框
        '''

        self._root = Tk()
        self._root.title('Notice')
        _label_tanchuang = Label(self._root, text=label_content)
        _label_tanchuang.pack()

        # 只有一个按钮的情况
        if button_num == 1:
            _button_tanchuang = Button(self._root, text="好的", command=self._root.quit)
            _button_tanchuang.pack()

        # 需要用户确认的情况
        else:
            _button_tanchuang1 = \
                Button(self._root, text="好的", command=lambda: self._caiquan_play_ui_build(False) \
                                                              and self._root.quit)
            _button_tanchuang1.pack()

            _button_tanchuang2 = \
                Button(self._root, text="算了", command=self._root.quit)
            _button_tanchuang2.pack()

        self._root.mainloop()
        # 确保在其他条件下窗口正常销毁
        try:
            self._root.destroy()
        except:
            pass

    # 善后
    def _end_game(self):
        # 删掉存档
        if os.path.exists('savefile_' + str(self._user_name)):
            os.remove('savefile_' + str(self._user_name))
