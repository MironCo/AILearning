#!/bin/bash

echo "🚀 Starting AI Digit Recognition App..."

# Start the server with Docker
echo "📦 Building and starting server with Docker..."
docker-compose up --build -d

# Wait a moment for server to start
sleep 3

# Start the client
echo "🎨 Starting Svelte client..."
cd client && npm run dev