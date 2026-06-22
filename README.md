# The Blog App:

## Project Setup Guide
### Install uv on Windows machines
#### https://docs.astral.sh/uv/getting-started/installation/#cargo

### How to run this project after cloning from GitHub
- git clone https://github.com/your-username/fastapi_blog.git
- run `cd fastapi_blog`
- run `uv sync`
- run `uv run fastapi dev main.py` to start proj in dev mode

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
- uv add --dev "moto[s3]" -> this is not used


### Project Dependencies:

```bash
uv add pillow
uv add sqlalchemy
uv add "passlib[argon2]" pyjwt pydantic-settings
uv add aiosmtplib
uv add "psycopg[binary]"
uv add alembic
uv add --dev pytest
```

#### Project-Level formatting rules in pyproject.toml configuration.
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

## Database Migrations

We use **Alembic** for database migrations.

Alembic is a database migration tool used to manage and version-control changes to a database schema over time,
especially in FastAPI projects using SQLAlchemy and PostgreSQL. It allows you to define schema changes as 
migration files instead of writing manual SQL, and then apply or rollback those changes safely across
development, staging, and production environments. This ensures all environments stay in sync, reduces 
the risk of schema drift, and provides a clear history of database evolution.

**Alternatives:** 
- Alembic is best suited for Python + FastAPI due to tight ORM integration and lightweight design.
- Django migrations 
- Prisma migrations 
- Flyway
- Liquibase

Run `uv run alembic init -t async alembic`
- alembic init → creates Alembic folder structure
- -t async → tells Alembic to use the async SQLAlchemy template
- alembic → folder name to generate

**Alembic Async Alternatives:** 
Run `alembic init -t generic alembic
- Standard SQLAlchemy Engine
- Blocking DB calls (no async/await)
- Simpler setups

`uv run alembic init -t async alembic` -> This will create several dirs and files:
FASTAPI_BLOG/
├── main.py
├── alembic.ini
└── alembic/
    ├── env.py
    ├── README
    ├── script.py.mako
    └── versions/

- alembic.ini → main Alembic configuration file
- alembic/env.py → migration runtime logic (DB connection setup)
- alembic/versions/ → all migration files (auto-generated)
- script.py.mako → template for new migration files
- README → Alembic folder explanation (rarely used)

Once above command is executed copy the changes from following files
FASTAPI_BLOG/
├── alembic.ini
- sqlalchemy.url = driver://user:pass@localhost/dbname
- change to --> sqlalchemy.url =

└── alembic/
    ├── env.py

make follwoing imports
- from alembic import context --> Add below lines after this line

- import models  # noqa: F401
- from alembic import context
- from config import settings
- from database import Base

- config = context.config --> Add below lines after this line
- config.set_main_option("sqlalchemy.url", settings.database_url)

- target_metadata = None --> update this line to below line
- target_metadata to Base.metadata
This tells alembic to use Base.metadata as source of thruth to for 
what the database schema should look alike

#### For Windows this change is required before running following command
This command will work only on mac and linux and on windows you might need
to play with your alembic/env with below change to make the command work with windows
```
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    if sys.platform.startswith("win"):
        # This will be deprecated in python 3.16
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(run_async_migrations())
```

Run ` uv run alembic revision --autogenerate -m "initial schema"`
- command generates migrate files in alembic/versions folder
- autogenerate tells alembic to look at model files and autogenerate migrations
- compare them to current state of database
- this will only create migrations but will not apply migration

#### To apply migrations
Run `uv run alembic upgrade head`

#### Postgres Commands
Its considered postgres is installed and running
I have googled to install postgress on Windows and then have set psql path

### Windows Terminal
Run `[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\PostgreSQL\18\bin", "Machine")`
Run `psql --version`
Output `(PostgreSQL) 18.4`

Run `psql -U postgres`
Give password

run `\l` to see database
run  `\du` to see users
run `\dt;` to see tables
run `\c blogdb bloguser` to connect to database with user
run `\dt` to see tables

run `\d posts` to see table structures

Selcting database directly from windows shell
run `psql blogdb -U bloguser`

Running Database queries
run `psql blogdb -U bloguser`


#### Alembic Commands
run `uv run alembic current`
run `SELECT id, title, likes FROM posts;`

```
\fastapi_blog> uv run alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
e3d2b535b7fe (head)
```
The head at the end means we are on latest version

Update migrations when change is made to database models
run `uv run alembic revision --autogenerate -m "Included new likes to the post model"`
run `uv run alembic upgrade head`

To roll back migrations
run `alembic downgrade -1`

IF required to check where current migrations are:
run `uv run alembic current`
run `uv run alembic history`


#### Tests
run ` uv run pytest/ -v` to run all tests
run `uv run pytest tests/test_users.py -v` to run tests for file
run `uv run pytest tests/test_users.py::test_create_user_validation_error -v` to run specific test
run `uv run pytest tests/ -s` for debuggin purposes if you want to show print statements

-v means verbose mode. It makes pytest print more details about the test run.
