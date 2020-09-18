# CZ3002-Backend

Web-server for Facial-recognition-based Attendance Taking System (FATS)

## Requirements
*   Python 3.6+ (Tested with Python 3.6, 3.7, and 3.8 on the pipeline)
*   MySQL

## Notes 
*   You may want to use `venv` for managing the python environments.

## Running the server for the first time
*   Make migrations: 
    ```bash
    python manage.py makemigrations
    ```

*   Migrate to the database server
    ```bash
    python manage.py migrate
    ```

*   Run the server
    ```bash
    python manage.py runserver
    ```