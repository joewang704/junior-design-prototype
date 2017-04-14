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

t0 activate virtual environment:

    windows:
```
$ venv\Scripts\activate   
```

    Posix:
```
$ source venv/bin/activate   
```

(to deactivate virtual environment):
```
$ deactivate   
```

install python dependencies using requirements.txt:
    make sure virtual environment is activated
    ```
    $ venv/bin/pip install -r requirements.txt  
    ```


## Usage
  run server:
    make sure virtual environment is activated 
    navigate to django_site/ folder  
    ```
    $ python manage.py runserver  
    ```

## Coding Conventions
    Follow PEP8    
    Use four spaces for python

## Problems
If no relation is found from users to profile try:
```
$ python django_site/manage.py shell < add_profile_to_user.py
```

## Pushing changes to AWS
Authorized users should have the AWS account credentials. To push changes go to https://console.aws.amazon.com/elasticbeanstalk -> All Applications -> Environments -> django_site -> HealthItForward-new 
In Overview there should be an option to Upload and Deploy. Make sure to zip the root folder as django_site, NOT HealthItForward. after zipping, upload and the changes should be made.
