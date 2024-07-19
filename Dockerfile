# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

# Set the working directory in the Docker image
WORKDIR /app

# Environment variable for the virtual environment location
ENV VENV_PATH=/opt/venv

# Create virtual environment in a directory not affected by bind mounts
RUN python -m venv $VENV_PATH

# Install Python dependencies
COPY requirements.txt /app/
RUN $VENV_PATH/bin/pip install -r requirements.txt

# Copy the rest of your application's code into the Docker image
COPY . /app

# Set environment to ensure commands and scripts run in the virtual environment
ENV PATH="$VENV_PATH/bin:$PATH"

# Command to run your application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# Continue installing Docker tools and other necessary components
