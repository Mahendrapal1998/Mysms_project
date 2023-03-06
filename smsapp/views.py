from django.shortcuts import render, redirect
from django.http import HttpResponse
import mysql.connector as mysql
import datetime


def home(req):
    return render(req, 'home.html')


def login(req):
    return render(req, 'login.html')


def reg(req):
    return render(req, 'reg.html')


def desk(req):
    return render(req, 'index.html')


def insert(req):
    return render(req, 'insert.html')


def regTask(req):
    user = req.GET.get('user')
    name = req.GET.get('name')
    fname = req.GET.get('fname')
    email = req.GET.get('email')
    gender = req.GET.get('gender')
    moblie = req.GET.get('mobile')
    password = req.GET.get('pass')
    if user == "Admin":
        con = mysql.connect(host="localhost", user="root",
                            password="Ranaji1", database="sms")
        cr = con.cursor()
        sql = "insert into admin(name,fname,email,gender,moblie,password) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            name, fname, email, gender, moblie, password)
        cr.execute(sql)
        con.commit()
        con.close()
        return redirect("/login")
    elif user == "Employee":
        con = mysql.connect(host="localhost", user="root",
                            password="Ranaji1", database="sms")
        cr = con.cursor()
        sql = "insert into employee(name,fname,email,gender,moblie,password) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            name, fname, email, gender, moblie, password)
        cr.execute(sql)
        con.commit()
        con.close()
        return redirect("/login")
    elif user == "Customer":
        con = mysql.connect(host="localhost", user="root",
                            password="Ranaji1", database="sms")
        cr = con.cursor()
        sql = "insert into customer(name,fname,email,gender,moblie,password) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            name, fname, email, gender, moblie, password)
        cr.execute(sql)
        con.commit()
        con.close()
        return redirect("/login")
    else:
        return HttpResponse("Please Chosse a User Type")


def loginTask(req):
    user = req.GET.get('user')
    email = req.GET.get('email')
    password = req.GET.get('pass')
    if user ==  "Admin":
        con = mysql.connect(host="localhost", user="root",
                            password="Ranaji1", database="sms")
        cr = con.cursor()
        sql = "select * from admin where email='{0}' and password='{1}'".format(
            email, password)
        cr.execute(sql)
        rec = cr.fetchall()
        sql1 = "select count(id) from customer"
        cr.execute(sql1)
        cust = cr.fetchall()
        con.commit
        sql2 = "select count(id) from employee"
        cr.execute(sql2)
        emp = cr.fetchall()
        con.commit
        sql3 = "select count(id) from product"
        cr.execute(sql3)
        pro = cr.fetchall()
        con.commit
        sql4 = "select count(id) from sells"
        cr.execute(sql4)
        sell = cr.fetchall()
        con.commit
        con.close()
        if rec == []:
            return HttpResponse("NO DATA")
        else:
            global rec1,cust1,emp1,sell1,pro1
            cust1 = cust
            emp1 = emp
            pro1 = pro
            sell1 = sell
            rec1= rec
            
            return render(req, 'admin.html',{'detail': rec1, 'custn': cust1,'empn':emp1 ,'pron':pro1, 'selln':sell})
    elif user == "Employee":
        con = mysql.connect(host="localhost", user="root",
                            password="Ranaji1", database="sms")
        cr = con.cursor()
        sql = "select * from employee where email='{0}' and password='{1}'".format(
            email, password)
        cr.execute(sql)
        rec = cr.fetchall()
        con.close()
        if rec == []:
            return HttpResponse("NO DATA")
        else:
            global rec11
            rec11 = rec
            return HttpResponse("welcome employee")
    elif user == "Customer":
        con = mysql.connect(host="localhost", user="root",
                            password="Ranaji1", database="sms")
        cr = con.cursor()
        sql = "select * from customer where email='{0}' and password='{1}'".format(
            email, password)
        cr.execute(sql)
        rec = cr.fetchall()
        con.close()
        if rec == []:
            return HttpResponse("NO DATA")
        else:
            global rec12
            rec12 = rec
            return redirect("/desk")
    else:
        return HttpResponse("Please Chosse a User Type")


def desk(req):
    global rec0
    rec0 = rec12
    return render(req, 'desk.html', {"product": rec0})


def logoutu(req):
    rec0.clear()
    return redirect('/login')


def logouta(req):
    rec1.clear()
    return redirect('/login')


def insertTask(req):
    name = req.GET.get('name')
    brand = req.GET.get('brand')
    price = req.GET.get('price')
    quantity = req.GET.get('quantity')
    category = req.GET.get('category')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "insert into product(name,brand,price,quantity,category) values('{0}','{1}','{2}','{3}','{4}')".format(
        name, brand, price, quantity, category)
    cr.execute(sql)
    con.commit()
    con.close()
    return HttpResponse("Data Inserted")


def emprec(req):
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from employee"
    cr.execute(sql)
    data = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'emprec.html', {'detail': data})


def prorec(req):
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from product"
    cr.execute(sql)
    data = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'prorec.html', {'detail': data})


def custrec(req):
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from customer"
    cr.execute(sql)
    data = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'custrec.html', {'detail': data})


def sellrec(req):
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from sells"
    cr.execute(sql)
    data = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'sellrec.html', {'detail': data})


def editemp(req):
    editid = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from employee where id={0}".format(editid)
    cr.execute(sql)
    rec = cr.fetchall()
    con.close()
    return render(req, 'editemp.html', {'detail': rec})


def editpro(req):
    editid = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from product where id={0}".format(editid)
    cr.execute(sql)
    rec = cr.fetchall()
    con.close()
    return render(req, 'editpro.html', {'detail': rec})


def editcust(req):
    editid = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from customer where id={0}".format(editid)
    cr.execute(sql)
    rec = cr.fetchall()
    con.close()
    return render(req, 'editcust.html', {'detail': rec})


def editTaskemp(req):
    name = req.GET.get('namee')
    fname = req.GET.get('fnamee')
    email = req.GET.get('emaile')
    moblie = req.GET.get('mobilee')
    password = req.GET.get('passe')
    id = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "update employee set name='{0}',fname='{1}',email='{2}',moblie='{3}',password='{4}' where id='{5}'".format(
        name, fname, email, moblie, password, id)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect("/emprec")


def editTaskcust(req):
    name = req.GET.get('namee')
    fname = req.GET.get('fnamee')
    email = req.GET.get('emaile')
    moblie = req.GET.get('mobilee')
    password = req.GET.get('passe')
    id = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "update customer set name='{0}',fname='{1}',email='{2}',moblie='{3}',password='{4}' where id='{5}'".format(
        name, fname, email, moblie, password, id)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect("/custrec")


def editTaskpro(req):
    name = req.GET.get('namee')
    brand = req.GET.get('brande')
    price = req.GET.get('pricee')
    quantity = req.GET.get('quantitye')
    category = req.GET.get('categorye')
    id = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "update product set name='{0}',brand='{1}',price='{2}',quantity='{3}',category='{4}' where id='{5}'".format(
        name, brand, price, quantity, category, id)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect("/prorec")


def deletetaskemp(req):
    delid = req.GET.get('sid')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "delete from employee where id={0}".format(delid)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect("/emprec")


def deletetaskcust(req):
    delid = req.GET.get('sid')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "delete from customer where id={0}".format(delid)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect("/custrec")


def deletetaskpro(req):
    delid = req.GET.get('sid')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "delete from product where id={0}".format(delid)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect("/prorec")


def proddetail(req):
    idd = req.GET.get('category')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from product where category='{0}'".format(idd)
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    return render(req, "proddetail.html", {"product": rec})


def cart(req):
    idd = req.GET.get('ide')
    email = str(rec12[0][3])
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from product where id='{0}'".format(idd)
    cr.execute(sql)
    prod = cr.fetchall()
    id = prod[0][0]
    name = prod[0][1]
    brand = prod[0][2]
    price = prod[0][3]
    q = prod[0][4]
    cat = prod[0][5]
    sql1 = "insert into cart set id='{0}',email='{1}',name='{2}',brand='{3}',price='{4}',quantity='{5}',category='{6}'".format(
        id, email, name, brand, price, q, cat)
    cr = con.cursor()
    cr.execute(sql1)
    con.commit()
    con.close()
    return redirect("/carttask")


def carttask(req):
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from cart"
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'cart.html', {"record": rec})


def buynow(req):
    ide = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from product where id='{0}'".format(ide)
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    global rec1
    rec1 = rec
    return render(req, 'buynow.html', {"record": rec})


def buy(req):
    q = int(req.GET.get('quan'))
    global q1
    q1 = q
    ide = rec1[0][0]
    qold = int(rec1[0][4])
    qq = qold-q
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "update product set quantity='{0}' where id='{1}'".format(qq, ide)
    cr.execute(sql)
    rec2 = cr.fetchall()
    con.commit()
    con.close()
    global rec3
    rec3 = rec1
    return redirect("/soldprod")


def soldprod(req):
    name = str(rec0[0][1])
    email = str(rec0[0][3])
    pid = str(rec3[0][0])
    pname = str(rec3[0][1])
    c = str(rec3[0][2])
    p = str(rec3[0][3])
    q = str(q1)
    pd = str(rec3[0][5])
    now = datetime.datetime.now()
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "insert into sells(id,name,email,product_name,category,brand,price,quantity,date) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(
        pid, name, email, pname, c, p, q, pd, now)
    cr.execute(sql)
    con.commit()
    con.close()
    return HttpResponse("<h1>Your Order is Successfully Completed<h1>")


def myorder(req):
    email = str(rec12[0][3])
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from sells where email='{0}'".format(email)
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'order.html', {"order": rec})


def userprofile(req):
    email = str(rec12[0][3])
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from customer where email='{0}'".format(email)
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    cpro = rec
    return render(req, 'profile.html', {"profile": cpro})


def adminprofile(req):
    email = str(rec1[0][3])
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from admin where email='{0}'".format(email)
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    apro = rec
    return render(req, 'adprofile.html', {"profile": apro})


def invoice(req):
    ide = req.GET.get('time')
    con = mysql.connect(host="localhost", user="root",
                        password="Ranaji1", database="sms")
    cr = con.cursor()
    sql = "select * from sells where date='{0}'".format(ide)
    cr.execute(sql)
    rec = cr.fetchall()
    con.commit()
    con.close()
    invo = rec
    return render(req, 'corder.html', {"invoice": invo})
