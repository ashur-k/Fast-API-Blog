TODO finsih Corey toutorial on pathlib and https://www.youtube.com/watch?v=AMdG7IjgSPM

first install uv on windows machines
https://docs.astral.sh/uv/getting-started/installation/#cargo

then create project folder 
 uv init fastapi_blog --> this will create fast_api blog with some basic files e.g. main.py, myproject.toml, readme.md

 uv init . # if already have folder

 cd into folder fastapi_blog

 uv add "fastapi[standard]"

 this command will look for virtual env and if it not exist it will automatically create it. and it will install fastapi + some extras into projecct for example fastapi, uvicorn, pydantic, standard asgi server setup tools, it will also update pyproject.toml and uv.lock files automatically.

 uv run fastapi dev main.py -> this command will auto relaod changes into the project if changes made or restarted

uv add pillow
uv add sqlalchemy

uv add "pwdlib[argon2]" pyjwt pydantic-settings
uv add aiosmtplib