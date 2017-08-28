#!/usr/bin/python2.7
#
# Import psycopg2 to work with PSQL
import psycopg2
#Establish variables for database connection setting for ease in changing as needed
DATABASE = "postgres"
USERNAME = "vagrant"
HOST = "localhost"
PASSWORD = "vagrant"
#Connect to the database and notify if the connection was successful or not
try:
    conn = psycopg2.connect("dbname=%s user=%s host=%s password=%s" % (DATABASE, USERNAME, HOST, PASSWORD))
    print "Database Connected"
except:
    print "Unable to connect to the database"
    quit()
#Establish Python Cursor
cur = conn.cursor()
#Print the list of choices the user of the program can choose from.
print ("The following options are available to the user for selection.")
print ("")
print ("1) Show me the most popular three articles of all time?")
print ("2) Who are the most popular article authors of all time?")
print ("3) On which days did more than 1% of requests lead to errors?")
print ("4) Exit Program")
#Establish the selection prompt for the user
choice = input("Please make your selection: ")
choice = int(choice)
#Selection to return sql query for returning the most popular three articles
# in the db
if choice == 1:
   cur.execute("SELECT articles.title, COUNT(log.path)as num "
               "FROM log JOIN articles ON log.path "
               "LIKE '/article/' || articles.slug GROUP BY articles.title "
               "ORDER BY num DESC LIMIT (3)")
   articles = cur.fetchall()
   print "\nShow me the articles: \n"
   for row in articles:
       print "Article - ", row[0], " - Number of Views: ", row[1]
#Selection to return sql query for returning the authors based
#  on popularity - limit 4
elif choice == 2:
   cur.execute("SELECT authors.name, COUNT(log.path) as num "
               "FROM authors "
               "LEFT JOIN articles ON authors.id = articles.author "
               "LEFT JOIN log on log.path "
               "LIKE '/article/' || articles.slug || '%' "
               "GROUP BY authors.name "
               "ORDER BY num DESC LIMIT (4)")
   articles = cur.fetchall()
   print "\nShow me the articles: \n"
   for row in articles:
       print "Author - ", row[0], " - Number of Views: ", row[1]
#Selection to return sql query from two pre-established database views to see
#on what days there were more than 1% error rate
elif choice == 3:
   cur.execute("SELECT mid.final_date, mid.percentage "
               "FROM (Select base.date as final_date, (errors * 100 / total)"
               " as percentage FROM (SELECT total_views.date as date, "
               "CAST(total_errors.total as float) as errors, "
               "CAST(total_views.total"
               " as float) as total FROM total_views INNER JOIN total_errors "
               "on total_views.date = total_errors.date) as base) as mid "
               "WHERE mid.percentage > 1.0 ORDER BY mid.percentage DESC;")
   articles = cur.fetchall()
   print "\nShow me the articles: \n"
   for row in articles:
       print "Date - ", row[0], " - Percent Errors ", row[1]
#Provide a selection to the customer to close the program
elif choice == 4:
   print "\nExiting the Program - Goodbye! \n"
   quit()
#Provide error response if the customer does not select a correct option
else:
   print ("Not a valid selection")
