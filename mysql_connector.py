"""
This py file is used  to establish a connection to mysql database
"""
import mysql.connector
con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)
cursor = con.cursor()
word = input("Enter a word:")
query = cursor.execute("select *  from  Dictionary where Expression = '%s'" %word)
results = cursor.fetchall()
# return only 1 result from dictionary  query =
# cursor.execute("SELECT * FROM Dictionary where Expression = 'inlay'")
# Return results in an extracted list of tuples:
if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")
