import unittest
import name_define_check
import user_command_judge_check
import clear_file_and_quit_check
import game_type_check
import name_before_game_check
import play_game_check
import robot_num_judge_check
import result_print_check

suite = unittest.TestSuite()

#name_define
suite.addTest(name_define_check.Test_name_define("name_define_check1"))
suite.addTest(name_define_check.Test_name_define("name_define_check2"))
suite.addTest(name_define_check.Test_name_define("name_define_check3"))

#command_judge
# suite.addTest(user_command_judge_check.Test_user_command_judge_check("command_judge_check1"))
# suite.addTest(user_command_judge_check.Test_user_command_judge_check("command_judge_check2"))
# suite.addTest(user_command_judge_check.Test_user_command_judge_check("command_judge_check3"))

#clear_file_and_quit
suite.addTest(clear_file_and_quit_check.Test_clear_file_and_quit("clear_file_and_quit_check1"))

#game_type
suite.addTest(game_type_check.Test_game_type("game_type_check1"))
suite.addTest(game_type_check.Test_game_type("game_type_check2"))

#name_before_game
suite.addTest(name_before_game_check.Test_name_before_game("name_before_game_check1"))
suite.addTest(name_before_game_check.Test_name_before_game("name_before_game_check2"))
suite.addTest(name_before_game_check.Test_name_before_game("name_before_game_check3"))

#result_print
# suite.addTest(result_print_check.Test_result_print("result_print_check1"))
# suite.addTest(result_print_check.Test_result_print("result_print_check2"))
# suite.addTest(result_print_check.Test_result_print("result_print_check3"))

#robot_num_judge
suite.addTest(robot_num_judge_check.Test_robot_num_judge("robot_num_judge_check1"))
suite.addTest(robot_num_judge_check.Test_robot_num_judge("robot_num_judge_check2"))
suite.addTest(robot_num_judge_check.Test_robot_num_judge("robot_num_judge_check3"))
suite.addTest(robot_num_judge_check.Test_robot_num_judge("robot_num_judge_check4"))
suite.addTest(robot_num_judge_check.Test_robot_num_judge("robot_num_judge_check5"))
suite.addTest(robot_num_judge_check.Test_robot_num_judge("robot_num_judge_check6"))

# #play_game
suite.addTest(play_game_check.Test_play_game("play_game_check1"))
suite.addTest(play_game_check.Test_play_game("play_game_check2"))
suite.addTest(play_game_check.Test_play_game("play_game_check3"))
suite.addTest(play_game_check.Test_play_game("play_game_check4"))
suite.addTest(play_game_check.Test_play_game("play_game_check5"))
suite.addTest(play_game_check.Test_play_game("play_game_check6"))
suite.addTest(play_game_check.Test_play_game("play_game_check7"))
suite.addTest(play_game_check.Test_play_game("play_game_check8"))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)