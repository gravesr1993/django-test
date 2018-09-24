from .views import get_access_token,index,accounts,transactions,item
from django.conf.urls import url

urlpatterns=[
	url(r'^$', index, name='auth'),
	url(r'^get_access_token$', get_access_token, name='get_access_token'),
	url(r'^accounts$', accounts, name='accounts'),
	url(r'^transactions$', transactions, name='transactions'),
	url(r'^item$', item, name='item'),
]