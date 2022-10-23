# Flask Crud with JWT

### 📚 About the project

### Structure

```bash
.
├── src  (MAIN PACKAGE)
│   ├── app.py
│   ├── database
│   │   ├── models.py
│   │   └── users_db.py
│   ├── extensions
│   │   ├── bleuprints.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   └── database.py
│   ├── routes
│   │   ├── auth_route.py
│   │   └── user_route.py
│   ├── schemas  (SERIALIZER SCHEMAS)
│   │   └── user_schema.py
│   ├── services
│   │   ├── auth_service.py
│   │   └── user_service.py
│   └── utils
│   │   ├── auth_util.py
│   │   └── responses_util.py
├── tests  (TESTS)
│   └── __init__.py
├── README.md
├── requirements.txt
└── settings.toml  (SETTINGS)
```

> This project its a simple examble using flask to create a CRUD and authorize sessions utilizing JWT for that.

## 💻 Built With

- ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
- ![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- ![](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)

#### Adjustments and Improvements

This project still in development, here some tasks that im working:

- [X] Project structure
- [X] Create the logic about the JWT authentication
- [X] Create the structure of the routes
- [ ] Create the connection with the database
- [ ] Create the logic at the services classes
- [ ] Create the schemas for validate imputs and outputs]
- [ ] Build the swagger doc
- [ ] Build the handle errors

## 🚀 Getting Started

To install the project follow this steps:

#### Windows

First we need to clone the project:

```
git clone https://github.com/ppcantidio/flask-jwt
```

Lets create our python venv

```
python -m venv venv
```

To activate de venv:

```
venv\Scripts\Activate
```

To install the dependences:

```
pip install -r requirements.txt
```

To run:

```
flask run
```
