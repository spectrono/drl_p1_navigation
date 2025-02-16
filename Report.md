# Report on DQN implementation

## Description of the algorithm

The implemented algorithm is an extension of the Q-Learning algorithm and extends it via deep neural networks to approximate the Q-Value function. This gives the agent the ability to learn high-dimensional and continuous state spaces. The original paper which introduced Deep Q-Learning is called *Playing Atari with Deep Reinforcement Learning* [Link](https://arxiv.org/abs/1312.5602).

Some highlights:

- *Deep neural networks* to approximate the Q-Value function
- *Experience Replay* is used to collect experiences during training and replay them for adapting the underlying weights of the neural net. This helps to break the correlation between consecutive samples.
- "Soft Update" to train the agent while maintaining a local and a target network. The local network is constantly updated via the experiences from the replay buffer. The target network is a copy of that local network but is less frequently updated. This way, the Q-Value updates are less correlated with the current Q-value estimate, which stabilizes the training and makes it more likeley to converge.

The implementation is given in the file *dqn_agent.py* alongside detailed comments on the code. The agent and its environment is controlled via the provided *navigation.ipynb* jupyter notebook.

## Chosen hyperparameters

To control the RL-agent several hyper parameter had to be choosen. First of all:

- the maximum number of pisodes was set to: n_episodes=1800
- and the maximum length of each episode was set to: max_t=1600

The epsilon greedy strategy was controlled by:

- an initial value of epsilon: eps_start=1.0
- a minimum value of epsilon: eps_end=0.005
- and an epsilin decay factor: eps_decay=0.997

These parameters are set in the jupyter notebook *navigation.ipynb* in the function:

*def dqn(env, agent, n_episodes=1800, max_t=1600, eps_start=1.0, eps_end=0.005, eps_decay=0.997):*

The remaining hyperparameter are set at the beginning of the *dqn_agent.py* file:

- The experience replay buffer size: BUFFER_SIZE = int(1e5)
- The minibatch size which controls when enough samples are available in memory for doing a learning step: BATCH_SIZE = 128
- The discount factor for new reward: GAMMA = 0.98
- Fraction on how much the local and target networks are mixed during a soft update step: TAU = 1e-3
- The learning rate:  LR = 5e-4
- How often the network should be updated (measured in steps of an episode): UPDATE_EVERY = 5

## Architecture of the neural network

The selected architecture consists of four fully connected layers:

- Input layer of size 37 which represents the state space
- First hidden layer with 128 neurons and ReLU activation function
- Second hidden layer with 64 neurons and ReLU activation function
- Third hidden layer with 16 neurons and ReLU activation function
- Output layer with a size of 4 to represent the action space

This realizes a mapping from state to Q-values for the possible actions. The implementaion of the neural network is given in *dqn_model.py* again with detailed comments in the code.

## Results

The environment was solved by the implmenemted algorithm after 962 episodes reaching an average Score of 15.00.

### Plot of Rewards

The below plot shows the performance of the algorithm:

![Plot of rewards](convergence_rate_15.png)

Remark: Consider the environment as solved if the agent reaches at least a score of 13.

### Example video from the training phase

The video shows how the agent selects actions during training:

[LearningAgent](./Agent_evaluation_recording_2025-02-12 23-01-56.mkv)

### Example video of trained agent acting in the banana environment

Watch the video below to see the fully trained agent:

[TrainedAgend](./Agent_training_recording_2025-02-12 22-24-00.mkv)

## Ideas for Future Work

As pointed out in the *Rainbow: Combining Improvements in Deep Reinforcement Learning* [Paper](https://arxiv.org/abs/1710.02298), there are several improvements already available. These are e.g.:

- Double DQN (DDQN)
- Prioritized experience replay
- Dueling DQN
- Learning from multi-step bootstrap targets(opens in a new tab)
- Distributional DQN(opens in a new tab)
- Noisy DQN

A good start would probably be adding *Prioritized experience replay* because it only demands minimal changes of the current implementation and as stated in the *Rainbow* paper will provide better performance than the vanilla DQN algorithm.
