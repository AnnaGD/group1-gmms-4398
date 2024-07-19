## Project Description

- Made by: Hassaan, Anna Goncharova, Josh
- The GMMS is a web-based application that acts as a centralized platform for managing
maintenance operations. It serves as a centralized platform that helps to automate and
schedule maintenance activities, track them, and ensure these activities are completed in a
timely and cost-efficient manner, across multiple industries. By Consolidating maintenance tasks
into a single platform, the GMMS enhances visibility and control over maintenance processes,
by promoting more organized and systematic approach to maintenance system.


## General Information

**Technologies Used**
- FlaskApp
- Python for the back-end logic, offering robust and efficient server-side operations. 
- SQLite for storing data. https://www.sqlite.org/docs.html
- Pytest
- pdoc for API documentation that follows the project's Python module hierarchy.
- Docker for containerization, ensuring the application can be easily set up and run across different environments.


/Project Structure
|-- app
|   |-- __init__.py
|   |-- models.py
|   |-- routes.py
|   |-- templates/
|   `-- static/
|-- tests
|   |-- __init__.py
|   `-- test_routes.py
|-- docs
|-- Dockerfile
|-- compose.yaml
|-- requirements.txt
|-- .gitignore
`-- README.md

## Local Environment Setup

Setting up your local environment to run the GMMS application is straightforward with Docker and our provided Makefile. Follow these steps to get up and running:

### Prerequisites

1. Ensure you have Docker installed on your system. If not, download and install Docker from [Docker's official website](https://docs.docker.com/get-docker/).
2. Ensure your system runs `make` commands. Run the command `make help` in a terminal to check.

### Setup Instructions

1. **Clone the repository**: Clone the GMMS project to your local machine.
2. **Navigate to the project directory**: Open a terminal and change into the project's root directory.
3. **Build the Docker images**: Run the command `make build` to build Docker images for the front-end and back-end services.
4. **Start the application**: Execute `make up` to start all services in detached mode. This command uses Docker Compose to run the services defined in `compose.yaml`.
5. **Access the application**:

### Available Make Commands

- `make build` - Builds Docker images for the front-end and back-end.
- `make up` - Starts all services in detached mode.
- `make stop` - Stops all running services without removing them.
- `make down` - Stops and removes all containers, networks, and volumes.
- `make remove-image` - Removes the Docker images for all services.
- `make bash-front` - Opens a bash shell in the running front-end container.
- `make bash-back` - Opens a bash shell in the running back-end container.

- `docker ps` -  Lists all running containers.
- `docker stats` - Shows resource usage of all running containers.

For more details on each command, you can run `make help` to see a list of all available commands and their descriptions.

**SQLite**
> We’re using SQLlite for the DataBase in the backend. In `update to python file` the back-end initializes the schemas inside back-end/sqlitedb/schemas. Each table should have it’s own schema so it’s easier to maintain.
