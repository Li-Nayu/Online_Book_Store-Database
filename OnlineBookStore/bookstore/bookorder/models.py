#filename:models.py
#-*-coding:utf-8-*-


from django.db import models
from django.contrib.auth.models  import User


class books(models.Model):
    ISBN13 = models.CharField(maxlength = 14, primary_key = True)
    ISBN10 = models.CharField(maxlength = 10)
    title = models.CharField(maxlength = 100)
    authors = models.CharField(maxlength = 50)
    publisher = models.CharField(maxlength = 100)
    pubDate = models.CharField(maxlength = 20)
    language = models.CharField(maxlength = 20) # additive attribute
    cover = models.CharField(maxlength = 100) # additive attribute
    inventory = models.IntegerField()
    price = models.CharField(maxlength = 10)
    bookFormat = models.CharField(maxlength = 10)
    # check(bookFormat = 'hardcover' or bookFormat = 'softcover')
    keywords = models.CharField(maxlength = 100)
    subject = models.CharField(maxlength = 100)
    def __unicode__(self):
        return u'%s' %(self.fname)
    class Admin:
        pass

class customers(models.Model):
    '''
    #when register, we should create one functionto generate this table items.
    '''

    login_name = models.CharField(maxlength = 20, primary_key = True) #login_name use the email
    full_name = models.CharField(maxlength = 50)
    #password = models.CharField(maxlength = 20)
    '''
    NO password in customers table
    '''
    address = models.CharField(maxlength = 200)
    phone_number = models.CharField(maxlength = 20)
    credit_card= models.CharField(maxlength = 50)
    def __unicode__(self):
        return u'%s' %(self.cname)


class orderinfo(models.Model):
    oid = models.IntegerField(primary_key = True) #login_name + order number
    login_name = models.ForeignKey(customers, db_column = 'login_name')
    date = models.CharField(maxlength = 20)
    status  = models.CharField(maxlength = 20)
    def __unicode__(self):
        return u'%s,%s' %(self.tid, self.enrollment)

class bookinfo(models.Model):
    oid = models.ForeignKey(orderinfo,db_column = 'oid')
    ISBN13 = models.ForeignKey(books,db_column = 'ISBN13')
    # This is a many-to-many relationship.
    # Django will automatically add an IntegerField to holld the primary key.
    copy = models.IntegerField()
    def __unicode__(self):
        return u'%s' %(self.cname)

class feedback(models.Model):
    fid = models.CharField(maxlength = 100,primary_key = True) # fid = email + ISBN13
    login_name =  models.ForeignKey(customers, db_column = 'login_name')
    ISBN13 = models.ForeignKey(books,db_column = 'ISBN13')
    
    # This is a many to many relationship.
    fscore = models.IntegerField()
    # check(fscore >=1 and fscore <=10)
    text = models.CharField(maxlength = 550)
    def __unicode__(self):
        return u'%s' %(self.cname)


class rate(models.Model):
    login_name = models.ForeignKey(customers, db_column = 'login_name')
    fid = models.ForeignKey(feedback, db_column = 'fid')
    rscore = models.IntegerField()
    # This is a many to many relationship.
    # check(rscore >=1 and rscore <=3)
    def __unicode__(self):
        return u'%s' %(self.cname)

class shop_cart(models.Model):
    login_name = models.ForeignKey(customers, db_column = 'login_name')
    ISBN13 = models.ForeignKey(books,db_column = 'ISBN13')
    copy = models.CharField(maxlength = 2)
    def __unicode__(self):
        return u'%s' %(self.cname)