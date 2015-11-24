from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.order_list, name='order_list'),
	url(r'^order/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
	url(r'^order/new/$', views.order_new, name='order_new'),
	url(r'^order/(?P<pk>[0-9]+)/edit/$', views.order_edit, name='order_edit'),
]