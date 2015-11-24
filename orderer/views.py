from django.shortcuts import render, get_object_or_404, redirect
from .models import ScheduledOrder
from .forms import OrderForm

# The default view.  Lists all currently scheduled orders.  Current orders
# can be selected to view in more detail or make changes.  Can add new orders
# from this view.
def order_list(request):
	orders = ScheduledOrder.objects.order_by('-start_date')
	return render(request, 'orderer/order_list.html', {'orders': orders})

# Show a scheduled order in detail and make changes if desired.
def order_detail(request, pk):
	order = get_object_or_404(ScheduledOrder, pk=pk)
	return render(request, 'orderer/order_detail.html', {'order': order})

# Present a form for making a new scheduled order.
def order_new(request):
	# If you are already on the form page and press the save button
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.customer = request.user
			order.save()
			return redirect('orderer.views.order_detail', pk=order.pk)
	# Else you just arrived at the form page and start with a blank form
	else:
		form = OrderForm()
	return render(request, 'orderer/order_edit.html', {'form': form})

# Present a form for making changes to a scheduled order (this html page is
# is used in the order_new view, as if you are simply editing an order that has
# no information in it yet.)
def order_edit(request, pk):
	order = get_object_or_404(ScheduledOrder, pk=pk)
	# If you are already on the form page and press the save button.
	if request.method == "POST":
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			order = form.save(commit=False)
			order.customer = request.user
			order.save()
			return redirect('orderer.views.order_detail', pk=order.pk)
	# Else you just arrived at the form page and will begin to edit the
	# existing order.
	else:
		form = OrderForm(instance=order)
	return render(request, 'orderer/order_edit.html', {'form': form})

