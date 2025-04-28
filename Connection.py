import mysql.connector as sql
conn = sql.connect(host='localhost',user='User',password='Your Password')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
c1.execute('create database project')
c1.execute('use project')
c1.execute('create table newuser(username VARCHAR(100) primary key,password VARCHAR(100),confirmpasswd VARCHAR(100))')
c1.execute('create table AddNewCustomer(accountno int primary key,bankname VARCHAR(25),bankbranch VARCHAR(25),name VARCHAR(25),address VARCHAR(100),areacode INT(6),phoneno BIGINT,email VARCHAR(25),boxid VARCHAR(25))')
c1.execute('create table Transaction(accountno INT(10) ,unit INT(10),toda VARCHAR(25),totamt INT(10),GST INT(10),totalamt INT(10),p VARCHAR(25) , foreign key(accountno) references AddNewCustomer(accountno))')          

print("table created")           

