from django.db import models

#not sure about double primary key
class Author(models.Model):
    unique_together = ("name", "address")
    name = models.CharField(max_length=255, primary_key=True) 
    address = models.CharField(max_length=255, primary_key=True) #primary key
    url = models.CharField(max_length=255)

class Book(models.Model):
    isbn = models.CharField(max_length=255, primary_key=True)
    year = models.IntegerField(10)
    title = models.CharField(max_length=255)
    price = #check 
    author_name = models.ForeignKey(Author.name)
    author_address = models.ForeignKey(Author.address)
    publisher_name = models.ForeignKey(Publisher.name)

class Publisher(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    url = models.IntegerField(10)

class Warehouse(models.Model):
    code = models.IntegerField(10, primary_key=True)
    address = models.CharField(max_length=255) 
    phone = models.CharField(max_length=255)

class Customer(models.Model):
    email = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class ShoppingBasket(models.Model):
    id = models.IntegerField(10, primary_key=True)
    customer_email = models.ForeignKey(Customer.email)


#TO DO:
#Primary key adjustment
#WarehouseBook join table
#ShoppingBasketBook join table