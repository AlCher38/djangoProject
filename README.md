Technical Store
Project Description

An online store project that will be finalized in each lesson throughout the course.
Installation and Setup
1. Clone the Repository

git clone https://github.com/](https://github.com/AlCher38/djangoProject.git
cd TechnicalStore

2. Copy the env.example file to .env:

Open.env and replace the values of the variables with your own

cp .env.example .env

3. Start Migrations

To start migrations, use the following command:

python3 manage.py migrate

4. Load Fixture

Loading test fixtures for the database:

python3 manage.py load_fixtures

5. Run Server

To run server, use the following command:

python3 manage.py runserver

The server will be available at http://127.0.0.1:8000
