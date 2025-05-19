# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install necessary build tools and libraries
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libhdf5-dev \
    pkg-config \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# Set a custom temporary directory for pip installations
ENV TMPDIR=/tmp/pip-tmp

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5002

# Run the application
CMD ["python", "main.py"]
