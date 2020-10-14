# Facial-recognition-based Attendance Taking System (FATS) - Backend

Web-server for Facial-recognition-based Attendance Taking System (FATS)

> A mobile application built for NTU's CZ3002 Advanced Software Engineering.

This application aims to improve the performance, experience, and integrity of the current manual attendance taking system
in most universities or institutions. It is optimized for tablets and makes use of facial recognition technology to allow
easy and efficient attendance taking at the beginning of each class. Other features provided by FATS include easy access
to past attendance records and secure overridng abilities for teachers or class coordinators. FATS is built to be highly
scalable and extensible such that it can be implemented in different schools and sectors all over the world.

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

## Notes 
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


## Contributors

This project is created by Fatty Acids a.k.a Group 1 in Lab Group TS2 in Academic Year 2020/21 Semester 1. The members of the group are:

- Jason Sebastian
- Margaret Claire Koesno
- Dennis Christopher Suherman
- Gabriella Benedicta Christianti
- Hans Tananda
- Kevin Winata
