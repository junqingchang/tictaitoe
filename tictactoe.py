class TicTacToe(object):
    def __init__(self):
        self.reset()

    def step(self, action):
        self.board[action] = self.turn
        self.change_player()
        self.action_space.remove(action)
        done, winner = self.game_complete()
        if not done:
            reward = -1
        else:
            reward = 10
            if winner == -1:
                print('Draw')
            else:
                print(f'Winner: Player {winner+1}')
        return self.board, reward, done

    def change_player(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def game_complete(self):
        if self.board[0] != -1:
            if (self.board[0] == self.board[1] and self.board[0] == self.board[2]) or (self.board[0] == self.board[3] and self.board[0] == self.board[6]) or (self.board[0] == self.board[4] and self.board[0] == self.board[8]):
                return True, self.board[0]
        if self.board[1] != -1:
            if (self.board[1] == self.board[4] and self.board[1] == self.board[7]):
                return True, self.board[1]
        if self.board[2] != -1:
            if (self.board[2] == self.board[5] and self.board[2] == self.board[8]):
                return True, self.board[2]
        if self.board[3] != -1:
            if (self.board[3] == self.board[4] and self.board[3] == self.board[5]):
                return True, self.board[3]
        if self.board[6] != -1:
            if (self.board[6] == self.board[7] and self.board[6] == self.board[8]) or (self.board[6] == self.board[4] and self.board[6] == self.board[2]):
                return True, self.board[6]
        if len(self.action_space) == 0:
            return True, -1
        else:
            return False, -1

    def reset(self):
        self.board = [-1] * 9
        self.turn = 0
        self.action_space = [x for x in range(0,9)]

    def render(self):
        board = '-------\n|'
        for i in range(len(self.board)):
            if self.board[i] == -1:
                board += ' |'
            elif self.board[i] == 0:
                board += 'O|'
            else:
                board += 'X|'
            if (i+1)%3 == 0:
                board += '\n-------\n|'
        print(board[:-1])

    def play(self):
        done = False
        while not done:
            valid_input = False
            while not valid_input:
                action = int(input(f'Enter move: {self.action_space}\n'))
                if action in self.action_space:
                    valid_input = True
                    _, _, done = self.step(action)
                    self.render()
                else:
                    print('Invalid Move')