import mysql.connector as sql , random , datetime as dt
import matplotlib.pyplot as plt
conn=sql.connect(host='localhost',user='User',passwd='Your Pass',database='Your database')
A = 0
if conn.is_connected() and A == 0:
    print("Successfully connected")
    A += 1

def presence():
    l = []
    info10="select * from Transaction;"
    c1.execute(info10)
    data3=c1.fetchall()
    for row in data3:
        l.append(row[0])
    if accountno in l:
        return False
    return True

def presence2():
    l = []
    info10="select * from newuser;"
    c1.execute(info10)
    data3=c1.fetchall()
    for row in data3:
        l.append(row[0])
    if use in l:
        return True
    return False

def presence1():
    l = []
    info10="select * from addnewcustomer;"
    c1.execute(info10)
    data3=c1.fetchall()
    for row in data3:
        l.append(row[0])
    if accountno in l:
        return True
    return False

def check_date():
    curt = (str(toda.strftime("%m")),str(toda.strftime("%Y")))
    l = []
    for i in data3:
        l.append((i[2].split('-')[1],i[2].split('-')[0]))
    if curt in l:
        return True
    return False
        

def pytm():
    unit=random.randint(0,101)
    print('Dear customer, you have used ',unit,'units of electricity.')
    print('One unit of curent is 150 ruppees')
    amount=150*unit
    deadline=dt.date(2022,11,30)
    if deadline<toda:
        fine=(int(toda.strftime("%d"))-int(deadline.strftime("%d")))*30
        totamt=amount+fine
        print('You have dealyed for ',toda-deadline,'days.The fine per day is 30 rupees.')
        GST=(15/100)*totamt
        totalamt=totamt+GST
        print('Pleae payup ',totalamt,'rupees inclding GST')
        p=input("Please Enter YES to transact")
        if p in ["YES","Yes","yes"]:
            print("Transaction successful")
            print("You have paid the bill")
            info3="insert into Transaction values({},{},'{}',{},{},{},'{}')".format(accountno,unit,toda,totamt,GST,totalamt,p)
            c1.execute(info3)
            conn.commit()
        elif p in ["NO","No","no"]:
            print('plz pay the bill sooner')
        else:
            print("Enter valid command!!")
    else:
        totamt=0
        GST=(15/100)*amount
        totalamt=amount+GST
        print('Please payup ',totalamt,'rupees inclding GST')
        p=input("Please Enter YES to transact")
        if p=="YES":
            print("Transaction successful")
            print("You have paid the bill")
        else:
            print('plz pay the bill sooner')
            info3="insert into Transaction values({},{},'{}',{},{},{},'{}')".format(accountno,unit,toda,totamt,GST,totalamt,p)
            c1.execute(info3)
            conn.commit()
    


c='YES' or "yes" or 'Yes'
V='YES' or "yes" or 'Yes'
c1=conn.cursor() 
while c=='YES' or "yes" or 'Yes':
    print('************************WELCOME TO ELECTRICITY BILLING SYSTEM************************')
    print(dt.datetime.now())
    print('1.NEW USER')
    print('2.EXISTING USER')
    print('3.DELETE USER')
    print('4.EXIT')
    choice1=int(input('ENTER YOUR CHOICE:'))
    if choice1==1:
        username=input("Enter your username :")
        password=input("Enter your password:")
        confirmpasswd=input("Confirm  your password:")
        if password==confirmpasswd:
            info1="insert into newuser values('{}','{}','{}')".format(username,password,confirmpasswd)
            c1.execute(info1)
            conn.commit()
            c=input("do you want to continue?(yes or no)")
        else:
            print('Your confirm password is incorrect')
            print('Try again')
            c=input("do you want to continue?(yes or no)")
    elif choice1==2:
        username=input('Enter your username :')
        password=input('Enter your password :')
        info2="select * from newuser where username='{}' and password='{}'".format(username,password)
        c1.execute(info2)
        data=c1.fetchall()
        while V=='YES' or "yes" or 'Yes':
            if any(data):
                print('************************WELCOME TO ELECTRICITY BILLING SYSTEM************************')
                print("1.ACCOUNT SETTINGS")
                print("2.TRANSACTION")
                print("3.VIEW CUSTOMER DETAILS")
                print("4.GRAPHICAL REPRESENTATION")
                print('5.EXIT')
                choice2=int(input('ENTER YOUR CHOICE :'))
                if choice2==1:
                    print('1.NEW CUSTOMER')
                    print('2.DELETE EXISTING ACCOUNT')
                    choice12=int(input('ENTER YOUR CHOICE :'))
                    if choice12==1:
                        accountno=random.randrange(1000000,9999999,10)
                        print("Your accountno is",accountno)
                        boxid=input("Enter your mete box ID  :")
                        bankname=input('Enter your BANK NAME  :')
                        bankbranch=input('Enter your BANK BRANCH  :')
                        name=input('Enter your name  :')
                        address=input('Enter your address  :')
                        areacode=int(input('Enter your area PIN CODE  :'))
                        phoneno=int(input('Enter your PHONE NUMBER  :'))
                        email=input('Enter your email  :')
                        info2="insert into AddNewCustomer values({},'{}','{}','{}','{}',{},{},'{}','{}')".format(accountno,bankname,bankbranch,name,address,areacode,phoneno,email,boxid)
                        c1.execute(info2)
                        conn.commit()
                        V=input("Do you want to continue?(yes or no)")
                        if V=='yes':
                            continue
                        else:
                            break
                    elif choice12==2:
                        acc=input("ENTER YOUR ACCOUNT NUMBER :")
                        info6=c1.execute("delete from Transaction where accountno='{}'".format(acc))
                        info7=c1.execute("delete from addnewcustomer where accountno='{}'".format(acc))
                        c1.execute(info6)
                        c1.execute(info7)
                        conn.commit()
                        print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY DELETED")
                        V=input("Do you want to continue?(yes or no)")
                        if V=='yes':
                            continue
                        else:
                            break
                    
                elif choice2==2:
                    accountno=int(input('Enter your account number  :'))
                    toda=dt.date.today()
                    if presence1():
                        if presence():
                            pytm()
                        else:
                            info10="select * from Transaction where accountno="+str(accountno)
                            c1.execute(info10)
                            data3=c1.fetchall()
                            for row in data3:
                                paid=row[6]
                            if paid=='yes' and check_date():
                                print('You have already paid the bill')
                                break
                            elif paid == 'yes' and check_date() == False:
                                pytm()
                                
                            else:
                                V=input("Do you want to continue?(yes or no)")
                                if V=='yes':
                                    continue
                                else:
                                    break
                    else:
                        print("Enter valid Account No. !!")
                        
                elif choice2==3:
                    accountno=int(input('Enter your account number  :'))
                    info4="select * from AddNewCustomer where accountno=" + str(accountno)
                    c1.execute(info4)
                    data1=c1.fetchall()
                    for row in data1:
                        print(" Account Number: ", row[0])
                        print("Bankname:",row[1])
                        print("Bankbranch:",row[2])
                        print("Person name:",row[3])
                        print("Your meter device ID=",row[8])
                        print("Residential address:",row[4])
                        print("Area code:",row[5])
                        print("Phone number:",row[6])
                        print("Email:",row[7])
                        info5="select * from Transaction where accountno=" + str(accountno)
                        c1.execute(info5)
                        data2=c1.fetchall()
                    for row in data2:
                        print("Unit : ",row[1])
                        print("paid on:",row[2])
                        print("Amount to be paid without GST:",row[3])
                        print("GST=",row[4])
                        print("Amount to be paid including GST:",row[5])
                    V=input("Do you want to continue?(yes or no)")
                    if V=='yes':
                        continue
                    else:
                        break
                elif choice2==4:
                    info9="select accountno,totalamt from Transaction"
                    c1.execute(info9)
                    L1,L2,=[],[]
                    for i in c1.fetchall():
                        L1.append(i[0])
                        L2.append(i[1])
                    plt.plot(L1,L2)
                    plt.title("GRAPH")
                    plt.show()
                    V=input("Do you want to continue?(yes or no)")
                    if V=='yes':
                        continue
                    else:
                        break
                elif choice2==5:
                    print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!")
                    break
                    c='yes'
                else:
                    print("Enter Valid Choice!")

          
            else:
                print('Username / password is incorrect')
                break
                c=input("Do you want to try again?(yes or no)")
            
                    
        else:
            print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!")
            V='no'
            
    

    elif choice1==3:
        use=input("ENTER YOUR USERNAME:")
        if presence2():
            info8=c1.execute("delete from newuser where username='{}'".format(use))
            c1.execute(info8)
            print(f"THANK YOU FOR USING OUR SOFTWARE,USER #{use}# IS SUCCESSFULLY DELETED")
            conn.commit()
        else:
            print("Entered Username doesn't exist!!")
            print("Please enter an authorised user...")
        V=input("Do you want to continue?(yes or no)")
        
    elif choice1==4:
        print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!")
        c='no'
        break
    else:
        print("Invalid choice!!")
        c=input("Do you want to try again?(yes or no)")
else:
    print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!")
    
    c='no'
    
