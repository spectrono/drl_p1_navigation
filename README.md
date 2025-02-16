# DRL - Project 1: Navigation

Udacity Deep Reinforcement Learning - Navigation Project

## Project environment

The environment was provided py udacity. It's a modified version of the Unity Banana collector environment. It' e.g. used to train a reinforcement learning algorithm to navigate in an 3D environment to collect bananas.

### State space

The state space is continuos and has 37 dimensions. It's provided as an obervation vector.

### Action space

The action space is discrete, containing 4 actions:

- Turn left
- Turn right
- Move forward
- Move backward

### Solving the environment

The environment is considered to be solved when a mean reward of at least 13 was given over the last 100 episodes.

### Getting started

**Attention:** The provided code is only testet on Linux (Pop!_OS 22.04 LTS)

To make sure that the provided Navigation.ipynb can be used succesfully, the following python environment is needed:

- at least Python 3.9.21
- numpy
- pytorch
- matplotlib
- ipykernel
- jupyter

You can install these components by pip or conveniently via conda if e.g. you need to create an environment with a special python version.

Additionly, you need the *modified* Banana-Environment from Udacity provided here:

- Linux: <https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip>
- Windows 32-bit: <https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip>
- Windows 64-bit: <https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip>
- Mac: <https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip>

Place the zip file in the root folder of your cloned repo and unzip it. This should create a folder named "Banana_linux" (or similar if another OS is used).

### Instructions (Training the DRL-Agent)

- Open the notebook Navigation.ipynb
- Execute the cells step by step, starting from the top:
  1. The first cell will import the most of the external libs like pytorch, UnityEnvironment, numpy, etc.
  2. The next cell wil import the DRL-Agent in "dqn_agent.py" and the used network architecture "dqn_model.py" to learn the Q-Values.
     1. Hint: uncomment the importlib section if you modified one of the files and want to reload them!
  3. Now import the "Banana" environment and print some basic information about it.
  4. The next cell defined orchestrates the RL procedure. Using the provided parameters should should solve the environment in less then 1800 epochs. In my experience, the enviroment is solved at around 1000 steps with the provided parameter.
  5. The next cell initializes the RL-Agent
  6. Now start the training by executing cell number six.
     1. During training, every 100 epochs a intermediate result of the mean score of the last 100 epochs is printed out. Also, the current epsilon factor is given.
     2. The training will stop, when a score of at least 15 is reached or 1800 episodes are reached. Whatever happens first.
     3. When training is finished, the scores all epoches will be plotted and the network weights will be saved to disk.

### Instructions (Watching the trained agent collecting bananas)

Once, training is finished succesfully, you can restart your yupyter kenerl (at least I had to give the banana environment a fresh start after learning, otherwise the unity engine stoped working for me!). Then run the last cell. This will again import all necessary packages and the saved network weights to show live how the agent performs in it's environment.

### Further instructions

See the report.md file for details on inmplementation and results.
