# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install virtualenv && \
    virtualenv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt

COPY . /app

# Development server configuration
ENTRYPOINT ["source", "venv/bin/activate", "&&", "flask"]
CMD ["run", "--host=0.0.0.0", "--port=5000", "--reload"]

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
