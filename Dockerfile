FROM runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY . .
RUN pip install -e .
RUN pip install runpod

# Set environment variables
ENV PYTHONPATH=/app
ENV CHECKPOINT_PATH=/runpod-volume/checkpoints

CMD ["python", "handler.py"]