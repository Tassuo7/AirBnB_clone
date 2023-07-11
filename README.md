# AirBnB_clone
![img](https://www.aydentownsley.com/img/hbnb.png)
## Project Description
The AirBnB clone project is to deploy on your server a simple copy of the [AirBnB website](https://fr.airbnb.com/?_set_bev_on_new_domain=1689093982_NDQ0M2I3YWY1MTcy). The clone includes the implementation of a command interpreter to manage AirBnB objects and a storage system to store and retrieve data.
## Steps
### The console
The console is  command interpreter provides a command-line interface to interact with and manage the AirBnB objects. It allows you to create, retrieve, update, and delete objects, as well as perform operations and computations on them
**Using the Console**
**_The AirBnB console can be run both interactively and non-interactively (like the Shell project in C)_**
* interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
* non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
