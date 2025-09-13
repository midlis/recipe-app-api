# recipe-app-api
Recipe API project (for https://www.udemy.com/course/django-python-advanced)

# Prerequisite pro psycopg2 module on macOS
```
brew install postgresql
export PATH=$(brew --prefix postgresql)/bin:$PATH
```

# django-environ
min. required version 0.12.0 otherwise potential problems with
- interpretting leading '$'
- separating comment end-of-line at '#'
