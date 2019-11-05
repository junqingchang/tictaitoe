import random


class TicTacToe(object):
    '''
    Tic Tac Toe environment
    
    Usable Variables:
    self.board contains all the information on the board at the moment (-1 unplayed space, 0 move by player 1, 1 move by player 2)
    self.action_space contains all legal moves at the point of calling
    self.turn alternates between 0 and 1 indicating current player

    Usable functions:
    reset() to reset the board
    get_observation() to get current observation in the form [*board_info, player_turn]
    step(action) to advance environment in direction of action
    sample_action() gets a random move from action_space. Not recommended
    play() lets you play the game alone (if you have a sad life) or with a friend

    Usage example:
    ```
    env = TicTacToe()
    observation = env.reset()
    for _ in range(1000):
        env.render()
        action = env.sample_action()
        observation, reward, done, info = env.step(action)

        if done:
            observation = env.reset()
    
    ```
    '''
    def __init__(self):
        '''
        Calls reset to restart environment
        '''
        self.reset()

    def reset(self):
        '''
        Resets the environment and returns the initial observation, observation in the form [*board_info, player_turn]
        '''
        self.board = [-1] * 9
        self.turn = 0
        self.action_space = [x for x in range(0, 9)]
        return self.get_observation()

    def get_observation(self):
        '''
        Return observation in the form [*board_info, player_turn]
        '''
        return [*self.board, self.turn]

    def step(self, action, info=False):
        '''
        Advance environment by a step in the direction of action given
        Returns observation, reward, done, winner
        
        winner is in the form of -1, 0, 1 with -1 indicating no winner, 0 being player 1, 1 being player 2
        '''
        if self.board[action] != -1:
            reward = -5
            done, winner = self.game_complete()
            return self.get_observation(), reward, done, winner
        self.board[action] = self.turn
        self.change_player()
        done, winner = self.game_complete()
        if not done:
            reward = -1
        else:
            if winner == -1:
                reward = 0
                if info:
                    print('Draw')
            else:
                reward = 10
                if info:
                    print(f'Winner: Player {winner+1}')

        return self.get_observation(), reward, done, winner

    def sample_action(self):
        '''
        Randomly samples an action from the action space. Not recommended. Recommended to sample action_space as required (e.g. EPS Greedy)
        '''
        return random.choice(self.action_space)

    def change_player(self):
        '''
        Backend mechanism to swap turns
        '''
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def game_complete(self):
        '''
        Backend mechanism to check if game is completed and if it is, who won
        '''
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

    def render(self):
        '''
        Renders the board in print form. Not recommended on training as it will flood the console
        Looking to upgrade this to an external visualisation
        '''
        board = '-------\n|'
        for i in range(len(self.board)):
            if self.board[i] == -1:
                board += ' |'
            elif self.board[i] == 0:
                board += 'O|'
            else:
                board += 'X|'
            if (i+1) % 3 == 0:
                board += '\n-------\n|'
        print(board[:-1])

    def play(self):
        '''
        Player vs player mode, mostly to test if the works
        '''
        done = False
        while not done:
            valid_input = False
            while not valid_input:
                action = int(input(f'Enter move: {self.action_space}\n'))
                if action in self.action_space:
                    valid_input = True
                    _, _, done, _ = self.step(action, info=True)
                    self.render()
                else:
                    print('Invalid Move')
