import MySQLdb
import re
import datetime
# Open database connection
db = MySQLdb.connect("localhost","root","1000yearsofpain","kHealth" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
#Create table as per requirement


def Create():
	db = MySQLdb.connect("localhost","root","1000yearsofpain","kHealth" )
	sql = """CREATE TABLE USERS (ID int NOT NULL AUTO_INCREMENT,
         NAME  CHAR(20) NOT NULL,
         DOB  DATE,
         GENDER CHAR(1),
         ZIPCODE INT,
         OTHER_ZIP_CODE INT,
         ALBUTEROL INT,
         VENTOLIN INT,
         PROAIR INT,
         XOPENEX INT,
         ATROVENT INT,
         PRIMARY KEY (ID) )"""

	cursor.execute(sql)

def read(id):
	db = MySQLdb.connect("localhost","root","1000yearsofpain","kHealth" )
	cursor = db.cursor()
	if id==10000:
		sql = "SELECT * FROM USERS"
		try:
			#Execute the SQL command
			cursor.execute(sql)
			Data = []
			results = cursor.fetchall()
			for rows in results:
				id=rows[0]
				name = rows[1]
				dob = rows[2]
				dob = dob.strftime('%Y-%m-%d')
				#dob = re.sub(r"_\d{6}$", "", dob)
				gender = rows[3]
				zipCode = rows[4]
				otherZip = rows[5]
				albuterol = rows[6]
				ventolin = rows[7]
				proAir = rows[8]
				xopenex = rows[9]
				atrovent = rows[10]

				rdata={
        'id': id,
        'name':name,
        'dob': dob,
        'gender': gender, 
        'zipCode': zipCode,
        'otherZip':otherZip,
        'albuterol':albuterol,
        'ventolin':ventolin,
        'proAir':proAir,
        'xopenex':xopenex,
        'atrovent':atrovent,
    }

				Data.append(rdata)
			return Data


		except Exception as e:
			print "Error: unable to fecth data"

	sql = "SELECT * FROM USERS WHERE ID = '%d'" % (id)
	try:
		#Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		if not cursor.rowcount:
			return "User with this ID doesn't exist in database"
		for row in results:
			id=row[0]
			name = row[1]
			dob = row[2]
			dob = dob.strftime('%Y-%m-%d')
			gender = row[3]
			zipCode = row[4]
			otherZip = row[5]
			albuterol = row[6]
			ventolin = row[7]
			proAir = row[8]
			xopenex = row[9]
			atrovent = row[10]
			# Now print fetched result
			#print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" %(fname, lname, age, sex, income )
			Data = [
    {
        'id': id,
        'name':name,
        'dob': dob,
        'gender': gender, 
        'zipCode': zipCode,
        'otherZip':otherZip,
        'albuterol':albuterol,
        'ventolin':ventolin,
        'proAir':proAir,
        'xopenex':xopenex,
        'atrovent':atrovent,
    }
    ]
		return Data
	except:
		print "Error: unable to fecth data"

def write(name, timestamp, gender, zipCode, otherZip, albuterol, ventolin, proAir, xopenex, atrovent):
	db = MySQLdb.connect("localhost","root","1000yearsofpain","kHealth" )
	cursor = db.cursor()
	#Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO USERS(NAME, DOB, GENDER, ZIPCODE, OTHER_ZIP_CODE, ALBUTEROL, VENTOLIN, PROAIR, XOPENEX, ATROVENT) VALUES ('%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" %(str(name), str(timestamp), str(gender), int(zipCode), int(otherZip), int(albuterol), int(ventolin), int(proAir), int(xopenex), int(atrovent))
	try:
		#Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any errord
		db.rollback()
		# disconnect from server

def delete(id):
	db = MySQLdb.connect("localhost","root","1000yearsofpain","kHealth" )
	cursor = db.cursor()
	sql = "DELETE FROM USERS WHERE ID = '%d'" % (id)
	try:
		#Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
		return {"data":"Delete Successful"}
	except:
		# Rollback in case there is any errord
		db.rollback()
		# disconnect from server

#write('bob', 'pit', 22, 'F', 5000)
#read(1)
#Create()

db.close()