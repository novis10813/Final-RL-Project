'''Pytorch version comes from: https://github.com/yzheng51/rl-dino-run'''

import torch
import gym
import gym_chrome_dino
from gym_chrome_dino.utils.wrappers import make_dino
from torch_agents import DQN, DoubleDQN, DuelDQN, NoisyDQN, DQNPrioritized, RainbowDQN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialise the game
env = gym.make('ChromeDino-v0')
# env = gym.make('ChromeDinoNoBrowser-v0')
env = make_dino(env, timer=True, frame_stack=True)

# Get the number of actions and the dimension of input
n_actions = env.action_space.n

# ----------- Nature DQN ---------------
# dqn = DQN(n_actions, device)
# dqn.train(env)
# dqn.load("./trained/dqn.pkl")
# dqn.test(env)


# ----------- Double DQN ----------------
# double_dqn = DoubleDQN(n_actions, device)
# double_dqn.train(env, logger)
# double_dqn.load("./trained/double-dqn.pkl")
# double_dqn.test(env)


# ----------- Dueling DQN ----------------
# duel_dqn = DuelDQN(n_actions, device)
# duel_dqn.train(env, logger)
# duel_dqn.load("./trained/duel-dqn.pkl")
# duel_dqn.test(env)


# ----------- PER DQN ---------------
# per_dqn = DQNPrioritized(n_actions, device)
# per_dqn.train(env)
# per_dqn.load("./trained/dqn.pkl")
# per_dqn.test(env)


# ----------- Noisy DQN ----------------
# noisy_dqn = NoisyDQN(n_actions, device)
# noisy_dqn.train(env)
# noisy_dqn.load("G:/Code/Python/GitHub/Final-RL-Project/NoisyDQN_model.pkl")
# noisy_dqn.test(env)


# ----------- Noisy DQN ----------------
rainbow_dqn = RainbowDQN(n_actions, device)
rainbow_dqn.train(env)
# rainbow_dqn.load("G:/Code/Python/GitHub/Final-RL-Project/RainbowDQN_model.pkl")
# rainbow_dqn.test(env)


env.render(mode="rgb_array")
env.close()