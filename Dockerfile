FROM python:3.10-slim

WORKDIR /app

# Set timezone non-interactively
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir runpod

# Copy application files
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV CHECKPOINT_PATH=/runpod-volume/checkpoints

CMD ["python", "-u", "handler.py"]