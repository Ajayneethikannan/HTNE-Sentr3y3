# ThirdEye

Instructions to install the application:
1. Clone the repo and enter it
```
git clone <url> && cd Sentr3y3
```

2. Create a virtual environment
```
python3 -m venv venv
```

3. Activate the virtual environment
```
source venv/bin/activate
```

4. Install the requirements for pip
```
python3 -m pip install --upgrade --user pip setuptools virtualenv
pip install wheels
```

5. Install the dependencies
```
pip install -r requirements.txt
```

6. Enter the django project, Migrate the database, create a super user
```
cd djangProj
python manage.py makemigrations details
python manage.py migrate
python manage.py createsuperuser
```

7. Run the django server
```
python manage.py runserver
```

8. Run the application
```
python mainApplication.py
```

9. To change the content restriction settings and to add/change the apps timings, go to the website http://localhost:8000/admin/details


Enjoy your freedom at home and work to your heart's content without worrying about content restriction and wastage of time !
