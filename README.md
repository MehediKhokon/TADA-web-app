# TADA Web App
 _A simple ta/da app with Employee ta/da history data._
 Here 
 
 #### Stack list

- Python
- Bootstrap 5
- Django


## Installation Process

###### 1. Create virtual environment
```python
pip install virtualenv
virtualenv env
```
###### Or
```python 
python -m venv env
```
###### 2. Activating virtual environment in terminal
###### For unix/mac
```python
source env/bin/activate
```
###### For Windows
```python
.\env\Scripts\activate
```

###### 3. Install require package
```python
pip install -r requirements.txt
```

###### 4. Database initialize and migration
```python
python manage.py migrate
```

###### 5. Start Servar
```python
python manage.py runserver
```

_For creating more user there is admin built in features in Django._
###### Admin Credential
URL:
```
http://127.0.0.1:8000/admin/
```
_User: hasan22_
<br>
_Password: hasan22_

