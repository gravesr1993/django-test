from .views import PlaidView, get_access_token,index
from django.conf.urls import url

urlpatterns=[
	url(r'^$', PlaidView.as_view(), name='auth'),
	url(r'^$', index, name='auth'),
	url(r'^get_access_token$', get_access_token, name='get_access_token')
]