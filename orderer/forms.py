from django import forms
from .models import ScheduledOrder

# A basic form for creating and editing ScheduledOrders
class OrderForm(forms.ModelForm):

	class Meta:
		model = ScheduledOrder
		fields = ('amazonid', 'quantity', 'frequency_qty', 'frequency_unit', 'start_date',)