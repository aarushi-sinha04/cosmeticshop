import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="root0000", database="cosmetics")
cursor=con.cursor()
if con.is_connected==False:
    print("Connection error")
import matplotlib.pyplot as mpt
import csv
import random

# welcome screen
def welcome():
    print(":"*70)
    print()
    print("  #"+" "*15+"#"+"  "+"#"*6+"  "+"#"+" "*7+"#"*6+" "*2+"#"*6+" "*2+"#"+" "*5+"#"+" "*2+"#"*6)
    print("   #"+" "*6+"#"+""+" "*6+"#"+" "*3+"#"+" "*7+"#"+" "*7+"#"+" "*7+"#"+" "*4+"#"+" "*2+"#"+" "+"#"+" "+"#"+" "+"#"+" "*2+"#")
    print("    #"+" "*4+"#"+" "+"#"+" "*4+"#"+" "*4+"#"*3+" "*5+"#"+" "*7+"#"+" "*7+"#"+" "*4+"#"+" "*2+"#"+" "*2+"#"+" "*2+"#"+" "*2+"#"*3)
    print("     #"+" "*2+"#"+" "*3+"#"+" "*2+"#"+" "*5+"#"+" "*7+"#"+" "*7+"#"+" "*7+"#"+" "*4+"#"+" "*2+"#"+" "*5+"#"+" "*2+"#")
    print("      #"+" "*7+"#"+" "*6+"#"*6+"  "+"#"*6+" "*2+"#"*6+" "*2+"#"*6+" "*2+"#"+" "*5+"#"+" "*2+"#"*6)
    print("="*70)
    print()
    print(":"*70)
    print()

# Reads the text file
def read_note(x):
    print()
    file = open(x, 'r')
    oupt = file.readlines()
    for i in oupt:
        print("             "+i)
    file.close()
    print(" ")
    
# Creates the text file
def create_note(x,y):
    print()
    print("Current "+y+" note:")
    read_note(x)
    print("Do you want to \n","1.Append the current "+y+" note\n","2.Make a new "+y+" note")
    k=int(input("Enter option:"))
    if k==1:
        file=open(x,'a+')
        val=int(input("Enter Number of lines you want to enter:"))
        for i in range(0, val):
            inpt = input("Enter line: ")
            inpt = inpt + '\n'
            file.writelines(inpt)
        file.close()
    elif k==2:
        file=open(x,'w')
        val=int(input("Enter Number of lines you want to enter:"))
        for i in range(0, val):
            inpt = input("Enter line: ")
            inpt = inpt + '\n'
            file.writelines(inpt)
        file.close()
    else:
        print("Wrong option")
        create_note(x,y)
    print(" ")
    print("The new "+y+" note:")
    read_note(x)

# Customer Login
def opt1():
    print()
    print("Please enter your login credentials:")
    opt1.C_name=input(" Name:")
    opt1.C_ID=input(" ID:")
    C_psswd=input(" Password:")
    f="select * from customer where CustomerID={} and name='{}' and psswd='{}'".format(opt1.C_ID,opt1.C_name,C_psswd)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    while count==0:
        print("Invalid name or ID or password ")
        print()
        print("Please enter your login credentials:")
        opt1.C_name=input(" Name:")
        opt1.C_ID=input("User ID:")
        C_psswd=input(" Password:")
        f="select * from customer where CustomerID={} and name='{}' and psswd='{}'".format(opt1.C_ID,opt1.C_name,C_psswd)
        cursor.execute(f)
        data=cursor.fetchall()
        count=cursor.rowcount
    else:
        print()
        print("Logged in successfully")
        print()
          
# Create Customer ID
def opt2():
    print()
    print("Please fill the following details:")
    C_newname=input(" Name:")
    C_newID=input(" User ID:")
    C_psswd=input(" Password (maximum 20 characters):")
    f="select CustomerID from customer where CustomerID={}".format(C_newID)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    if count==0:
        e="insert into customer(CustomerID ,name,psswd,times_bought) values ({},'{}','{}',0)".format(C_newID,C_newname,C_psswd)
        cursor.execute(e)
        con.commit()
        print("User ID created successfully!!!")
        print()
    else:
        while count!=0:
            print()
            print("This User ID is already taken, please enter a new User ID")
            print()
            C_newID=input(" User ID:")
            f="select CustomerID from customer where CustomerID={}".format(C_newID)
            cursor.execute(f)
            data=cursor.fetchall()
            count=cursor.rowcount
        if count==0:
            e="insert into customer(CustomerID ,name,psswd,times_bought) values ({},'{}','{}',0)".format(C_newID,C_newname,C_psswd)
            cursor.execute(e)
            con.commit()
            print("User ID created successfully!!!")
            print()
            
# Admin Login
def opt3():
    print()
    print("Please enter your login credentials:")
    A_name=input(" Admin Name:")
    A_ID=input(" Admin ID:")
    A_psswd=input(" Password:")
    f="select * from admin where adminID={} and name='{}' and psswd='{}'".format(A_ID,A_name,A_psswd)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    while count==0:
        print("Invalid login credentials ")
        print()
        print("Please re-enter your login credentials:")
        A_name=input(" Name:")
        A_ID=input(" Admin user ID:")
        A_psswd=input(" Password:")
        f="select * from admin where adminID={} and name='{}' and psswd='{}'".format(A_ID,A_name,A_psswd)
        cursor.execute(f)
        data=cursor.fetchall()
        count=cursor.rowcount
    else:
        print()
        print("Logged in successfully!!")
        print()
        
# Create Admin ID
def opt4():
    print()
    print("Please fill up the following:")
    A_newname=input(" Admin Name:")
    A_psswd=input(" Password (maximum 20 characters):")
    A_newID=random.randint(1000,9000)
    f="select adminID from admin where adminID={}".format(A_newID)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    if count==0:
        print(" Your ID is :",A_newID)
        e="insert into admin(adminID ,name,psswd) values ({},'{}','{}')".format(A_newID,A_newname,A_psswd)
        cursor.execute(e)
        con.commit()
        print("ID created successfully!!!")
    else:
        while count!=0:
            A_newID=random.randint(1000,9000)
            f="select adminID from admin where adminID={}".format(A_newID)
            cursor.execute(f)
            data=cursor.fetchall()
            count=cursor.rowcount
        if count==0:
            print(" Your ID is :",A_newID)
            e="insert into admin(adminID ,name,psswd) values ({},'{}','{}')".format(A_newID,A_newname,A_psswd)
            cursor.execute(e)
            con.commit()
            print("ID created successfully!!!")
            print()        


def alter():
    c=input("Do you want to alter anything else?(yes/no) ")
    if c=='yes' or c=='Yes':
        print()
        print("What do you want to do?\n","1.Alter catalogue\n","2.Alter table\n","3.Alter Product table\n")
        l=int(input("Please select an option from above:"))
        if l==1:
            alter_catalogue()
        elif l==2:
            alter_table()
        elif l==3:
            alter_product()
        else:
            print("Invalid option , Please choose an option from above")
    else:
        print("Ok, Thank you")
        
# shows the catalogue
def show_catalogue():
    print()
    print("(SNO,CATALOGUE)")
    cursor.execute("select * from Catalogue")
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)
    print()

# alters the catalogue
def alter_catalogue():
    print()
    print("What do you want to do?\n","1.Insert\n","2.Update\n","3.Delete")
    q=int(input("Enter what you want to do:"))
    print()
    print("The current Catalogue is :")
    show_catalogue()
    print()
    if q==1:
        sno=int(input("Enter the new serial number:"))
        cataloguename=input("Enter the new catalogue name:")
        print()
        print("The new Catalogue is :")
        e="insert into Catalogue(SNo ,Catalogue) values ({},'{}')".format(sno,cataloguename)
        cursor.execute(e)
        con.commit()
        show_catalogue()
        f="create table {}(SNo integer primary key,Name varchar(20))".format(cataloguename)
        cursor.execute(f)
        con.commit()
        
    elif q==2:
        sno=int(input("Enter serial number:"))
        cataloguenameold=input("Enter the old catalogue name:")
        cataloguename=input("Enter the new catalogue name:")
        print()
        print("The new Catalogue is :")
        e="update Catalogue set Catalogue='{}' where SNo={}".format(cataloguename,sno)
        cursor.execute(e)
        con.commit()
        show_catalogue()
        f="alter table {} rename to {}".format(cataloguenameold,cataloguename)
        cursor.execute(f)
        con.commit()
    elif q==3:
        sno=int(input("Enter serial number:"))
        cataloguename=input("Enter the catalogue name:")
        print()
        print("The new Catalogue is :")
        d="delete from Catalogue where SNO={}".format(sno)
        cursor.execute(d)
        con.commit()
        show_catalogue()
        k="drop table {}".format(cataloguename)
        cursor.execute(k)
        con.commit()
    else:
        print("Please choose an option from above:")
    alter()
    
# shows the categories table
def show_table():
    print()
    print("#######",alter_table.N,"#######")
    print()
    print("(SNO , NAME)")
    f="select * from {} ".format(alter_table.N)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)
    print()
    
# alter the categories
def alter_table():
    show_catalogue()
    print("Which table you want to alter?")
    k=input("Enter serial number:")
    alter_table.N=input("Enter the name:")
    show_table()
    print()
    print("What do you want to do?\n","1.Insert\n","2.Update\n","3.Delete")
    q=int(input("Enter option:"))
    print()
    print("The  current Table is :")
    show_table()
    print()
    if q==1:
        sno=int(input("Enter new serial number:"))
        name=input("Enter the new name:")
        print()
        print("The new Table is :")
        e="insert into {}(SNo ,Name) values ({},'{}')".format(alter_table.N,sno,name)
        cursor.execute(e)
        con.commit()
        show_table()
        f="create table {}(ItemID varchar(10) primary key, Name varchar(20),Brand varchar(20) , Cost integer, manudate varchar(20), expdate varchar(20))".format(name)
        cursor.execute(f)
        con.commit()
        
    elif q==2:
        sno=int(input("Enter serial number:"))
        nameold=input("Enter the old  name:")
        namenew=input("Enter the new catalogue name:")
        print()
        print("The new Table is :")
        e="update {} set Name='{}' where SNo={}".format(alter_table.N,namenew,sno)
        cursor.execute(e)
        con.commit()
        show_table()
        f="alter table {} rename to {}".format(nameold,namenew)
        cursor.execute(f)
        con.commit()
    elif q==3:
        sno=int(input("Enter serial number:"))
        name=input("Enter the catalogue name:")
        print()
        print("The new Table is :")
        d="delete from {} where SNO={}".format(alter_table.N,sno)
        cursor.execute(d)
        con.commit()
        show_table()
        k="drop table {}".format(name)
        cursor.execute(k)
        con.commit()
    else:
        print("Please choose an option from above:")
    alter()
    
# shows the product details 
def show_product():
    print()
    print("####################",alter_product.N,"####################")
    print()
    print("(ItemID ,       NAME       ,     BRAND  , COST , MANUDATE , EXPDATE)")
    f="select * from {} ".format(alter_product.N)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)
    print()

# alter the product table
def alter_product():
    show_catalogue()
    alter_table.N=input("Enter the name of the catalogue you want to alter:")
    show_table()
    alter_product.S=int(input("Enter serial number:"))
    alter_product.N=input("Enter product type:")
    show_product()
    print()
    print("What do you want to do?\n","1.Insert\n","2.Update\n","3.Delete\n")
    l=int(input("Select an option from above:"))
    print()
    print("The current product table is:")
    show_product()
    print()
    if l==1:
        p_ID=input("Enter ItemID:")
        p_name=input("Enter the Name:")
        p_brand=input("Enter the brand name:")
        p_cost=int(input("Enter the cost:"))
        p_mdate=input("Enter the Manufacturing Date:")
        p_edate=input("Enter the Expiry Date:")
        print()
        print("The new table is :")
        e="insert into {}(ItemID,Name,Brand,Cost,manudate,expdate) values ('{}','{}','{}',{},'{}','{}')".format(alter_product.N,p_ID,p_name,p_brand,p_cost,p_mdate,p_edate)
        cursor.execute(e)
        con.commit()
        show_product()
        f="insert into product(ItemID,Name,Quantity_bought,no_of_review) values ('{}','{}',0,0)".format(p_ID,p_name)
        cursor.execute(f)
        con.commit()
        
    elif l==2:
        print()
        y=input("Enter the ID of the item you want to update:")
        print()
        print("ItemID\n","Name\n","Brand\n","Cost\n","Manudate\n","Expdate\n")
        x=input("What do you want to update?")
        z=input("Enter the new "+x+":")
        print()
        print("The new Table is :")
        e="update {} set {}='{}' where ItemID='{}'".format(alter_product.N,x,z,y)
        cursor.execute(e)
        con.commit()
        show_product()
        if x=='ItemID' or x=='Name' or x=='name':
            f="update product set {}='{}' where ItemID='{}'".format(x,z,y)
            cursor.execute(f)
            con.commit()
        else:
            print()
        
    elif l==3:
        print()
        y=input("Enter the ID of the item you want to delete:")
        print()
        print("The new table is :")
        d="delete from {} where ItemID='{}'".format(alter_product.N,y)
        cursor.execute(d)
        con.commit()
        show_product()
        g="delete from product where ItemID='{}'".format(y)
        cursor.execute(g)
        con.commit()
    else:
        print("Invalid input\n","Please choose an option from above")
    alter()
    
# stacks the details of all the products bought
Stack=[]
def isempty(stack):
    if stack==[]:
        return True
    else:
        return False
def Push(stack,item):
    stack.append(item)
    top=len(stack)-1
def Display(stack):
    if isempty(stack):
        print ('Stack empty')
    else:
        top=len(stack)-1
        print(stack[top])
        for a in range(top-1,-1,-1):
            print(stack[a])
            
# alters/adds the address of customers
class address:
    def add_address(self):
        print()
        k=input("Please enter your address:")
        e="update customer set address='{}' where CustomerID={}".format(k,opt1.C_ID)
        cursor.execute(e)
        con.commit()
    def check_address_exist(self):
        mn="select address FROM customer where customerID={}".format(opt1.C_ID)
        cursor.execute(mn)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            l=str(row[0])
        if l=='None':
            print("You have not registered your address")
            self.add_address()
        else:
            print()
            print("           ADDRESS")
            print(l)
            print()
            print(" 1.Use this address\n","2.Create new address\n")
            s=int(input("Enter option:"))
            if s==1:
                print()
            elif s==2:
                self.add_address()
    def view_address(self):
        print()
        print("           ADDRESS")
        mn="select address FROM customer where customerID={}".format(opt1.C_ID)
        cursor.execute(mn)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
list=[]


def buy():
    print()
    print("###### Catalogue ######")
    show_catalogue()
    print()
    alter_table.N=input("Enter the product category name:")
    show_table()
    alter_product.N=input("Enter  product type description:")
    print()
    print("List of available products")
    show_product()
    print("What do you want to buy?")
    buy.l=input("Enter the ItemID:")
    print()
    print("These are the details of the product")
    print("(ItemID , NAME , BRAND , COST , MANUDATE , EXPDATE)")
    f="select * from {} where ItemID='{}'".format(alter_product.N,buy.l)
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)   
    print()
    j=int(input("Enter quantity:"))
    jj=str(row)+" Quantity="+str(j)
    s=input("Do you want to view the review of this product?(yes/no)")
    if s=='yes':
        print()
        g="select no_of_review from product where ItemID='{}'".format(buy.l)
        cursor.execute(g)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            qty=int(row[0])
        if qty==0:
            print("No reviews")
        else:
            print("These are the reviews")
            r=review()
            r.view_review_one()
    elif s=='no':
        print()
    print()
    b=input("order confirm?(yes/no)")
    print()
    if b=='yes' or b=='YES':
        print("Order confirmed!!")
        Push(Stack,jj)
        
        # for piechart of popular products
        g="select Quantity_bought from product where ItemID='{}'".format(buy.l)
        cursor.execute(g)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            qty=int(row[0])
        c=qty+j
        f="update product set Quantity_bought='{}' where ItemID='{}'".format(c,buy.l)
        cursor.execute(f)
        con.commit()
        
        # total cost append in list
        m="select cost from {} where ItemID='{}'".format(alter_product.N,buy.l)
        cursor.execute(m)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            cost=float(row[0])
            z=cost*j
            list.append(z)
        print()
        
        # edits in the csv file of buying details of customers
        f="select ItemID,Name,Brand from {} where ItemID='{}'".format(alter_product.N,buy.l)
        cursor.execute(f)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            xyz=row
        with open("buyingdetails.csv","a",newline='') as f1:
            infile=csv.writer(f1)
            infile.writerow([opt1.C_ID,opt1.C_name,xyz,j,z])
        z=input("Do you want to buy anything else?(yes\ no)")
        if z=='yes' or z=='YES':
            buy()
        elif z=='no' or z=='NO':
            print("Your total order ")
            print("(ItemID , NAME , BRAND , COST , MANUDATE , EXPDATE)")
            Display(Stack)
            print()
            print("Your total cost:",sum(list))
            h="select times_bought from customer where CustomerID='{}'".format(opt1.C_ID)
            cursor.execute(h)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                t=int(row[0])
            if t==0:
                print()
                print("As this is your first order, you get 15% discount!!")
                a=sum(list)
                d=(15*a)/100
                tc=a-d
                print("Total payable amount:",tc)
                print()
            else:
                print()
            k=t+1
            p="update customer set times_bought='{}' where CustomerID='{}'".format(k,opt1.C_ID)
            cursor.execute(p)
            con.commit()
            
            #address of customer
            a=address()
            a.check_address_exist()
            a.view_address()
            mk=0
            while mk==0:
                lll=input("Address confirm?(yes/no)")
                if lll=='yes':
                    print("Items will be delivered to this address")
                    mk=1
                else:
                    a.check_address_exist()
            print()
            print("Order confirmed!!")
            print()
            print("Your order will be delivered to you within 8-9 days")
            print()
    elif b=='no' or b=='NO':
        print("Ok, taking you back to start options")
        buy()
        
# asks if the customer wants to do something else
def anythingelse():
    print()
    gh=input("Do you want to do anything else? (yes/no)")
    if gh=='yes':
        print()
        customer()
    else:
        read_note('ThankYounote.txt')
        
# shows the piechart of the popular products bought
def popular():
    h=[]
    j="select Quantity_bought from product"
    cursor.execute(j)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        u=int(row[0])
        h.append(u)
    k=[]
    o="select itemid,name from product"
    cursor.execute(o)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        u=str(row[0]+","+row[1])
        k.append(u)
    col=['black','']
    mpt.pie(h, labels=k,autopct="%1.1f%%")
    mpt.title("Popular products")
    mpt.show()
    
# edits in the csv for storing the record of things bought    
def create_buying_details():
    with open("buyingdetails.csv","w",newline='') as f1:
        infile=csv.writer(f1)
        infile.writerow(["C_ID","[-Name-]","[-----Product bought-----]","Quantity","Total Cost"])
    f1.close()     
def buying_details_exist():
    with open("buyingdetails.csv","a",newline='') as f1:
        with open("buyingdetails.csv","r") as f1:
            outfile=csv.reader(f1)
            a=0
            for row in outfile:
                a=1
            if a==0:
                create_buying_details()
            else:
                print()          
def buying_details():
    with open("buyingdetails.csv","r") as f1:
        outfile=csv.reader(f1)
        for row in outfile:
            print(row)
            
# adds reviews of customers 
class review:
    def product_bought_review(self):
        with open("buyingdetails.csv","r",newline='') as f1:
            infile=csv.reader(f1)
            print("These are the products purchased by you")
            print("(ItemID , NAME , BRAND )")
            for row in infile:
                if row[0]==opt1.C_ID:
                    print(row[2])
            self.add_review()
    def check_exist(self):
        with open("buyingdetails.csv","r",newline='') as f1:
            infile=csv.reader(f1)
            print()
            k=1
            for row in infile:
                if row[0]==opt1.C_ID:
                    k=0
            if k==1:
                print("You have not purchased anything")
            else:
                self.product_bought_review()
    def add_review(self):
        print()
        l=input("Enter the ID of the product:")
        k=input("Enter the name of the product:")
        m=input("Enter the review:")
        ee="select max(sno) FROM review"
        cursor.execute(ee)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            cc=int(row[0])
        ccc=cc+1
        e="insert into review(sno,ItemID,name,review) values ({},'{}','{}','{}')".format(ccc,l,k,m)
        cursor.execute(e)
        con.commit()
        g="select no_of_review from product where ItemID='{}'".format(l)
        cursor.execute(g)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            qty=int(row[0])
        c=qty+1
        o="update product set no_of_review='{}' where ItemID='{}'".format(c,l)
        cursor.execute(o)
        con.commit()
    def view_review_all(self):
        print()
        print("Sno | ItemID | Name    | Review")
        f="select * from review"
        cursor.execute(f)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
    def view_review_one(self):
        print()
        f="select review from review where ItemID='{}'".format(buy.l)
        cursor.execute(f)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
            
# shows admin the record of all the products
def details_product_tilldate():
    print()
    print("(ItemID |      Name      |Qty bought| no. of Reviews)")
    f="select * from product"
    cursor.execute(f)
    data=cursor.fetchall()
    count=cursor.rowcount
    for row in data:
        print(row)
        
# asks if the customer wants to make anychanges in his details
def change_info():
    print("What do you want to change?\n","1.Name\n","2.Password\n","3.Address\n")
    np=int(input("Enter option:"))
    if np==1:
        o=input("Enter new name:")
        l="update customer set name='{}' where CustomerID={}".format(o,opt1.C_ID)
        cursor.execute(l)
        con.commit()
    elif np==2:
        h=input("Enter current password:")
        f="select * from customer where CustomerID={} and psswd='{}'".format(opt1.C_ID,h)
        cursor.execute(f)
        data=cursor.fetchall()
        count=cursor.rowcount
        while count==0:
            print(" Incorrect Password ")
            print()
            h=input(" Please re-enter your Password:")
            f="select * from customer where CustomerID={} and psswd='{}'".format(opt1.C_ID,h)
            cursor.execute(f)
            data=cursor.fetchall()
            count=cursor.rowcount
        else:
            o=input("Enter new password:")
            l="update customer set Psswd='{}' where CustomerID={}".format(o,opt1.C_ID)
            cursor.execute(l)
            con.commit()
            print("Password changed successfully")
    elif np==3:
        print("Current address:")
        a=address()
        a.check_address_exist()
        print("Your address is:")
        print()
        a.view_address()
    else:
        print("Invalid option")
        change_info()
        
# for returning products
class return_order():
    def product_bought(self):
        with open("buyingdetails.csv","r",newline='') as f1:
            infile=csv.reader(f1)
            print("These are the items purchased by you")
            print("(ItemID , NAME , BRAND )")
            for row in infile:
                if row[0]==opt1.C_ID:
                    print(row[2])
            self.return_item()
    def check_exist(self):
        with open("buyingdetails.csv","r",newline='') as f1:
            infile=csv.reader(f1)
            print()
            k=1
            for row in infile:
                if row[0]==opt1.C_ID:
                    k=0
            if k==1:
                print("You have not purchased anything")
            else:
                self.product_bought()
    def return_item(self):
        print()
        print("Please enter the details of the item which you want to return")
        l=input("ID:")
        k=input("Name:")
        m=input("Why do you want to return it?")
        print("---We will come to take the item within 7 days---")
        
# prints options for customer (customer menu)
def customer():
    print("Please select the desired option\n","1.Purchase item\n","2.Modify your personal information\n",
              "3.Add/modify shipping address\n","4.Pie chart of popular products in demand\n",
              "5.Add product review\n","6.Return order\n","7.Exit\n")
    l=int(input("Enter:"))
    if l==1:
        buying_details_exist()
        buy()
        anythingelse()
    elif l==2:
        print()
        change_info()
        anythingelse()
    elif l==3:
        print("Current address:")
        a=address()
        a.check_address_exist()
        print("Your address is:")
        print()
        a.view_address()
        anythingelse()
    elif l==4:
        popular()
        anythingelse()
    elif l==5:
        r=review()
        r.check_exist()
        anythingelse()
    elif l==6:
        r=return_order()
        r.check_exist()
        anythingelse()
    elif l==7:
        print()
        print()
        start()
    else:
        print("invalid option")
        customer()
        
# prints options for admin (admin menu)
def admin():
    print()
    print("What do you want to do?\n","1.Alter Product Main Catalogue\n","2.Alter Category Table\n","3.Alter Product details\n",
              "4.Edit the Welcome note\n","5.Edit the Thank You note\n","6.View the purchasing details\n",
          "7.View reviews\n","8.Details of product bought till date\n","9.Exit")
    l=int(input("Please select an option from above:"))
    if l==1:
        print()
        alter_catalogue()
        admin()
    elif l==2:
        print()
        alter_table()
        admin()
    elif l==3:
        print()
        alter_product()
        admin()
    elif l==4:
        print()
        create_note('welcomenote.txt','welcome')
        admin()
    elif l==5:
        print()
        create_note('ThankYounote.txt','Thank You')
        admin()
    elif l==6:
        print()
        buying_details()
        admin()
    elif l==7 :
        print()
        r=review()
        r.view_review_all()
        admin()
    elif l==8:
        print()
        details_product_tilldate()
        admin()
    elif l==9:
        print()
        print()
        start()
    else:
        print()
        print("Invalid , Please choose an option from above")
        admin()
        
# start menu
def start():
    print(" 1.Customer Login \n","2.Create Customer ID \n","3.Admin Login \n","4.Create Admin ID \n","5.Exit\n")
    l=int(input("Please select your desired option:"))
    if l==1 :
        opt1()
        a=1
    elif l==2 :
        opt2()
        m=input("Do you want to login?(yes/no)")
        if m=='yes' or m=='Yes':
            opt1()
            a=1
        else:
            read_note('ThankYounote.txt')
    elif l==3:
        opt3()
        a=2
    elif l==4:
        opt4()
        print()
        m=input("Do you want to login?(yes/no)")
        if m=='yes'or m=='Yes':
            opt3()
            a=2
        elif m=='no' or m=='No':
            a=3
            read_note('ThankYounote.txt')
    elif l==5:
        print("Thank you!")
        a=0
    else:
        print("Please choose from the options given above")
    if a==1:
        customer() 
    elif a==2:
        admin()
    elif a==0:
        exit()
welcome()
read_note('welcomenote.txt')        
start()
#/usr/local/mysql/bin/mysql -u root -p



"""makeup,skincare,hair,fragrance,bath and body,nail products"""