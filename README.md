# Thi Blog App:

## Project Setup Guide
## Install uv on Windows machines
### https://docs.astral.sh/uv/getting-started/installation/#cargo

## How to run this project after cloning from GitHub
- git clone https://github.com/your-username/fastapi_blog.git
- cd fastapi_blog
- uv sync

### I have developed this app using this follwing toutorial for learning purposes.
## Through this project:
- Authentication and authorization in FastAPI
- Working with relational databases (SQLAlchemy + PostgreSQL)
- Security concepts in data validation and serialization
- Application configuration using environment-based settings [Pydantic-Settings]
- Structuring a FastAPI project in a scalable way

## Project Setup Guide
## Dev Instructions
## - uv init fastapi_blog
### This will create a new project directory with basic files such as:
- main.py
- pyproject.toml
- uv.lock
- README.md

## - uv init .
### Use this if you are already inside a project directory.

## cd fastapi_blog
## uv add "fastapi[standard]"
- Automatically creates a virtual environment (if not already present)
### - Installs FastAPI and required dependencies, including
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (data validation)
- Standard tooling for FastAPI development
- Updates: pyproject.toml, uv.lock

## uv run uvicorn main:app --reload
### It starts a web server using Uvicorn and automatically reloads the application 
### to reflect any code changes immediately without restarting.

## Packages Installed in this project:
- uv add pillow
- uv add sqlalchemy
- uv add "pwdlib[argon2]" pyjwt pydantic-settings
- uv add aiosmtplib
- uv add uv add "psycopg[binary]"

## Project Settings to Organise Imports:
### These lines are included to pyproject.toml
- [tool.uv.workspace]
- [tool.black]
- line-length = 140

- [tool.ruff]
- line-length = 88
- select = ["E", "F", "I"]  # E/F = linting, I = import sorting
- fix = true

- [tool.ruff.format]
- quote-style = "double"

### These setting are included in setting.json 
{
  "editor.formatOnSave": true,

  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true
  },

  "ruff.lint.run": "onSave"
}

## VSCode Extensions
- Ruff (official extension)
- Ruff (official extension)