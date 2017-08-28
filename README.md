# Python and PostGres SQL Logs Project
## This is a Udacity FSND project

# Introduction

This program is to show understanding of both Python and SQL syntax in general.  The database was provided by Udemy and uploaded into a VirtualBox - PSQL system with the database running on "localhost:5432". The solutions to three questions were required:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The solution to these problems is calculated completely with SQL queries allowing the database to perform the computations.

# Getting Started

The user of the program must have PostGres SQL installed and running on localhost:5432 in order to connect.  If the user is using a different port, the port perameter must be added to the psycopg2.connect statement.  The standard Udacity user vagrant is coded to a variable in the psqlcon.py file and can be updated as required.  A password is also coded to a variable and can be updated as needed.  For the purpose of providing security, vagrant was added as the password.  The database name is **postgres**.

In addition to the Udacity provided database, tables, and values, two views were created to minimise processing time for question 3.  To create these views, on can copy and paste the following two statements and execute to the database.  Due to difficulties with Vargant, the newsdata.sql file was uploaded to postgres manually via the command \i <path>newsdata.sql.  The lastest version of this sql database file can be found on Udemy's website.

CREATE VIEW total_errors AS
SELECT date(time), count(status) AS total
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY date(time)

CREATE VIEW total_views AS
SELECT date(time), count(status) AS total
FROM log
GROUP BY date(time)

**NOTE** Credit to this view creation goes to subadhra.srinivas on the Udacity Forums [Udacity Post 294406](https://discussions.udacity.com/t/is-my-query-3-results-right/294406)

Once the database is in place and the two views have been created successfully, the user will run the program psqlcon.py using Python 2.7.  Once running, the user can selected the option they wish to see the result of and press enter.  The program will automatically exit when completed.

# Design of The Program
## psqlcon.py
The program was written using Python 2.7 and psycopg2 which was downloaded through shell using the command 'pip install psycopg2'.  The program uses variables for the database connection requirements so as to ease any changes required by users with different parameters.  Provided that the user is running PostGres SQL as stated in the introduction and has set their parameters for the connection, only the source file of psqlcon.py is required to operate the program.

# Credits and Notes

As noted in the getting started section, subadhra.srinivas on the Udacity Forums provided the idea and code for creating the views.  This was modified slightly for the purpose of my project.

Much of the Python code was generated based on internet searches and parts of other users suggested code.  While there was not direct copying of any other users code other than that used to create the views, it should be noted that many post only contributed to the final outcome and final version of the project.

# License

Python is used in agreement with Python 2.7 license which can be found in whole at the following link: [Python 2.7 License](https://www.python.org/download/releases/2.7/license/)
