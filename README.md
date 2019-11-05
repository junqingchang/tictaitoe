# tic-tAI-toe
Tic-Tac-Toe environment for Reinforcement learning. Written similarly to how OpenAI gym environment works

## Built on
* Python 3.7.4 (Should work for any python3)

## Sample Render
```
Enter move: [0, 1, 2, 3, 4, 5, 6, 7, 8]
6
Winner: Player 1
-------
|O|X|O|
-------
|X|O|X|
-------
|O| | |
-------
```
## Usage
The usage is very similar to how you would use a gym environment
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
## Reward Method
* -5 for trying to make a move on a spot already taken
* -1 for each turn the game does not complete
* 10 when game completes (Probably need your own code to determine + or - depending on if they won)

## More work
* Train an AI to play the game with people, so we will be less sad
* Change render to external visualisation