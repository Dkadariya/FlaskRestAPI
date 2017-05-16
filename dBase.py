import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","1000yearsofpain","dipnot" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
#Create table as per requirement
#sql = """CREATE TABLE EMPLOYEE (ID int NOT NULL AUTO_INCREMENT,
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,  
#         SEX CHAR(1),
#         INCOME FLOAT,
#         PRIMARY KEY (ID) )"""

#cursor.execute(sql)

def read(id):
	db = MySQLdb.connect("localhost","root","1000yearsofpain","dipnot" )
	cursor = db.cursor()
#	if id==10000:
#		sql = "SELECT * FROM EMPLOYEE"
#		try:
#			pass
#		except Exception as e:
#			raise
	sql = "SELECT * FROM EMPLOYEE WHERE ID = '%d'" % (1)
	try:
		#Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		for row in results:
			id=row[0]
			fname = row[1]
			lname = row[2]
			age = row[3]
			sex = row[4]
			income = row[5]
			# Now print fetched result
			print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" %(fname, lname, age, sex, income )
			Data = [
    {
        'id': id,
        'fname':fname,
        'lname': lname,
        'age': age, 
        'sex': sex,
        'income':income
    }
]
		return Data
	except:
		print "Error: unable to fecth data"

def write(fname,lname,age,sex,income):
	db = MySQLdb.connect("localhost","root","1000yearsofpain","dipnot" )
	cursor = db.cursor()
	#Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" %(fname,lname,age,sex,income)
	try:
		#Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any errord
		db.rollback()
		# disconnect from server

#write('bob', 'pit', 22, 'F', 5000)
#read(1)

db.close()