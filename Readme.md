# Initial commands



```script

mkdir flask\_start

cd flask\_start

mkdir templates



git init

git remote add origin https://github.com/yonyu/flask_start.git
git branch -M master



python -m venv .venv

.venv\\Scripts\\activate

-- flask 3.1.2
pip install Flask

```


# VS Code extensions

Python
Jupyter - for working with Jupyter notebooks
Pylance - tool for type checking

Even Better TOML - for pyproject.toml files
Better Jinja - Jinja2 template syntax highlighting
Ruff - the best and only linter you'll need
Live Preview - lets you render web pages within VS Code with auto-refresh
Python Indent - Correct Python indentation

Markdown All in One - because you'll generally see plenty of Markdown in project

Traycer - an AI assistant. Alternatives: Black Box, Windsurf Plugin (formerly Codeium)

# Initial files and folders for a Flask app



app.py

requirements.txt: list libraries that can be installed by the server automatically

static/

templates/

jinja is used

flask run
http://127.0.0.1:5000/
http://127.0.0.1:5000/?name=carter



