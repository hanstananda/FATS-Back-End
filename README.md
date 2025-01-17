# Facial-recognition-based Attendance Taking System (FATS) - Backend

> A mobile application built for NTU's CZ3002 Advanced Software Engineering.

Web-server for Facial-recognition-based Attendance Taking System (FATS)

This is the sourcecode for the backend system of FATS prototype.

## Set up

### Prerequisites
*   Python 3.6+ (Tested with Python 3.6, 3.7, and 3.8 on the pipeline)
*   MySQL

Make sure you have the `Python 3` and `MySQL` installed. You can verify your version by running:

```
python3 --version
mysql -V
```

#### Notes 
*   You may want to use `venv` for managing the python environments.

### Running the server for the first time
1   Download and open the project directory:  
```bash
cd FATS-Back-End
```
    
2   Make migrations:  
```bash
python manage.py makemigrations
```

3   Migrate to the database server  
```bash
python manage.py migrate
```

4   Run the server  
```bash
python manage.py runserver
```

### Re-running the server 
If the database has been set up, then the system can be started directly using: 
```bash
python manage.py runserver
```
