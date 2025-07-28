#!/bin/bash

ollama serve &

echo "Waiting for Ollama server to start..."
sleep 5

echo "Pulling LLaMA3 model..."
ollama pull llama3

echo "Starting app..."
python main.py
