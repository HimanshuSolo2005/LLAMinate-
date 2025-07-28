# Use Ubuntu base
FROM ubuntu:22.04

# Avoid user interaction prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    python3 \
    python3-pip \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull LLaMA 3 model so it's ready
RUN ollama pull llama3

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Run the app
CMD ["python3", "app.py"]
