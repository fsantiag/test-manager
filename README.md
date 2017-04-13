Test Executiopn Manager
=======================

The Test Execution Manager is a general purpose tool build using Python3 to submit and check tests executions.

![Test Execution Manager](docs/images/tem.png)

The project has two main componentes:
* Scheduler
* Django App

The scheduler is the component responsible for starting the execution of the tests according to the environment selected as well as checking if the tests have already finished so its status can be properly updated.
The Django App is a regular RESTful API to serve html to clients.

New tests can be inserted by placing the respective testes under /autotests/tests.

This project is based in a free bootstrap template [SB Admin](https://startbootstrap.com/template-overviews/sb-admin/).

Intallation and Configuration
-----------------------------

Install Django:

```
pip install django==1.11
```

In the root folder, populate the database:
```
echo ".read db.sql" | ./manage.py dbshell
```

Running
-------

* First, start the scheduler:
```
./start_scheduler.sh
```

* Second, start the web server:
```
./manage.py runserver
```


The app will be running at localhost:8000/runs/

License
-------

MIT is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).