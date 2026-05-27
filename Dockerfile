FROM python:3.11-slim

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Install system packages
RUN apt update && apt install -y \
    ffmpeg \
    git \
    curl \
    && apt clean

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Upgrade pip and install requirements
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Railway provides PORT automatically
EXPOSE 8080

# Start bot
CMD ["python3", "start.py"]
