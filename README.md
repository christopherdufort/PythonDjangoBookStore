# SOEN 341-H Software Process Fall 2018 - Term Project

Library Catalog Software System V1.0

Library Catalog is a user oriented software system designed to automate the library process for both library clients as well as library administrators. The user functionalities include searching and browsing the library catalog as well as loaning and returning items. The administrators have the capability of adding, removing and modifying library items. Additional documentation about software specifications are available in the SRS Document (Software Requirement Specification) and code implementation details are available in the SAD Document (Software Architecture Document).


## Prerequisite
Install the following:
* Python 3.7.0
* Django 2.1.2
* MySQL 5.7.23 (5.6.0+)
* ...
----
Following used for windows development:
* pip 18.1 (10.1+)
* wheel 0.32.1
* [mysqlclient-1.3.13-cp37-cp37m-win32.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python)
* "pip install pymysql" - connector package
*..
---
Mac/Linux:
* ...

## Installing

1. git pull origin master
2. git checkout -b "new branch name"
3. cd */library
4. python manage.py runserver

### Team Member Information
| Student name       | Student ID |
| :-----------------:|:-----------:|
| Christopher Dufort (Team Lead) | #40030286 |
| Michael Garner	 | #26338739 |
| Alessandro Kreslin	 |#40025121|	
|Carlita L’Abbe	 |	#40028020	|
|Surya Prakash |	#40085527	|
|Sahana Anantha |	#40085533	|
| Sai Charan Teja Doddi |	#40076338	|
| Shruthi Kondapura Venkataiah|	#40091427|

## Installation and Run Program Full Instructions
1. Install the following programs (Get version for your system)
*Assumed to have web browser already installed (Chrome, Firefox, Safari, Edge...)
Install WAMP to run SQL and PHP scripts [ http://www.wampserver.com/en/ ] Use Installation wizard
mySQL workbench   [ https://www.mysql.com/products/workbench/ ]   Use Installation wizard
GIT [ https://git-scm.com/downloads ]   Use Installation wizard
Python [https://www.python.org/ ]    Use Installation wizard
Django [ https://www.djangoproject.com/download/ ] Use Git
Download mySQL configuration file 
  *if on windows: mysqlclient-1.3.13-cp37-cp37m-win32.whl [ https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python ]

2. Install Additional software and Install
Install Django, mySQL and pySQL (and update django)
  Open Git CMD 
  command: pip install Django==2.1.3
  command: git clone https://github.com/django/django.git
  command: pip install <location of .why file>mysqlclient-1.3.13-cp37-cp37m-win32.whl
  command: pip install pymysql

3. Create a Git Hub Folder Location, Initialize and Clone the Repository
Create a directory on the local computer for the code repository
clone repository from git
  Open Git CMD 
  command:  git clone https://github.com/christopherdufort/SOEN-341-H-Fall-2018.git

4. Create Database and Tables, populate tables with data from included script or an external data file with Library database
Open mySQL workbench and run the .SQL script included in SOEN-341-H-Fall-2018\LibraryCatalog\library\migrations

5. Configure the settings for your system
Enter your system's specific password in:
  SOEN-341-H-Fall-2018\LibraryCatalog\library\settings.py (line 84)
  SOEN-341-H-Fall-2018\LibraryCatalog\library\DataBaseLayer.py (lines 15, 30, 45, 58)

6. Execute the program
Ensure that the system is running apache and SQL server compatible operating system directly or virtually with WAMP (or other)
Run the python code from the 
  Open Git CMD 
  command: python manage.py runserver
  
7. Open a web browser and enter the URL address given from the GIT CMD console 
Ex. http://127.0.0.1:8000/



