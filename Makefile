.PHONY: help build up down stop remove-image shell logs test doc

# Define variables for docker-compose commands
COMPOSE=docker compose
COMPOSE_FILE=compose.yaml

help:
	@echo "Available targets:"
	@echo "  build        - Build the Docker images for the web service."
	@echo "  up           - Start all services in detached mode."
	@echo "  down         - Stop and remove containers, networks created by 'up'."
	@echo "  stop         - Stop all running services."
	@echo "  remove-image - Remove the Docker images for all services."
	@echo "  shell        - Access the shell of the web service container."
	@echo "  logs         - View output from containers."
	@echo "  test         - Run pytest for the application."
	@echo "  doc          - Generate project documentation using pdoc."

# Build the Docker images
build:
	$(COMPOSE) -f $(COMPOSE_FILE) build

# Start the Docker containers
up:
	$(COMPOSE) -f $(COMPOSE_FILE) up -d

# Stop and remove containers, networks, etc.
down:
	$(COMPOSE) -f $(COMPOSE_FILE) down

# Stop the Docker containers without removing them
stop:
	$(COMPOSE) -f $(COMPOSE_FILE) stop

# Remove the Docker images
remove-image:
	$(COMPOSE) -f $(COMPOSE_FILE) down --rmi all

# Access the container's shell for the web service
shell:
	$(COMPOSE) -f $(COMPOSE_FILE) exec web /bin/ash

# View logs from containers
logs:
	$(COMPOSE) -f $(COMPOSE_FILE) logs -f

# Run pytest inside the container
test:
	$(COMPOSE) -f $(COMPOSE_FILE) exec web pytest /app/tests

# Generate documentation using pdoc
doc:
	$(COMPOSE) -f $(COMPOSE_FILE) exec web pdoc --html --output-dir /app/docs /app
