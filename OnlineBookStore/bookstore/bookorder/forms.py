import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import newforms as forms


class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(
		label='Password',
		widget=forms.PasswordInput()
	)
	password2 = forms.CharField(
		label='Password (Again)',
		widget=forms.PasswordInput()
	)

	def clean_password2(self):
		if 'password1' in self.clean_data:
			password1 = self.clean_data['password1']
			password2 = self.clean_data['password2']
			if password1 == password2:
				return password2
		raise forms.ValidationError('Passwords do not match.')

	def clean_username(self):
		username = self.clean_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username can only containalphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')

class SearchForm(forms.Form):
	search_key = forms.CharField(label='search_key', max_length=30)

class order_book_class(forms.Form):
	def __init__(self,order_ob,book_ob_list):
		self.order_ob = order_ob
		self.book_ob_list = book_ob_list


class feedback_ave_score_class(forms.Form):
	def __init__(self,feedback_ob, rate):
		self.feedback_ob = feedback_ob
		self.rate = rate

class BookRecord(forms.Form):
	def __init__(self,ISBN,NUM):
		self.ISBN = ISBN
		self.NUM = NUM

class rate_feedback_class(forms.Form):
	def __init__(self,rate_ob, feeedback_ob):
		self.rate_ob = rate_ob
		self.feeedback_ob = feeedback_ob

class book_score_class(forms.Form):
	def __init__(self, book_ob, aver_score):
		self.book_ob = book_ob
		self.aver_score = aver_score

class book_sale_class(forms.Form):
	def __init__(self, book_ob, sale_num):
		self.book_ob = book_ob
		self.sale_num = sale_num

