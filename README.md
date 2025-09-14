# AI Digit Recognition

A full-stack digit recognition application using PyTorch and Svelte. Draw digits on a 28x28 canvas and watch the neural network try to guess what you drew!

## Features

- **Interactive Canvas**: Draw digits with your mouse
- **Real-time Predictions**: Neural network processes drawings instantly
- **Docker Containerized**: Easy setup and deployment
- **MNIST-trained Model**: Uses a simple feedforward neural network

## Tech Stack

- **Backend**: Python, Flask, PyTorch
- **Frontend**: Svelte, Vite
- **Deployment**: Docker, Docker Compose

## Quick Start

```bash
# Start everything
./start.sh
```

That's it! The script will:
1. Build and start the Python server in Docker (port 8000)
2. Start the Svelte development server (port 5173)

Open `http://localhost:5173` and start drawing!

## Manual Setup

If you prefer to run things manually:

```bash
# Start server
docker-compose up --build

# In another terminal, start client
cd client && npm install && npm run dev
```

## How It Works

1. **Draw**: Use the canvas to draw digits (28x28 pixels)
2. **Process**: Canvas data is sent to Flask backend
3. **Predict**: PyTorch model processes the image
4. **Display**: Prediction is shown in real-time

## Model Details

- Simple feedforward neural network
- Input: 28x28 grayscale images
- Architecture: 784 → 530 → 10 neurons
- Trained on MNIST dataset
- Achieves decent accuracy on clean, centered digits

## Project Structure
```
├── server/           # Python backend
│   ├── ai.py        # Neural network model
│   ├── server.py    # Flask API
│   ├── imagecreator.py # Image preprocessing
│   └── requirements.txt
├── client/          # Svelte frontend
│   └── src/         # Source code
├── docker-compose.yml
└── start.sh         # Quick start script
```