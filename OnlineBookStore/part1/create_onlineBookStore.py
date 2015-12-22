import MySQLdb as mdb

con = mdb.connect(host = "localhost", user = "root", passwd = "123456", db = "onlineBookStore")

with con:
	cur = con.cursor()
	
	cur.execute("CREATE TABLE books(ISBN13 varchar(14) primary key, ISBN10 varchar(10),\
		title varchar(100), authors varchar(50), publisher varchar(100),\
		pubDate varchar(20), language varchar(20), cover varchar(100),\
		inventory integer, price varchar(10), bookFormat varchar(10),\
		keywords varchar(100), subject varchar(100) );")

	cur.execute("CREATE TABLE customers(login_name varchar(20) primary key,\
	    full_name varchar(50), address varchar(200),\
	    phone_number varchar(20), credit_card varchar(50) );")

	cur.execute("CREATE TABLE orderinfo(oid varchar(20) primary key,\
	    login_name varchar(20) references customers(login_name),\
		date varchar(20), status varchar(20) );")

	cur.execute("CREATE TABLE bookinfo(id integer primary key,\
		orderId varchar(20) references orderInfo(orderId),\
		ISBN13 varchar(14) references books(ISBN13), copy integer );")

	cur.execute("CREATE TABLE feedback(id integer primary key,\
		login_name varchar(20) references customers(login_name),\
		ISBN13 varchar(14) references books(ISBN13),\
		fscore int, ftext varchar(1000));")

	cur.execute("CREATE TABLE rate(id integer primary key,\
		login_name varchar(20) references customers(login_name),\
		fid integer references feedback(id), rscore integer);")