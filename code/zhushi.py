def main(stdscr):
    def init():
        #重置游戏棋盘
        # game_field.reset()
        return 'Game'

    def not_game(state):

        #画出GameOver 或者 Win 的界面
        # game_field.draw(stdscr)
        # # 读取用户输入得到action，判断是重启游戏还是结束游戏
        # action = get_user_action(stdscr)
        # responses = defaultdict(lambda: state)
        # responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        # return responses[action]
        return 0

    def game():
        #画出当前棋盘状态
        # game_field.draw(stdscr)
        # action = get_user_action(stdscr)
        #
        # if action == "Restart":
        #     return 'Init'
        # if action == 'Exit':
        #     return 'Exit'
        # if game_field.move(action):
        #     if game_field.move(action):
        #         return 'Win'
        #     if game_field.is_gameover():
        #         return 'Gameover'

        return 'Game'

"""
duohangzhushi
"""

# danhangzhushi