import MySQLdb as mdb

con = mdb.connect(host = "localhost", user = "root", passwd ="123456", db = "try_01")

with con:
	cur = con.cursor()

	cur.execute("INSERT INTO bookorder_books(ISBN13, ISBN10, title, authors, publisher, pubDate,\
	    	language, cover, inventory, price, bookFormat, keywords, subject)\
        VALUES('978-0062073471','0062073478','And Then There Were None','Agathas Christie',\
        	'William Morrow Paperbacks','January 18, 2011','English',\
        	'http://ecx.images-amazon.com/images/I/51oEX2uka5L._SX331_B01.204.203.200_.jpg',\
        	24,'10.02','Hardcover','mystery','novel')")
	cur.execute("INSERT INTO bookorder_books(ISBN13, ISBN10, title, authors, publisher, pubDate,\
	    	language, cover, inventory, price, bookFormat, keywords, subject)\
        VALUES('978-0545044257','0545044251','Harry Potter #1-7','J. K. Rowling',\
        	'Arthur A. Levine Books','October 16, 2007','English',\
        	'http://ecx.images-amazon.com/images/I/41MUmy9w52L._SX331_B01.204.203.200_.jpg',\
        	227,'99.99','Hardcover','mystery','novel')")
	cur.execute("INSERT INTO bookorder_books(ISBN13, ISBN10, title, authors, publisher, pubDate,\
	    	language, cover, inventory, price, bookFormat, keywords, subject)\
        VALUES('978-1505280951','1505280958','The Wonderful Wizard of Oz','L. Frank Baum',\
        	'CreateSpace Independent Publishing Platform','November 29, 2014','English',\
        	'http://ecx.images-amazon.com/images/I/51FwiJgch9L._SX331_B01.204.203.200_.jpg',\
        	197,'6.99','Paperback','adventure','chiddren novel')")
	cur.execute("INSERT INTO bookorder_books(ISBN13, ISBN10, title, authors, publisher, pubDate,\
	    	language, cover, inventory, price, bookFormat, keywords, subject)\
        VALUES('978-0375825446','0375825444','Flipped','Wendelin Van Draanen',\
        	'Ember','May 13, 2003','English',\
        	'http://ecx.images-amazon.com/images/I/31uAFdCu1nL._SX322_B01.204.203.200_.jpg',\
        	12,'8.99','Paperback','love','novel')")	
	cur.execute("INSERT INTO bookorder_books(ISBN13, ISBN10, title, authors, publisher, pubDate,\
	    	language, cover, inventory, price, bookFormat, keywords, subject)\
        VALUES('978-0679734772','0679734775','The House on Mango Street','Sandra Cisneros',\
        	'Vintage','April 3, 1991','English',\
        	'http://ecx.images-amazon.com/images/I/51KEr5saI2L._SX323_B01.204.203.200_.jpg',\
        	521,'8.99','Audio CD','A young Latina girl inventing for herself who and what she will become.','novel')")	
	cur.execute("INSERT INTO bookorder_books(ISBN13, ISBN10, title, authors, publisher, pubDate,\
	    	language, cover, inventory, price, bookFormat, keywords, subject)\
        VALUES('978-0981467344','0981467342','Two Scoops of Django: Best Practices for Django 1.8',\
        	'Daniel and Audrey Roy Greenfeld','Two Scoops Press','May 15, 2015','English',\
        	'http://ecx.images-amazon.com/images/I/61tiw0quz4L._SX404_B01.204.203.200_.jpg',\
        	32,'40.46','Paperback','Django','Database')")	


