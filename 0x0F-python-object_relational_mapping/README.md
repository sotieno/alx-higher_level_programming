# 0x0F. Python - Object-relational mapping

In this project, I link two amazing worlds: Databases and Python!

In the first part, I use the module MySQLdb to connect to a MySQL database and execute SQL queries.

In the second part, I use the module SQLAlchemy an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, the biggest concern is “What can I do with my objects” and not “How is this object stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You are able to change your storage easily without re-writing your entire project.

The biggest difficulty with ORM is: The syntax! Indeed, all of them have the same type of syntax, but not always.

## Focus

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Requirements

* Ubuntu 20.04 LTS using python3
* MySQLdb version 2.0.x
* SQLAlchemy version 1.4.x
* pycodestyle version 2.8.*
* All files are executable
* All modules have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All classes have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All functions (inside and outside a class) have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

### How to install MySQL

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
```

### How to install MySQLdb

For installing MySQLdb, you need to have MySQL installed.
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

### How to install SQLAlchemy

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```



