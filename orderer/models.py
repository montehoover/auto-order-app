from django.db import models
# from django.utils import timezone

# A simple representation of a recuring order.  Each instance represents
# a single product from amazon based on the amazonid.  The only modifications
# possible are the quantity of the item to be bundled into a recurring order.
# The user will specify when to receive the first shipment and then at what
# intervals to recieve the item(s).
class ScheduledOrder(models.Model):
	customer = models.ForeignKey('auth.User')
	amazonid = models.CharField(max_length=200)
	quantity = models.IntegerField()
	# User will see order frequency as "Order every 6 weeks"
	# with "6" being <frequency_qty> and "weeks" being <frequency_unit>
	frequency_qty = models.IntegerField(default=1)
	frequency_unit = models.CharField(default="Month", max_length=200)
	start_date = models.DateField(blank=True, null=True)
#	stop_date = models.DateField(blank=True, null=True)

	def add_order(self):
		self.save()

	def __str__(self):
		return self.amazonid


# I initially thought I tried to create a relational database, but
# realized that to start with I only need a simple representation
# of ongoing scheduled orders.  More will be necessary later though.

# class Order(models.Model):
# 	# django gives default primary key in the form:
# 	# id = models.AutoField(primary_key=True)
# 	customer = models.ForeignKey('auth.User')
# 	order_date = models.DateTimeField(blank=True, null=True)

# 	def place_order(self):
# 		self.order_da

# # Junction table between an order and the items in it
# class OrderItem(models.Model):
# 	order = models.ForeignKey('Order')
# 	#customer = models.ForeignKey('auth.User')
# 	#order_date = models.DateTimeField(blank=True, null=True)
# 	item = models.ForeignKey('Item')
# 	quantity = models.IntegerField()

# class Item(models.Model)
# 	amazonid = models.CharField(primary_key=True, max_length=200)
