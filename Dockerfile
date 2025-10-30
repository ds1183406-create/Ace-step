FROM runpod/pytorch:2.1.0

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
RUN pip install runpod

# Copy application files
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV CHECKPOINT_PATH=/runpod-volume/checkpoints

CMD ["python", "-u", "runpod_handler.py"]