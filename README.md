## Project Description

- Made by: Hassaan Abbasi, Anna Goncharova, Josh Baker
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

```
Project Structure
|-- .venv
|-- bin
|-- gmms
|   |-- __init__.py
|   |-- routes.py
|   |-- templates/
|   |-- static/
|-- tests
|   |-- __init__.py
|   `-- test_routes.py
|-- docs
|-- requirements.txt
|-- .gitignore
`-- README.md
```
## Local Environment Setup

1. Quickinstall guide: (https://flask.palletsprojects.com/en/3.0.x/quickstart/).
2. User guide for additional in depth info: (https://flask.palletsprojects.com/en/3.0.x/#user-s-guide).

**SQLite**
> We’re using SQLlite for the DataBase in the backend. In `update to python file` the back-end initializes the schemas inside back-end/sqlitedb/schemas. Each table should have it’s own schema so it’s easier to maintain.
