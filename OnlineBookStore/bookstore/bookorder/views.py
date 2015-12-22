#filename:views.py
#-*-coding:utf-8-*-

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from bookorder.forms import *
from bookorder.models import books,customers,feedback,orderinfo,bookinfo,shop_cart,rate
import MySQLdb 
import re, time

'''
changed the app, the models have to import again
'''

def main_page(request):
	''' Main Page '''

	if "search_key" in request.GET:
		search_key = request.GET['search_key']
		ISBN_LIST = search(search_key)
		BOOK_OB_LIST=[]

		for value in ISBN_LIST:
			book = books.objects.filter(ISBN13=value)
			#the result of filter operate is also a list
			BOOK_OB_LIST.extend(book)
		if len(BOOK_OB_LIST)==0:
			variables = RequestContext(request, {"search_result" : BOOK_OB_LIST,'search_key':search_key, 'No_result':'NO result'})
		else:
			try:
				if request.GET['sorted_way']:
					sorted_result =  sort_search_result(BOOK_OB_LIST, request.GET['sorted_way'])
					if request.GET['sorted_way']=='1':
						variables = RequestContext(request, {"search_result" : sorted_result, 'way_1':'sorted'})
					else:
						variables = RequestContext(request, {"search_result" : sorted_result, 'way_2':'sorted'})
			except:
				variables = RequestContext(request, {"search_result" : BOOK_OB_LIST, 'way_3':'sorted'})
		return render_to_response( 'search_result.html', variables)
	else:
		book_list = books.objects.all().order_by('inventory')
		#print type(book_list[0].ISBN13)
		book_recom = book_recommand()
		for value in book_recom[0:5]:
			value.ISBN = books.objects.get(ISBN13 = value.ISBN) 
			
		book_dict={"fixed_key":book_list[0:5],'recommand_book' : book_recom[0:5]}
		dict_statics = best_seller_last_month()
		for k,v in dict_statics.items():
			book_dict[k] = v[0:5]
		
		variables = RequestContext(request, book_dict)

	return render_to_response( 'main_page.html', variables)

	

def user_page(request, username):
	''' Personal Page '''

	usr_info_dict = find_usr_info(username)
	variables = RequestContext(request, usr_info_dict)
	return render_to_response('user_page.html', variables)


def modify_user_info(request, username):
	usr_info_dict = find_usr_info(username)
	variables = RequestContext(request, usr_info_dict)

	if 'new_addr' in request.GET:
		customers_ob = customers.objects.get(full_name = username)
		if len(request.GET['new_addr'])==0:
			pass
		else:
			customers_ob.address = request.GET['new_addr']
			customers_ob.save()
		if len(request.GET['new_num'])==0:
			pass
		else:
			customers_ob.phone_number = request.GET['new_num']
			customers_ob.save()
		if len(request.GET['new_credit'])==0:
			pass
		else:
			customers_ob.credit_card = request.GET['new_credit']
			customers_ob.save()

		return render_to_response('user_info_changed.html',variables)

	
	return render_to_response('modify_user_info.html', variables)



def shop_cart_page(request, username):
	'''Shopping Cart Page'''
	cart_host_ob = customers.objects.get(full_name=username)
	cart_host = cart_host_ob.login_name
	cart_LIST = shop_cart.objects.filter(login_name=cart_host_ob)
	if 'trash' in request.GET:
		shop_cart_item_delete(username, request.GET['trash'],request.GET['copy'])


	if 'generate_order' in request.GET:
		migrate_data(cart_host_ob,  cart_LIST)
		erase_cart(cart_host_ob)
		
		variables = variables = RequestContext(request, {'cart_LIST': cart_LIST})
		return render_to_response('order_gen.html',variables)
	else:
		pass

	if len(cart_LIST)==0:
		variables = RequestContext(request, {'No_order' : 'No Order yet'})
		return render_to_response('shop_cart_page.html',variables)
	else:
		variables = RequestContext(request,{'cart_LIST': cart_LIST})
		return render_to_response('shop_cart_page.html',variables)

def order_page(request, username):
	''' Personal Order Page '''
	info_dict = order_page_info(username)

	# variables = RequestContext(request,{'order_list': order_list,'order_book_list' : order_book_list })
	variables = RequestContext(request, info_dict)
	return render_to_response('order_page.html',variables)



def book_page(request,book_ISBNpart1,book_ISBNpart2):
	''' Single Book Page '''
	book_ISBN = book_ISBNpart1 + '-' + book_ISBNpart2
	f_ISBN = books.objects.get(ISBN13=book_ISBN)
	if request.user.username:

		submit_man = customers.objects.get(full_name=request.user.username)
		submit_man_name = submit_man.full_name
	
	#Submit feedback
	if "submit_feedback" in request.GET:
		feedback_search = feedback.objects.filter(login_name=submit_man, ISBN13=book_ISBN)
		#feedback_search = feedback.objects.filter(full_name=submit_man, ISBN13=feedback_book_ISBN)
		if len(feedback_search)==0 or len(submit_feedback)==0:
			if len(request.GET['rate_this_book'])==0:
				variables = RequestContext(request,{'submit_man': submit_man_name})
				return render_to_response( 'submit_feedback_failed.html', variables)
			else:
				f1 = feedback(fid = submit_man.login_name + f_ISBN.ISBN13,
										login_name = submit_man,
										ISBN13 = f_ISBN,
										fscore = request.GET['rate_this_book'],
										text = request.GET['submit_feedback'])
				f1.save()
				variables = RequestContext(request,{'submit_man': submit_man_name})
				return render_to_response( 'submit_feedback_success.html', variables)
		else:
			variables = RequestContext(request,{'submit_man': submit_man_name})
			return render_to_response( 'submit_feedback_failed.html', variables)

	#Add book to shopping cart
	if "add_to_cart" in request.GET:
		#judge whether the inventory is enough
		if int(request.GET['add_to_cart']) > f_ISBN.inventory:
			variables = RequestContext(request,{'Buy_man': request.user.username})
			return render_to_response('add_to_cart_failed.html',variables)
		else:		
			#judge whether where are same book in shoppin cart, if is, just add the copy of this book, if no create new item in shopping cart
			if len(shop_cart.objects.filter(ISBN13 = f_ISBN,login_name = submit_man))!=0:
				s_book = shop_cart.objects.get(ISBN13 = f_ISBN)
				s_book.copy = str(int(s_book.copy) + int(request.GET['add_to_cart']))
				s_book.save()
			else:
				s1 = shop_cart(login_name = submit_man,
								ISBN13 = f_ISBN,
								copy = request.GET['add_to_cart'])
				s1.save()
				book_inv = f_ISBN.inventory - int(request.GET['add_to_cart'])
				f_ISBN.inventory = book_inv
				f_ISBN.save()

			variables = RequestContext(request, {'Buy_man': submit_man_name})
			return render_to_response('cart_test.html',variables)

	#Submit a rate to one certain feedback.
	if 'rate' in request.GET:
		log_name = customers.objects.get(full_name = request.user.username)
		fid = feedback.objects.get(fid = request.GET['fid'])
		if log_name.login_name==fid.login_name.login_name:
			return render_to_response('rated_failed.html')
		else:
			if len(rate.objects.filter(login_name = log_name, fid = fid))==0:
				rate1 = rate(login_name = log_name,
							fid = fid,
							rscore = int(request.GET['rate'])
							)
				rate1.save()
			else:
				return render_to_response('have_rated.html')
				


	#Get the info of book
	single_book = books.objects.filter(ISBN13=book_ISBN) #the data type of single_book is LIST
	related_book = related(book_ISBN)
	#get the feedback of this book

	# feedback_LIST = feedback.objects.filter(ISBN13=book_ISBN)
	feed_list = feedback.objects.filter(ISBN13=book_ISBN)
	feedback_LIST = feedback_gene_sort(feed_list)

	try:
		if request.GET['choose']=='5':
			if len(feedback_LIST)<=5:
				feedback_LIST_show = feedback_LIST
			else:
				feedback_LIST_show = feedback_LIST[0:5]
		else:
			if len(feedback_LIST)<=10:
				feedback_LIST_show = feedback_LIST
			else:
				feedback_LIST_show = feedback_LIST[0:10]
	except:
		feedback_LIST_5 = []
		if len(feedback_LIST)<=5:
			feedback_LIST_show = feedback_LIST
		else:
			feedback_LIST_show = feedback_LIST[0:5]

	variables = RequestContext(request, {'book_info': single_book,'written_feedback':feedback_LIST_show,'related_book': related_book})
	return render_to_response( 'book_page.html', variables)



def book_feedbacks(request, book_ISBNpart1,book_ISBNpart2):
	book_ISBN = book_ISBNpart1 + '-' + book_ISBNpart2
	f_ISBN = books.objects.filter(ISBN13=book_ISBN)
	feed_list = feedback.objects.filter(ISBN13=book_ISBN)

	feedback_LIST = feedback_gene_sort(feed_list)

	dict_va = {'book_info':f_ISBN,'written_feedback':feedback_LIST}
	variables = RequestContext(request, dict_va)
	return render_to_response( 'book_feedbacks.html', variables)




def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_page(request):
	''' Regster Page '''
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			#Write to customers TABLE
			customers.objects.create(login_name = form.clean_data['email'],
									full_name = form.clean_data['username'])
			user = User.objects.create_user(
				username=form.clean_data['username'],
				password=form.clean_data['password1'],
				email=form.clean_data['email']
			)
			return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response(
		'registration/register.html',variables)


def search(search_key):
	''' Function used to search books. '''
	search_key = search_key.title()
	search_value = search_key.split()

	db = MySQLdb.connect(user='root', db='try_01', passwd='123456', host='localhost')
	cursor = db.cursor()
	ISBN_LIST = []
	ISBN_result = []
	for value in search_value:

		string = "SELECT * FROM bookorder_books where title LIKE " + "'%" + value + "%'" + " OR  authors LIKE " + "'%" + value + "%'" + " OR publisher LIKE " + "'%" + value + "%'" +  " OR subject LIKE " + "'%" + value + "%'"
		cursor.execute(string)
		ISBN = [row[0]  for row in cursor.fetchall()]

		ISBN_LIST.extend(ISBN)
	db.close()

	for value in ISBN_LIST:
		if value in ISBN_result:
			pass
		else:
			ISBN_result.append(value)
	return ISBN_result


def related(book_ISBN):
	''' Function to feedbacks of one Book. '''
	related_book_raw = []
	related_book_result = []
	related_book_ob = []

	related_oid = bookinfo.objects.filter(ISBN13=book_ISBN)
	for value in related_oid:
		related_bookinfo_ob = bookinfo.objects.filter(oid=value.oid.oid)
		related_book_raw.extend(related_bookinfo_ob)

	for value in related_book_raw:
		if value.ISBN13.ISBN13 in related_book_result:
			pass
		elif value.ISBN13.ISBN13 == book_ISBN:
			pass
		else:
			related_book_result.append(value.ISBN13.ISBN13)
	for value in related_book_result:
		book_ob = books.objects.filter(ISBN13 = value)
		related_book_ob.extend(book_ob)

	related_book_ob_sort = sale_num(related_book_ob)
	return related_book_ob_sort


def sale_num(book_ob_list):
	book_sale_class_list = []
	for value in book_ob_list:
		sum = 0
		order_book = bookinfo.objects.filter(ISBN13 = value)
		for ob in order_book:
			sum = sum + ob.copy
		book_sale_class1 = book_sale_class(value, sum)
		book_sale_class_list.append(book_sale_class1)
	length = len(book_sale_class_list)
	for i in range(length):
		for j in range(1, length-i):
			if book_sale_class_list[j-1].sale_num < book_sale_class_list[j].sale_num:
				book_sale_class_list[j-1], book_sale_class_list[j] = book_sale_class_list[j], book_sale_class_list[j-1]

	return book_sale_class_list


def migrate_data(cart_host_ob,  cart_LIST):
	'''Migrate cart data into order table'''
	timestamp = str(time.time())
	num = len(orderinfo.objects.all())
	order_num = num +1
	order1 = orderinfo(oid = order_num,
					login_name = cart_host_ob,
					date = timestamp,
					status = 'default' )
	order1.save()
	order_oid_ob = orderinfo.objects.get(oid = order_num)

	for value in cart_LIST:
		f_ISBN = books.objects.get(ISBN13=value.ISBN13.ISBN13)
		bookinfo1 = bookinfo(oid = order_oid_ob,
							ISBN13 = f_ISBN,
							copy = value.copy)
		bookinfo1.save()

	return None

def erase_cart(cart_host_ob):
	'''Erase shop cart data'''
	erase1 = shop_cart.objects.filter(login_name = cart_host_ob)
	erase1.delete()

	return None


def shop_cart_item_delete(username,ISBN13,copy):
	log_name = customers.objects.get(full_name = username)
	book = books.objects.get(ISBN13 = ISBN13)
	erase2 = shop_cart.objects.filter(login_name = log_name.login_name, ISBN13 = book.ISBN13)
	erase2.delete()

	book.inventory = book.inventory + int(copy)
	book.save()

	return None


def genetate_order_plus_book(username):
	user = customers.objects.get(full_name = username)
	usr_order = orderinfo.objects.filter(login_name = user.login_name)
	order_book_class_list = []
	for value in usr_order:
		value.date = time.strftime("%Y-%m-%d",time.localtime(float(value.date)))
		usr_book_ob = []
		usr_book = bookinfo.objects.filter(oid = value.oid)
		for bookinfo_ob in usr_book:
			book = books.objects.filter(ISBN13 = bookinfo_ob.ISBN13.ISBN13)
			usr_book_ob.extend(book)
		class1 = order_book_class(value, usr_book_ob)
		order_book_class_list.append(class1)
	return order_book_class_list
	

	
def find_usr_info(username):
	user = customers.objects.get(full_name = username)
	order_book_class_list = genetate_order_plus_book(username)
	feed_list = feedback.objects.filter(login_name = user.login_name)
	usr_feedback = feedback_gene_sort(feed_list)
	usr_rate_history = rated_feedback(username)

	usr_info_dict = {'username': user, 
						'usr_order' : order_book_class_list, 
						'usr_feedback' : usr_feedback,
						'usr_rate_history':usr_rate_history}
	return usr_info_dict

def rated_feedback(username):
	'''find out all feedbacks you have rated, and sorted them by usefulness'''
	user = customers.objects.get(full_name = username)
	rated_feedback_list = rate.objects.filter(login_name = user)
	rate_feedback_class_list = []
	for value in rated_feedback_list:

		rated_feedback_ob = feedback.objects.get(fid = value.fid.fid)

		rate_feedback_class1 = rate_feedback_class(value, rated_feedback_ob)
		rate_feedback_class_list.append(rate_feedback_class1)

	length = len(rate_feedback_class_list)
	for i in range(length):
		for j in range(1, length-i):
			if rate_feedback_class_list[j-1].rate_ob.rscore < rate_feedback_class_list[j].rate_ob.rscore:
				rate_feedback_class_list[j-1], rate_feedback_class_list[j] = rate_feedback_class_list[j], rate_feedback_class_list[j-1]

	usr_rate_history_class = rate_feedback_class_list

	return usr_rate_history_class


def order_page_info(username):
	info_dict_temp = genetate_order_plus_book(username)
	if len(info_dict_temp)==0:
		info_dict = {'No_ORDER' : 'No Generated Order yet!'}
	else:
		info_dict = {'info_dict_class' : info_dict_temp}

	return info_dict

def feedback_gene_sort(feed_list):

	feedback_ave = []
	for value in feed_list:
		rate_list = rate.objects.filter(fid = value.fid)
		sum = 0
		average = 0.0

		if len(rate_list)==0:
			pass
		else:
			for rate_ob in rate_list:
				sum = sum + rate_ob.rscore
			average = float(sum) / float(len(rate_list))
		feedback_ave1 = feedback_ave_score_class(value, average)
		feedback_ave.append(feedback_ave1)
	length = len(feedback_ave)
	for i in range(length):
		for j in range(1, length-i):
			if feedback_ave[j-1].rate < feedback_ave[j].rate:
				feedback_ave[j-1], feedback_ave[j] = feedback_ave[j], feedback_ave[j-1]

	return feedback_ave



def book_recommand():
	#Find the sale record of each book, and return one order sorted in saling number
	BookSaleRecord = {}
	RecordNum = []
	orders = orderinfo.objects.all()
	for value in orders:
		BooksInOrder = bookinfo.objects.filter(oid = value)
		for book in BooksInOrder:
			if book.ISBN13.ISBN13 in BookSaleRecord:
				BookSaleRecord[book.ISBN13.ISBN13 ] = BookSaleRecord[book.ISBN13.ISBN13 ] + book.copy
			else:
				BookSaleRecord[book.ISBN13.ISBN13 ] = book.copy
	for k, v in BookSaleRecord.items():
		RcecordClass1 = BookRecord(k,v)
		RecordNum.append(RcecordClass1)
	length = len(RecordNum)
	for i in range(length):
		for j in range(1, length-i):
			if RecordNum[j-1].NUM < RecordNum[j].NUM:
				RecordNum[j-1], RecordNum[j] = RecordNum[j],RecordNum[j-1]
	return RecordNum

def sort_search_result(search_result_temp, sorted_way):
	'''sort the search result by the way you choose,sorted_way='1', means sort by Publish Date,'2' means sort by score

	'''

	if sorted_way=='1':
		length = len(search_result_temp)
		for i in range(length):
			for j in range(1, length-i):
				if int(search_result_temp[j-1].pubDate[-4:]) < int(search_result_temp[j].pubDate[-4:]):
					search_result_temp[j-1], search_result_temp[j] = search_result_temp[j],search_result_temp[j-1]

		sorted_result = search_result_temp
		print len(sorted_result)
		return sorted_result

	else:
		book_score_list = []
		for value in search_result_temp:
			sum = 0.0
			aver_score = 0.0
			feedback_book_list = feedback.objects.filter(ISBN13 = value.ISBN13)
			if len(feedback_book_list)==0:
				book_score_class1 = book_score_class(value, aver_score)
				book_score_list.append(book_score_class1)
			else:	
				for feedback_ob in feedback_book_list:
					sum = sum + float(feedback_ob.fscore)
				aver_score = sum/float(len(feedback_book_list))
				book_score_class1 = book_score_class(value, aver_score)
				book_score_list.append(book_score_class1)
		length = len(book_score_list)
		for i in range(length):
			for j in range(1, length-i):
				if book_score_list[j-1].aver_score < book_score_list[j].aver_score:
					book_score_list[j-1], book_score_list[j] = book_score_list[j],book_score_list[j-1]

		sorted_result = book_score_list
		return sorted_result


def best_seller_last_month():
	'''To find order for last month, and do some sortting '''
	order_last_month = []
	book_list = []
	book_count = {}
	author_count = {}
	publisher_count = {}

	Book_Num_Record = []
	Author_Num_Record = []
	Punlisher_Num_Record = []
	time_now = time.strftime('%Y%m',time.localtime(time.time()))
	if time_now[-2:]=='01':
		time_last_month = str(int(time_now[:4])-1) + '12'
	else:
		if int(time_now[-2:]) > 10:
			time_last_month = time_now[:4] + str(int(time_now[-2:])-1)
		else:
			time_last_month = time_now[:4] + '0' + str(int(time_now[-2:])-1)

	order_ob_list = orderinfo.objects.all()
	for value in order_ob_list:
		date_format = time.strftime("%Y%m",time.localtime(float(value.date)))
		if time_last_month==date_format:
			order_last_month.append(value)
	for value in order_last_month:
		book_one_order = bookinfo.objects.filter(oid = value)
		book_list.extend(book_one_order)

	for value in book_list:
		if value.ISBN13.ISBN13 in book_count:
			book_count[value.ISBN13.ISBN13] = book_count[book.ISBN13.ISBN13 ] + value.copy
		else:
			book_count[value.ISBN13.ISBN13] = value.copy

		if value.ISBN13.authors in author_count:
			author_count[value.ISBN13.authors] = author_count[book.ISBN13.authors ] + value.copy
		else:
			author_count[value.ISBN13.authors] = value.copy

		if value.ISBN13.publisher in publisher_count:
			publisher_count[value.ISBN13.publisher] = publisher_count[book.ISBN13.publisher ] + value.copy
		else:
			publisher_count[value.ISBN13.publisher] = value.copy

	for k, v in book_count.items():
		book_ob = books.objects.get(ISBN13 = k)
		BookClass1 = BookRecord(book_ob,v)
		Book_Num_Record.append(BookClass1)

	for k, v in author_count.items():
		BookClass2 = BookRecord(k,v)
		Author_Num_Record.append(BookClass2)

	for k, v in publisher_count.items():
		BookClass3 = BookRecord(k,v)
		Punlisher_Num_Record.append(BookClass3)


	length = len(Book_Num_Record)
	for i in range(length):
		for j in range(1, length-i):
			if Book_Num_Record[j-1].NUM < Book_Num_Record[j].NUM:
				Book_Num_Record[j-1], Book_Num_Record[j] = Book_Num_Record[j],Book_Num_Record[j-1]

	length = len(Author_Num_Record)
	for i in range(length):
		for j in range(1, length-i):
			if Author_Num_Record[j-1].NUM < Author_Num_Record[j].NUM:
				Author_Num_Record[j-1], Author_Num_Record[j] = Author_Num_Record[j],Author_Num_Record[j-1]

	length = len(Punlisher_Num_Record)
	for i in range(length):
		for j in range(1, length-i):
			if Punlisher_Num_Record[j-1].NUM < Punlisher_Num_Record[j].NUM:
				Punlisher_Num_Record[j-1], Punlisher_Num_Record[j] = Punlisher_Num_Record[j],Punlisher_Num_Record[j-1]

	dict_stastics = {'Book_Num_Record' : Book_Num_Record,
								'Author_Num_Record' : Author_Num_Record,
								'Punlisher_Num_Record' : Punlisher_Num_Record}
	return  dict_stastics
