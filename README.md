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
