import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='9999943210',database='jee_main')
#if conn.is_connected():
      #print('connected sucessfully')
c1=conn.cursor()
c1.execute("create table regninfo (name varchar(50)  ,father_name varchar(50),mother_name varchar(50),examination_applied varchar(40),year int(6),gender varchar(11),date_of_birth varchar(10),nationality varchar(15),community varchar(10),minority varchar(4),Address varchar(60),dist varchar(30),state varchar(30),pin_code int(8),pho_no varchar (20),mobile_no varchar(20),e_mail varchar(45),std10_percentage decimal (7,2),aadhar_no varchar(20),registration_number varchar(20) primary key)")
conn.commit()
