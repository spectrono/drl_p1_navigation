# Learning Algorithm

## Description of the algorithm

The implemented algorithm is an extension of the Q-Learning algorithm and extends it via deep neural networks to approximate the Q-Value function. This gives the agent the ability to learn high-dimensional and continuous state spaces. The original paper which introduced Deep Q-Learning is called *Playing Atari with Deep Reinforcement Learning* [Link](https://arxiv.org/abs/1312.5602).

Some highlights:

- *Deep neural networks* to approximate the Q-Value function
- *Experience Replay* is used to collect experiences during training and replay them for adapting the underlying weights of the neural net. This helps to break the correlation between consecutive samples.
- "Soft Update" to train the agent while maintaining a local and a target network. The local network is constantly updated via the experiences from the replay buffer. The target network is a copy of that local framework but is less frequently updated. This way, the Q-Value updates are less correlated with the current Q-value estimate, which stabilized the training and makes it more likeley to correlate.

## Chosen hyperparameters

## Architecture of the neural network

## Results

Report the number of episodes needed to solve the environment

### Plot of Rewards

A plot of rewards per episode to illustrate that the agent is able to receive an average reward (over 100 episodes) of at least +13

### Example video during training

### Example video of trained agent in the banana environment

## Ideas for Future Work

Concrete future ideas for improving the agent's performance
