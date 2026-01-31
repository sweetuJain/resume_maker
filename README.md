git init
uv venv venv
for windows -> .\venv\Scripts\activate
for Mac/Linux -> source venv/bin/activate
Ctrl + Shift + P
    Python: Select Interpreter
    .\venv\Scripts\python.exe

mkdir app app/core app/db app/api app/models app/schemas app/tests
uv pip install pydentic - for typescript 
uv pip install passlib[bcrypt] - for password encrypted 
uv pip freeze - fro check installed packages 



<h2><b>install packages</b></h2>
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
