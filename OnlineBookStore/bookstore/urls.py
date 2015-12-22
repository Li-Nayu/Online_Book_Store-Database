#filename:urls.py
#-*-coding:utf-8-*-

import os.path
from django.conf.urls.defaults import *
from bookorder.views import *
#Changed!
from django.views.generic.simple import direct_to_template


site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
	(r'^$', main_page),
	(r'^user/(\w+)/$', user_page),
	(r'^login/$','django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^register/$', register_page),
	(r'^register/success/$', direct_to_template,
		{ 'template': 'registration/register_success.html' }),
	(r'^admin/', include('django.contrib.admin.urls')),
	(r'^book_page/(\d+)-(\d+)/$',book_page), #关于地址的匹配
	(r'^book_feedbacks/(\d+)-(\d+)/$',book_feedbacks), #关于地址的匹配
	(r'^modify_user_info/(\w+)/$',modify_user_info),
	(r'^shop_cart_page/(\w+)/$',shop_cart_page),
	(r'^order_page/(\w+)/$',order_page),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root': site_media }),

)