import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sputnik7#"
)
print(mydb)

mycursor = mydb.cursor()
test = []

mycursor.execute("select B1_PER_ID1,B1_PER_ID2,B1_PER_ID3 from tc_db.b1permit limit 20;")
myresult = mycursor.fetchall()

for x in myresult:
    tst = [x[0] , x[1], x[2]]
    test.append(tst)

for y in test:
    print(y[2])