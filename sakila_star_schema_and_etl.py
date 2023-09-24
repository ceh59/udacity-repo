import platform
import getpass
import psycopg2 as psc
import datetime

h = platform.uname()
#print(h)

pw = getpass.getpass("Database Password: ")

try:
    conn = psc.connect(database="caitlinelaine",
                            host="localhost",
                            user="caitlinelaine",
                            password=pw,
                            port="5432")
except:
    print("Password was incorrect.")

cursor = conn.cursor()

##HOW MUCH -- WHAT DATA SIZES ARE WE LOOKING AT?
tables = ['store','film','customer','rental','payment','staff','city','country']
counts = []
iteration = 0
table_counts = ['nStores','nFilms','nCustomers','nRentals','nPayment','nStaff','nCity','nCountry']
for table in tables:
    query = "SELECT COUNT(*) FROM " + table
    cursor.execute(query)
    result = cursor.fetchone()
    for row in result:
        counts.append(row)
for count in table_counts:
    result = count + " = " + str(counts[iteration])
    print(result)
    iteration += 1

##WHEN -- WHAT TIME PERIOD ARE WE TALKING ABOUT?
print("\n")
query = "SELECT MIN(PAYMENT_DATE) AS START, MAX(PAYMENT_DATE) AS END FROM payment"
cursor.execute(query)
timespan = cursor.fetchall()
for value in timespan:
    start = value[0].strftime('%m/%d/%Y %H:%M:%S')
    end = value[1].strftime('%m/%d/%Y %H:%M:%S')
    print("Start: " + start)
    print("End: " + end)


##WHERE -- WHERE DO EVENTS IN THIS DATABASE OCCUR?
##Write a query that provides the number of addresses by district in the address table.
##Limit the table to the top 10 results
print("\n")
query = "SELECT DISTRICT, COUNT(*) AS N FROM address GROUP BY 1 ORDER BY 2 DESC,1 ASC LIMIT 10"
cursor.execute(query)
result = cursor.fetchall()
for district in result:
    print(district[0] + ": " +str(district[1]))
