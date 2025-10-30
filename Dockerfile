FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel

WORKDIR /app

# Set timezone non-interactively
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

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