# Use slim-based Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

# Set work directory
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt /app/

# Update package list and install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    postgresql-client \
    bash && \
    # Install pip and dependencies
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    # Clean up cache and unnecessary build dependencies
    apt-get purge -y --auto-remove gcc python3-dev build-essential && \
    apt-get clean

# Copy project files to the container
COPY . /app
