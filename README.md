## Install Guide
### Prerequisites
- Python 2.7 and Pip
    - https://www.python.org/downloads/
    - When downloading Python 2.7 from this website, pip will be installed with it
- Virtualenv
    - Open a terminal window and run ```pip install virtualenv```
    - Tutorial on how to open terminal on [Windows](https://www.quora.com/How-do-I-open-terminal-in-windows) or [Mac OS](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)


### Dependent libraries that must be installed
- PostgreSQL
    - https://www.postgresql.org/download/

### Download instructions
1. Clone the github repository
    - https://help.github.com/articles/cloning-a-repository/
2. Create virtual environment (specify path if default interpreter is python3):
```
$ cd [HealthItForward/]
$ virtualenv [-p path/to/python2.7] venv  
```
(Note: anything in these blocks is meant to be run in terminal)

3. Activate virtual environment:

    Windows: ```$ venv\Scripts\activate```

    Mac OS/Linux: ```$ source venv/bin/activate```

### Installation of actual application

1. Install python dependencies using requirements.txt:
    make sure virtual environment is activated
    ```
    $ venv/bin/pip install -r requirements.txt  
    ```


### Run Instructions
  1. Make sure virtual environment is activated, meaning the previous commands must have just been run in the same terminal window
  2. 
  ```
  $ cd django_site/
  $ python manage.py runserver  
  ```

## Coding Conventions
    Follow PEP8    
    Use four spaces for python

## Pushing changes to AWS
Authorized users should have the AWS account credentials. To push changes go to https://console.aws.amazon.com/elasticbeanstalk -> All Applications -> Environments -> django_site -> HealthItForward-new 
In Overview there should be an option to Upload and Deploy. Make sure to zip the root folder as django_site, NOT HealthItForward. after zipping, upload and the changes should be made.
