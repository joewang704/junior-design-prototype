## Installation
Install python 2.7
Install pip
Install virtualenv:
```
$ pip install virtualenv 
```

## Setup
create virtual environment (specify path if default interpreter is python3):
```
$ cd [HealthItForward/] 
$ virtualenv [-p path/to/python2.7] venv  
```

install python dependencies using requirements.txt:
```
$ venv/bin/pip install -r requirements.txt  
```

activate virtual environment:

    windows:
```
$ venv\Scripts\activate   
```

    Posix:
```
$ source venv/bin/activate   
```

deactivate virtual environment:
```
$ deactivate   
```
    
## Usage
run server:
    activate virtual environment 
    navigate to django_site/ folder  
    ```
    $ python manage.py runserver  
    ```

## Coding Conventions
    Follow PEP8    
    Use four spaces for python
