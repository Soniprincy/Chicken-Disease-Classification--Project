# FROM python:alpine

# # RUN apt update -y && apt install awscli -y
# RUN apk update && apk add --no-cache aws-cli
# WORKDIR /app

# COPY . /app
# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]

FROM python:alpine

# Install AWS CLI and required system dependencies
RUN apk update && apk add --no-cache \
    aws-cli \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    build-base

WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run your app
CMD ["python3", "app.py"]
