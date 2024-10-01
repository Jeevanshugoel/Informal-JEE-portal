import csv
import random
import mysql.connector as sql
import matplotlib.pyplot as plt
def sign_up():
    conn=sql.connect(host='localhost',user='root',passwd='9999943210',database='jee_main')
    #if conn.is_connected():
    #print('connected sucessfully')
    c1=conn.cursor()
    #v_sql=("create table login_info (User_Id varchar(10) primary key, Password varchar(10), Mobile_No varchar(15)) ")
    #print(v_sql)
    #c1.execute(v_sql)
    us=input("ENTER YOUR USER ID")
    pa=input("ENTER YOUR PASSWORD")
    mb=input("ENTER YOUR MOBILE NUMBER")
    v_sq=("insert into login_info values('"+us+"','"+pa+"','"+mb+"')")
    print(v_sq)
    c1.execute(v_sq)
    conn.commit()
def quespaper():
    f=open("chemistry ques.csv","r+")
    g=open("comp project.csv","r+")
    h=open("PHYSICS QUES1.csv","r+")
    s=csv.reader(f)
    t=csv.reader(g)
    u=csv.reader(h)
    cl=ml=pl=[]
    for i in s:
        cl.append(i)
    for i in t:
        ml.append(i)
    for i in u:
        pl.append(i)
    chem=random.sample(cl,5)
    math=random.sample(ml,5)
    phy=random.sample(pl,5)
    lst=chem+math+phy
    score=0
    MSG='''WELCOME TO THE PRELIMINARY PARTCIPATION ROUND
    THERE WILL BE 15 MULTIPLE CHOICE QUESTIONS 5 EACH OF ALL SUBJECTS
    EACH QUESTION HAS 4 MARKS AWARDED FOR THE CORRECT ANSWER WITH NO NEGATIVE MARKING
    QUALIFYING MARKS ARE 24 OUT OF 60'''
    print(MSG)
    ch=input("TO START THE EXAM ENTER 'YES':")
    if ch.lower()=="yes":
        for i in lst:
            print(i[0])
            print("1 ",i[1])
            print("2 ",i[2])
            print("3 ",i[3])
            print("4 ",i[4])
            uchoice=int(input("ENTER OPTION NUMBER:"))
            if i[uchoice]==i[5]:
                score=score+4
            else:
                None
    print('''THANK YOU FOR PARTICIPATING IN THE TEST
    YOUR SCORE IS:''',score,''' OUT OF 60''')
    if score>=24:
        print('''CONGRATULATIONS YOU HAVE BEEN QUALIFIED TO REGISTER FOR THE MAINS EXAM
        REGISTRATION NUMBER:''',reg_no)
    else:
        print("YOUR SCORE IS NOT SATISFACTORY TRY AGAIN")
    f.close()
    g.close()
    h.close()
while True:
    msg="Welcome to JEE Registration Form"
    print("=================================")
    print(msg)
    print("=================================")
    print("press '1' to Register")
    print("press '2' to Login")
    print("press '3' to exit")

    choice=int(input("enter your choice:"))
    if choice==1:
        sign_up()
    elif choice ==2:
        conn=sql.connect(host='localhost',user='root',passwd='9999943210',database='jee_main')
        #if conn.is_connected():
          #print('connected sucessfully')
        c1=conn.cursor()
        c1.execute("select * from login_info")
        dat=c1.fetchall()
        user=input("Enter user name:")
        passwd=input("Enter the password:")
        phn_no=input("Enter your registered phone_no:")
        
        reg_no="jee_"+phn_no
        t=0
        for i in dat:
            if i==(user,passwd,phn_no):
                print("YOU HAVE SUCCESSFULLY LOGGED IN")
                print("YOU HAVE TO QUALIFY  A PRELIMINARY TEST TO REGISTER FOR THE ACTUAL EXAM AND ACQUIRE REGISTRATION NUMBER")
                t=1
                
        while t==1:
                     print("====================================================")
                     print("1. TO START THE PRELIMINARY ROUND")
                     print("2.TO REGISTER FOR MAINS OR IF YOU HAVE ALREADY REGISTERED")
                     print("3.TO EXIT")
                     print("====================================================")
                     in_ch=int(input("Enter your choice:"))
                     if in_ch==1:
                         quespaper()
                     elif in_ch==2:
                         ureg_no=input("Enter your registration number:")
                         if reg_no==ureg_no:
                             print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ JEE REGISTARATION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                             while True:
                                 print("========================================================================")
                                 print("1:ADD DETAILS")
                                 print("2:VIEW DETAILS OF RECORD YOU HAVE ENTERED")
                                 print("3:ENTER THE YEAR TO DISPLAY REGISTRATION IN THAT YEAR")
                                 print("4:VIEW NO. OF REGISTRATIONS YEARWISE GRAPHICALLY")
                                 print("5:ENTER THE COURSE TO DISPLAY REGISTRATION OF THAT PARTICULAR COURSE")
                                 print("6:VEIW DATA OF STUDENTS SCOREWISE IN SECONDARY EXAMINATION")
                                 print("7:VIEW NO. OF REGISTRATIONS ACCORDING TO NATIONALITY GRAPHICALLY")
                                 print("8:TO VIEW RECORDS OF STUDENTS STARTING WITH A PARTICULAR CHARACTER")
                                 print("9:TO VIEW THE RECORDS OF MALE(M)/FEMALE(F)")
                                 print("10:TO VIEW DETAILS OF ALL THE STUDENTS IN A PARTICULAR ORDER ASCENDING(A)/DESCENDING(D)")
                                 print("11:TO SEARCH RECORDS OF STUDENTS BORN IN PARTICULAR MONTH")
                                 print("12:TO SEE DIFFERENT COURSES AVAILABE")
                                 print("13:QUIT")
                                 print("========================================================================")
                                 
                              
                                 ch=int(input("Enter the choice:"))
                                 if ch==1:
                                     v_name=input("Enter your name--")
                                     v_f_na=input("Enter you father name--")
                                     v_m_na=input("Enter your mother name--")
                                     v_ea=input("Enter the examination applied--")
                                     v_yr=input("Enter the current year--")
                                     v_gen=input("Enter your gender--")
                                     v_dob=input("Enter your date of birth--")             
                                     v_nat=input("Enter your nationality--")
                                     v_comm=input("Enter your community--")
                                     v_min=input("Do you belong to minority--")
                                     v_add1=input("Enter address line1--")
                                     v_dist=input("Enter your district--")
                                     v_state=input("Enter your state--")
                                     v_pin=input("Enter your pin code--")
                                     v_pho=input("Enter your phone number 1--")
                                     v_mob=input("Enter your phone number 2--")
                                     v_ema=input("Enter your mail ID--")
                                     v_edu=input("Enter your 10th standard marks")
                                     v_aadh=input("Enter your aadhar number--")
                                     v_sql=("insert into regninfo values ('"+v_name+"',"+"'"+v_f_na+"',"+"'"+v_m_na+"','"+v_ea+"',"+v_yr+",'"+v_gen+"','"+v_dob+"','"+v_nat+"','"+v_comm+"','"+v_min+"','"+v_add1+"','"+v_dist+"','"+v_state+"',"+v_pin+","+v_pho+","+v_mob+",'"+v_ema+"',"+v_edu+','+v_aadh+",'"+reg_no+"')")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_sql)
                                     conn.commit()
                                     print("YOU HAVE BEEN REGISTERED")
                                 elif ch==2:
                                     ureg=input("Enter the registartion number:")
                                     v_ch=("select * from regninfo where registration_number='"+ureg+"'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==3:
                                     yea=input("Enter the year")
                                     v_ch=("select * from regninfo where year='"+yea+"'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==4:
                                     
                                     v_ch=("select count(name), year from regninfo group by year")
                                     print(v_ch)
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                     x=[]
                                     y=[]
                                     for i in data:
                                         x.append(i[1])
                                         y.append(i[0])
                                     print(x,y)
                                     plt.plot(x,y,"green")
                                     plt.xlabel("Year ")
                                     plt.ylabel("no. of Registrations")
                                     plt.title("YEARLY DATA")
                                     plt.show()
                                     
                                 elif ch==5:
                                     cor=input("Enter the course")
                                     v_ch=("select * from regninfo where examination_applied='"+cor+"'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==6:
                                     lv=input("Enter the lower limit")
                                     uv=input("enter the upper limit")
                                     v_ch=("select * from regninfo where std10_percentage between'"+lv+"'and'"+uv+"'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==7:
                                     v_ch=("select count(name), nationality from regninfo group by nationality")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                     x=[]
                                     y=[]
                                     for i in data:
                                         x.append(i[1])
                                         y.append(i[0])
                                     print(x,y)
                                     plt.plot(x,y,"red")
                                     plt.xlabel("countries")
                                     plt.ylabel("no. of Registrations")
                                     plt.title(" DATA ON BASIS OF NATIONALITY")
                                     plt.show()
                                 elif ch==8:
                                     charac=input("Enter the first characters of the name")
                                     v_ch=("select * from regninfo where name like'"+charac+"%'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==9:
                                     gen=input("Enter the gender")
                                     v_ch=("select * from regninfo where gender='"+gen+"'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==10:
                                     print("for ascending:asc")
                                     print("for descending:desc")
                                     chh=input("enter your choice")
                                     if chh==asc:
                                         v_ch=("select * from regninfo order by name")
                                         print("================================")
                                         print("COMMAND EXECUTED")
                                         print("================================")
                                         c1.execute(v_ch)
                                         data=c1.fetchall()
                                         print(data)
                                     elif chh==desc:
                                         v_ch=("select * from regninfo order by name desc")
                                         print(v_ch)
                                         c1.execute(v_ch)
                                         data=c1.fetchall()
                                         print(data)
                                 elif ch==11:
                                     mon=input("Enter the month(NUMERICAL):")
                                     v_ch=("select * from regninfo where month(date_of_birth)='"+mon+"'")
                                     print("================================")
                                     print("COMMAND EXECUTED")
                                     print("================================")
                                     c1.execute(v_ch)
                                     data=c1.fetchall()
                                     print(data)
                                 elif ch==12:
                                     print("1:) Btech")
                                     print("2:) BArch")
                                     print("3:)Bplan")
                                 elif ch==13:
                                     print("QUITTING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                     break
                         else:
                             print("THE REGISTERATION NUMBER IS INVALID PLZ TRY AGAIN OR GIVE THE PRELIMINARY TO OBTAIN A REGISTRATION NUMBER")
                     else:
                         break
    elif choice==3:
        break
    else:
        print('''INPUTTED CEDENTIALS ARE EITHER WRONG OR YOU HAVE NOT REGISTERED
        TRY AGAIN OR CREATE YOUR ACCOUNT''')
        
    
