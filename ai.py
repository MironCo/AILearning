import os
import torch
from torch import nn
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor, Lambda, PILToTensor

device = (
    "cuda"
    if torch.cuda.is_available()
    #else "mps"
    #if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 530),
            nn.ReLU(), 
            nn.Linear(530, 10),
        )
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    
model = NeuralNetwork().to(device)

if (os.path.exists("./model_weights.pth")):
    model.load_state_dict(torch.load('model_weights.pth'))

def predict_image_server(numpy_array):
    return predict_image(array=numpy_array, model=model)

# Function to predict the number in a specific image
def predict_image(array, model):
    #transform = PILToTensor()
    numpy_array = np.array(array, dtype=np.float32).reshape(1, 1, 28, 28)
    image_tensor = torch.from_numpy(numpy_array).to(device)

    model.eval()
    with torch.no_grad():

        image_tensor = image_tensor.to(device)
        output = model(image_tensor)
        predicted = output.argmax(1)
        print(f"Predicted label: {predicted.item()}")
        return predicted.item()
