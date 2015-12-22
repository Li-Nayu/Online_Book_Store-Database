import MySQLdb 


def search(search_key):

	search_key = search_key.title()
	search_value = search_key.split()

	db = MySQLdb.connect(user='root', db='try_02', passwd='APTX38324MYSQL', host='localhost')
	cursor = db.cursor()
	ISBN_LIST = []
	ISBN_result = []
	for value in search_value:

		string = "SELECT * FROM bookorder_books where title LIKE " + "'%" + value + "%'" + " OR  authors LIKE " + "'%" + value + "%'"
		cursor.execute(string)
		ISBN = [row[0]  for row in cursor.fetchall()]

		ISBN_LIST.extend(ISBN)
	db.close()
	print len(ISBN_LIST)
	for value in ISBN_LIST:
		if value in ISBN_result:
			pass
		else:
			ISBN_result.append(value)

	return ISBN_result

result = search('Rowling')
for value in result:
	print value
