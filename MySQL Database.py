from tabulate import tabulate
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="",database="details")


def insert(name,age,address,contact,email):
    res=con.cursor()
    sql= "insert into data (name,age,address,contact,email) values (%s,%s,%s,%s,%s)"
    user=(name,age,address,contact,email)
    res.execute(sql,user)
    con.commit()
    print("\n")
    print("Record Insert successfully")

def select():
    res=con.cursor()
    sql="SELECT * FROM data"
    res.execute(sql)
    result=res.fetchall()
    print("\n")
    print(tabulate(result,headers=["ID","NAME","AGE","ADDRESS","CONTACT","EMAIL"]))

def update(option):
    if option == 1:
        id = input("Enter Your ID: ")
        name = input("Enter Your Name: ")
        cur=con.cursor()
        sql= "update data set name=%s where id=%s"
        a=(name,id)
        cur.execute(sql,a)
        con.commit()
        select()
        print("\nUpdate Sucessfully")
    elif option == 2:
        id = input("Enter Your ID: ")
        age = input("Enter Your Age: ")
        cur=con.cursor()
        sql= "update data set age=%s where id=%s"
        a= (age,id)
        cur.execute(sql,a)
        con.commit()
        select()
        print("\nUpdate Sucessfully")
    elif option == 3:
        id = input("Enter Your ID: ")
        address = input("Enter Your Address: ")
        cur=con.cursor()
        sql= "update data set address=%s where id=%s"
        a= (address,id)
        cur.execute(sql,a)
        con.commit()
        select()
        print("\nUpdate Sucessfully")
    elif option == 4:
        id = input("Enter Your ID: ")
        contact = input("Enter Your Contact: ")
        cur=con.cursor()
        sql= "update data set contact=%s where id=%s"
        a= (contact,id)
        cur.execute(sql,a)
        con.commit()
        select()
        print("\nUpdate Sucessfully")
    elif option == 5:
        id = input("Enter Your ID: ")
        email = input("Enter Your Email: ")
        cur=con.cursor()
        sql= "update data set email=%s where id=%s"
        a=(email,id)
        cur.execute(sql,a)
        con.commit()
        select()
        print("\n")
        print("update Sucessfully")
    else:
        print("Invalid")

def delete(id):
    res = con.cursor()
    sql = "delete from  date where id=%s"
    user= (id,)
    res.execute(sql, user)
    con.commit()
    print("\nRecord Deleted Sucessfully...!!!")

while True:
    print("\n")
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        age = input("Enter age : ")
        address = input("Enter address : ")
        contact = input("Enter contact : ")
        email = input("Enter email : ")
        insert(name,age,address,contact,email)
    elif choice == 2:
        select()
    elif choice == 3:
        print("1.Name")
        print("2.Age")
        print("3.Address")
        print("4.Contacte")
        print("5.Email")
        option = int(input("\nWhich field you want to update?:"))
        update(option)
    elif choice == 4:
        id = input("Enetr Your ID: ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Option...!!!")

