import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetworkAlpha(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, hidden_layer_1=128, hidden_layer_2=64, hidden_layer_3=16):
        """Initialize parameters and build model.

        The architecture consists of 4 fully connected (dense) layers with ReLU activation functions for the first three layers.
        state_size and action_size can individually be controlled by the RL-agent. 
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetworkAlpha, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, hidden_layer_1)
        self.fc2 = nn.Linear(hidden_layer_1, hidden_layer_2)
        self.fc3 = nn.Linear(hidden_layer_2, hidden_layer_3)
        self.fc4 = nn.Linear(hidden_layer_3, action_size)
        
    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        
        return self.fc4(x)
