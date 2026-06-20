# The Blog App:

## Project Setup Guide
### Install uv on Windows machines
#### https://docs.astral.sh/uv/getting-started/installation/#cargo

### How to run this project after cloning from GitHub
- git clone https://github.com/your-username/fastapi_blog.git
- cd fastapi_blog
- uv sync

### Through this project:
- Authentication and authorization in FastAPI
- Working with relational databases (SQLAlchemy + PostgreSQL)
- Security concepts in data validation and serialization
- Application configuration using environment-based settings [Pydantic-Settings]
- Structuring a FastAPI project in a scalable way

### Project Setup Guide - Dev Instructions
#### - uv init fastapi_blog
#### This will create a new project directory with basic files such as:
- main.py
- pyproject.toml
- uv.lock
- README.md

### - uv init .
- Use this if you are already inside a project directory.

### Run Following Commands:
- cd fastapi_blog
- uv add "fastapi[standard]"
- Automatically creates a virtual environment (if not already present)
#### Installs FastAPI and required dependencies, and starts FastAPI Webserver
#### Starts Uvicorn server with auto-reload on code changes.
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (data validation)
- Standard tooling for FastAPI development
- Updates: pyproject.toml, uv.lock
- uv run uvicorn main:app --reload


### Project Dependencies:

```bash
uv add pillow
uv add sqlalchemy
uv add "passlib[argon2]" pyjwt pydantic-settings
uv add aiosmtplib
uv add "psycopg[binary]"
```

#### The project-level project-level formatting rules in pyproject.toml configuration.
```toml
[tool.uv.workspace]

[tool.black]
line-length = 140

[tool.ruff]
line-length = 88
select = ["E", "F", "I"]  # E/F = linting, I = import sorting
fix = true

[tool.ruff.format]
quote-style = "double"
```

#### Add setting.json
#### VS Code is configuration to use Ruff for auto-formatting and linting on save.
```json
{
  "editor.formatOnSave": true,

  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true
  },

  "ruff.lint.run": "onSave"
}
```
### Required VSCode Extensions
- Ruff (official extension)
- Ruff (official extension)