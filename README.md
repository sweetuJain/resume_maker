<p>git init</p>
<p>uv venv .venv</p>
<p>for windows -> .\venv\Scripts\activate</p>
<p>for Mac/Linux -> source venv/bin/activate</p>
<p>
    Ctrl + Shift + P
    Python: Select Interpreter
    .\venv\Scripts\python.exe
</p>
<p>mkdir app app/core app/db app/api app/models app/schemas app/tests</p>
<p>uv pip install pydantic  - for typescript </p>
<p>uv pip install passlib[bcrypt] - for password encrypted </p>
<p>uv pip freeze - fro check installed packages </p>

<h2><b>Install Packages</b></h2>
fastapi
uvicorn
psycopg2-binary
sqlalchemy
pydantic
python-dotenv
passlib[bcrypt]
python-jose
pytest
black
ruff
mypy

pip install -r requirements.txt - for production cmd
create toml 
touch app/main.py

uv run ruff check . --fix
uv run ruff check .
uv run uvicorn app.main:app --reload

export ENV=local  - #Linux / Mac
setx ENV local - Windows

export ENV=local - for Mac/Linux
 $env:ENV="staging - for Windows 