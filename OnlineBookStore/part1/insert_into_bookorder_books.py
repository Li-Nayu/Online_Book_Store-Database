import MySQLdb as mdb

con = mdb.connect(host = "localhost", user = "root", passwd ="123456", db = "try_01")

with con:
	cur = con.cursor()
	
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject) \
	VALUES ('Photoshop Elements 9: The Missing Manual','paperback',60,'English','Barbara Brundage','Pogue Press','2010','1449389678','978-1455389673',\
		'http://ecx.images-amazon.com/images/I/41lv4IN1cjL._SX379_BO1,204,203,200_.jpg','$29.48','Photoshop','Computer & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Where Good Ideas Come From: The Natural History of Innovation','hardcover',36,'English','Steven Johnson','Riverhead Hardcover','2010','1594487715','978-1594487712',\
		'http://ecx.images-amazon.com/images/I/31OhEnvRv0L._BO1,204,203,200_.jpg','$4.94','Creativity','Motivational');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Digital Photography Book','paperback',29,'English','Scott Kelby','Peachpit Press','May 20, 2013','032147404X','978-0321474049',\
		'http://ecx.images-amazon.com/images/I/51IG9K-Xc2L._SY344_BO1,204,203,200_.jpg','$20.98','Video photography','Computer & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Great Gatsby','hardcover',21,'English','F. Scott Fitzgerald','Scribner','September 30, 2004','0684801523','978-0684801520',\
		'http://ecx.images-amazon.com/images/I/51khWutZqCL._SX325_BO1,204,203,200_.jpg','$8.49','Classic','Literature & Fiction');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Davis s Drug Guide For Nurses (book With Cd-rom) And Mednotes: Nurse s Pocket Pharmacology Guide','hardcover',1482,'English','Judith Hopfer Deglin, April Hazard Vallerand','F. A. Davis Company','June 5, 2014','0803612257','978-0803612259',\
		'http://ecx.images-amazon.com/images/I/51OWa1937qL._SY344_BO1,204,203,200_.jpg','$14.78','Pharmacology','Textbooks');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Microsoft Office 2007: Introductory Concepts and Techniques','paperback',136,'English','Gary B. Shelly','The MIT Press','2010','1111529027','978-1111529024',\
		'http://ecx.images-amazon.com/images/I/51KgqYzGPRL._SX394_BO1,204,203,200_.jpg','$30.99','Enterprise','Computer & Technology');")
	cur.execute("INSERT INTO  bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Future of Learning Institutions in a Digital Age','paperback',81,'English','Cathy N. Davidson, David Theo Goldberg','The MIT Press','June 5, 2009','0262513595','978-0262513593',\
		'http://ecx.images-amazon.com/images/I/41D9trqCi%2BL._SY344_BO1,204,203,200_.jpg','$16.00','Reference','Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The New Rules of Marketing and PR','paperback',20,'English','David Meerman Scott','Wiley','2010','0470547812','978-0470547816',\
		'http://ecx.images-amazon.com/images/I/51tC86oBm2L._SX331_BO1,204,203,200_.jpg','$14.75','Marketing','Business & Sales');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Dont Make Me Think: A Common Sense Approach to Web Usability, 2nd Edition','paperback',16,'English','Steve Krug','New Riders Press','January 3, 2014','0321344758','978-0321344755',\
		'http://ecx.images-amazon.com/images/I/51pnouuPO5L._SX387_BO1,204,203,200_.jpg','$26.10','Web design','Computer & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Shallows: What the Internet Is Doing to Our Brains','hardcover',26,'English','Nicholas Carr','W. W. Norton & Company ','2010','0393072223','978-0393072228',\
		'http://ecx.images-amazon.com/images/I/51nePfjFLoL._SY344_BO1,204,203,200_.jpg','$23.46','Neuroscience',' Medical');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('CompTIA A+ Certification All-in-One Exam Guide, Seventh Edition (Exams 220-701 & 220-702)','hardcover',13,'English','Michael Meyers','McGraw-Hill Osborne Media','2010','0071701338','978-0071701334',\
		'http://ecx.images-amazon.com/images/I/51GO%2BsxPFrL._SX382_BO1,204,203,200_.jpg','$13.00','CompTIA',' Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Statistics for People Who (Think They) Hate Statistics: Excel 2007 Edition','paperback',42,'English','Li Nayu','Sage Publications, Inc','2009','1412971020','978-1412971027',\
		'http://ecx.images-amazon.com/images/I/51%2BoSOm9HjL._SY344_BO1,204,203,200_.jpg','$37.82','Probability & Statistics','Science & Math');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Windows 7 For Dummies Book + DVD Bundle','paperback',48,'English','Andy Rathbone','For Dummies','2009','0470523980','978-0470523988',\
		'http://ecx.images-amazon.com/images/I/51hVa4RgG0L._SX258_BO1,204,203,200_.jpg','$19.90','Microsoft','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Introduction to Algorithms, Third Edition','hardcover',12,'English','Thomas H. Cormen','The MIT Press','2009','0262033844','978-0262033848',\
		'http://ecx.images-amazon.com/images/I/51eDwv7tCtL._SX442_BO1,204,203,200_.jpg','$50.09','Computer Science','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Algorithm Design','hardcover',46,'English','Jon Kleinberg, Eva Tardos','Addison Wesley','March 26, 2005','0321295358','978-0321295354',\
		'http://ecx.images-amazon.com/images/I/51BHNytrZCL._SX258_BO1,204,203,200_.jpg','$48,50','Languages & Tools','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Data Structures and Algorithm Analysis in C++ (3rd Edition)','hardcover',58,'English','Mark A. Weiss','Addison Wesley','2006','032144146X','978-0321441461',\
		'http://ecx.images-amazon.com/images/I/41oGuEd4krL._SX378_BO1,204,203,200_.jpg','$29.39','> Computer Science','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Algorithm Design Manual','hardcover',73,'English','Steven S. Skiena','Springer','2008','1848000693','978-1848000698',\
		'http://ecx.images-amazon.com/images/I/51HpjMQ6hDL._SX346_BO1,204,203,200_.jpg','$67.75','Discrete Mathematics','Mathematics');")	
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Introduction to Computing Systems: From bits & gates to C & beyond','hardcover',65,'English','Yale Patt, Sanjay Patel','McGraw-Hill Science/Engineering/Math','August 5, 2003','0072467509','978-0072467505',\
		'http://ecx.images-amazon.com/images/I/41MHRPUGZML._SX402_BO1,204,203,200_.jpg','$45,67','Design & Architecture','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Hackers & Painters: Big Ideas from the Computer Age','paperback',17,'English','Paul Graham','O Reilly Media','2010','1449389554','978-1449389550',\
		'http://ecx.images-amazon.com/images/I/51foanUeChL._SY344_BO1,204,203,200_.jpg','$15.07','Protocols & API','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Data Structures and Algorithms in Java','hardcover',36,'English','Michael T. Goodrich, Roberto Tamassia','Wiley','January 28, 2014','0470383267','978-0470383261',\
		'http://ecx.images-amazon.com/images/I/61cFhkf7NCL._SX405_BO1,204,203,200_.jpg','$116.69','Java','Computers & Technology');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Quantitative Chemical Analysis','hardcover',92,'English','Daniel C. Harris','W. H. Freeman','2002','0716744643','978-0716744641',\
		'http://ecx.images-amazon.com/images/I/51LS5PZeZxL._SX397_BO1,204,203,200_.jpg','$119.98','Chemistry','Science & Mathematics');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Transport Phenomena, Revised 2nd Edition','hardcover',95,'English','R. Byron Bird','John Wiley & Sons, Inc.','December 11, 2006','0470115394','978-0470115398',\
		'http://ecx.images-amazon.com/images/I/41QjGv0OCsL._SX395_BO1,204,203,200_.jpg','$167.02','Fluid Dynamics','Engineering & Transportation');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Introduction to Chemical Engineering Thermodynamics (The Mcgraw-Hill Chemical Engineering Series)','hardcover',84,'English','J.M. Smith, Hendrick Van Ness, Michael Abbott','McGraw-Hill Science/Engineering/Math','November 12, 2004','0073104450','978-0073104454',\
		'http://ecx.images-amazon.com/images/I/51fMuIh-JJL._SX376_BO1,204,203,200_.jpg','$75.50','Chemical','Engineering & Transportation');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Fundamentals of Momentum, Heat and Mass Transfer','hardcover',40,'English','James Welty, Charles E. Wicks','Wiley','September 9, 2014','0470128682','978-0470128688',\
		'http://ecx.images-amazon.com/images/I/51amznjPCBL._SX401_BO1,204,203,200_.jpg','$181.38','Materials & Material Science','Engineering & Transportation');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Elements of Chemical Reaction Engineering (4th Edition)','hardcover',18,'English','H. Scott Fogler','Prentice Hall','September 2, 2005','0130473944','978-0130473943',\
		'http://ecx.images-amazon.com/images/I/41%2Bor55ltOL._SX358_BO1,204,203,200_.jpg','$19.00','Chemical','Engineering & Transportation');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Basic Biomechanics','paperback',57,'English','Susan Hall','McGraw-Hill Humanities/Social Sciences/Languages','2006','0073044814','978-0073044811',\
		'http://ecx.images-amazon.com/images/I/51C07rDIU4L._SX388_BO1,204,203,200_.jpg','$36.29','Bioengineering','Engineering & Transportation');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Dracula','paperback',38,'English','Bram Stoker','Nabu Press ','April 18, 2000','1177759144','978-1177759144',\
		'http://ecx.images-amazon.com/images/I/51N33RX1FWL._SX312_BO1,204,203,200_.jpg','$3.37','Contemporary','Literature & Fiction');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Autobiography of Benjamin Franklin','paperback',16,'English','Benjamin Franklin','IndoEuropeanPublishing.com ','2010','1604443413','978-1604443417',\
		'http://ecx.images-amazon.com/images/I/51MxjDM80-L._SY344_BO1,204,203,200_.jpg','$9.95','Colonial Period','History');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Common Sense (Penguin Classics)','paperback',12,'English','Thomas Paine','Penguin Classics ','November 18, 1982','0140390162','978-0140390162',\
		'http://ecx.images-amazon.com/images/I/41atUpu7hSL._SX323_BO1,204,203,200_.jpg','$9.99','United States','Politics & Social Sciences');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Persuasion','paperback',30,'English','Jane Austen','Nabu Press ','November 29, 2014','1178018636','978-1178018639',\
		'http://ecx.images-amazon.com/images/I/51EaJuv%2BHHL._SX331_BO1,204,203,200_.jpg','$7.79','Classics','Literature & Fiction');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Big Short: Inside the Doomsday Machine (Thorndike Press Large Print Nonfiction Series)','hardcover',41,'English','Michael Lewis','Thorndike Press','September 15, 2010','141043026X','978-1410430267',\
		'http://ecx.images-amazon.com/images/I/41PzLYxYZbL._SX373_BO1,204,203,200_.jpg','$19.99','Americas','History');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Memorable Thoughts of Socrates','paperback',14,'English','Xenophon','Watchmaker Publishing ','September 3, 2013','1603863206','978-1603863209',\
		'http://ecx.images-amazon.com/images/I/51Ouf8HZpJL._SX258_BO1,204,203,200_.jpg','$14.00','Classics','Literature & Fiction');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Thus Spoke Zarathustra (Selections)','paperback',40,'English','Friedrich Nietzsche','Dover Publications','May 5, 2014','0486437116','978-0486437118',\
		'http://ecx.images-amazon.com/images/I/51h6493QazL._SX314_BO1,204,203,200_.jpg','$35.90','Modern','Philosophy');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Do Androids Dream of Electric Sheep?: 1800 Headwords (Oxford Bookworms Library)','paperback',28,'English','Philip K. Dick','Oxford University Press ','May 28, 1996','0194792226','978-0194792226',\
		'http://ecx.images-amazon.com/images/I/51ehNNnPpDL._SY344_BO1,204,203,200_.jpg','$56.00','Media Tie-In','Comics & Graphic Novels');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Guns, Germs, and Steel: The Fates of Human Societies','paperback',49,'English','Jared M. Diamond','W. W. Norton & Company','April 1, 1999','0393317552','978-0393317558',\
		'http://ecx.images-amazon.com/images/I/51TMOKNiZCL._SX317_BO1,204,203,200_.jpg','$10.92','Geography','Textbooks');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Cultural Landscape: An Introduction to Human Geography (10th Edition)','hardcover',57,'English','James M. Rubenstein','Prentice Hall','January 12, 2013','0321677358','978-0321677358',\
		'http://ecx.images-amazon.com/images/I/51uJxYP%2B5eL._SX412_BO1,204,203,200_.jpg','$55.09','Human Geography','Politics');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Communist Manifesto (Norton Critical Editions)','paperback',22,'English','Karl Marx','W. W. Norton & Company','February 7, 2014','0393956164','978-0393956160',\
		'http://ecx.images-amazon.com/images/I/51vHCno0a4L._SX330_BO1,204,203,200_.jpg','$78.60','Political','Politics & Social Sciences');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('The Wealth of Nations (Modern Library Classics)','paperback',11,'English','Adam Smith, Robert Reich','Modern Library ','March 4, 2003','0679783369','978-0679783367',\
		'http://ecx.images-amazon.com/images/I/51BQGhex0xL._SX298_BO1,204,203,200_.jpg','$89.00','Business','Biographies & Memoirs');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Biology with MasteringBiology (8th Edition)','hardcover',79,'English','Neil A. Campbell, Jane B. Reece','Benjamin Cummings','November 16, 2013','0321543254','978-0321543257',\
		'http://ecx.images-amazon.com/images/I/413FBttp5BL._SX412_BO1,204,203,200_.jpg','$69.00','Biology','Biological Sciences');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Kaplan MCAT Biology Review','paperback',19,'English','Kaplan','Kaplan Publishing','July 7, 2015','1607146436','978-1607146438',\
		'http://ecx.images-amazon.com/images/I/514j473H5RL._SX381_BO1,204,203,200_.jpg','$45.80','Biology','Textbooks');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Notes on Nursing: What It Is, and What It Is Not','paperback',13,'English','Florence Nightingale','Dover Publications','May 24, 2012','048622340X','978-0486223407',\
		'http://ecx.images-amazon.com/images/I/51pBtVmSsCL._SY344_BO1,204,203,200_.jpg','24.95','Nursing','Medical eBooks');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Kaplan MCAT General Chemistry Review','paperback',56,'English','Kaplan','Kaplan Publishing','July 1, 2014','1607146398','978-1607146391',\
		'http://ecx.images-amazon.com/images/I/51wx0wWEncL._SX382_BO1,204,203,200_.jpg','$85.90','General & Reference','Science & Math');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Sidelights On Relativity','hardcover',26,'English','Albert Einstein','Kessinger Publishing, LLC ','July 21, 2010','1169173802','978-1169173804',\
		'http://ecx.images-amazon.com/images/I/51lAaav0npL._SX311_BO1,204,203,200_.jpg','$36.20','Geometry & Topology',' Mathematics');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Frankenstein (Cambridge Literature)','paperback',86,'English','Mary Shelley','Cambridge University Press ','October 21, 1994','0521587026','978-0521587020',\
		'http://ecx.images-amazon.com/images/I/51Ww0FqYJDL._SX312_BO1,204,203,200_.jpg','$3.60','Horror','Literature & Fiction');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Curious Folks Ask','paperback',22,'English','Sherry Seethaler','FT Press','December 15, 2009','0137057385','978-0137057382',\
		'http://ecx.images-amazon.com/images/I/51roREdIupL._SX335_BO1,204,203,200_.jpg','11.99','Education & Teaching','Science');")
	cur.execute("INSERT INTO bookorder_books(title,bookFormat,inventory,language,authors,publisher,pubDate,ISBN10,ISBN13,cover,price,keywords,subject)\
	VALUES ('Math for Moms and Dads: A dictionary of terms and concepts...just for parents','paperback',20,'English','Kaplan','Kaplan Publishing','October 7, 2008','1427798192','978-1427798190',\
		'http://ecx.images-amazon.com/images/I/51WyDT8kg6L._SY344_BO1,204,203,200_.jpg','$3.69','Study & Teaching','Science & Math');")