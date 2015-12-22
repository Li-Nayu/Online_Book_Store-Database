create table Books(
	ISBN13 char(14) primary key,
	ISBN10 char(10),
	title char(100),
	authors char(50),
	publisher char(100),
	pubDate char(20),
	language char(20), # additive attribute
	cover char(50), # additive attribute
    inventory int,
	price real,
	format char(10) check(format = 'hardcover' or format = 'softcover'),
	keywords char(100),
	subject char(100)
);

create table Customers(
	login_name char(20) primary key,
	full_name char(50),
	password char(20),
	address char(200),
	phone_number char(20),
	credit_card char(50)
);

create table BookInfo(
	oid char(20),
    ISBN13 char(14),
    copy int,
    primary key(oid,ISBN13),
	foreign key (ISBN13) references Books 
);

create table OrderInfo(
	oid char(20) primary key,
	login_name char(20),
	date char(20),
	status char(20),
    foreign key (login_name) references Customers  
);

create table Feedback(
	login_name char(20),
    ISBN13 char(14),
    score int check(score >=1 and score <=10),
    text char(10000),
    primary key(ISBN13,login_name),
	foreign key (login_name) references Customers,
    foreign key (ISBN13) references Books
);

create table Rates(
	login_name1 char(20),
    login_name2 char(20) check (login_name1<>login_name2),
    ISBN13 char(14),
    primary key (login_name,fid),
    foreign key (login_name1) references Customers,
    foreign key (login_name2,ISBN13) references Feedback
);