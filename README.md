# recipe-app-api
Recipe API project (for https://www.udemy.com/course/django-python-advanced)

# Prerequisites for building psycopg2 module on macOS
```
brew install postgresql
export PATH=$(brew --prefix postgresql)/bin:$PATH
```

# Prerequisites for building psycopg2 on linux
```
sudo apt install libpq-dev
```

# django-environ
min. required version 0.12.0 otherwise potential problems with
- interpretting leading '$'
- separating comment end-of-line at '#'

# VSCodium extensions

- Black Formatter :: ms-python.black-formatter
- Flake8 :: ms-python.flake8
- Pylint :: ms-python.pylint
- GitLens :: eamodio.gitlens
- Open Remote - SSH :: jeanp413.open-remote-ssh
- Python :: ms-python.python
- Python Debugger :: ms-python.debugpy
- Python Snippet 3 :: ericsia.pythonsnippets3
- MagicPython :: magicstack.magicpython
- Django :: batisteo.vscode-django
- BasedPyright :: detachhead.basedpyright
