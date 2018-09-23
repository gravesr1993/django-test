"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from profiles.views import ProfileFollowToggle,RegisterView,activate_user_view
from menus.views import HomeView
from quickstartREST.views import UserViewSet,GroupViewSet
from rest_framework import routers
from restaurants.views import (RestaurantListView,RestaurantDetailView,RestaurantCreateView)
from django.views.generic import TemplateView

# for RESTFUL applications
# http://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    # Standard views via CFE tutorials
    url(r'^$', HomeView.as_view(),name="home"),
    url(r'^u/', include('profiles.urls',namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^restaurants/', include('restaurants.urls',namespace='restaurants')),
    url(r'^items/', include('menus.urls',namespace='menus')),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(),name="follow"),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # Activation view with slug
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view,name='activate'),
    # testing views
    url(r'^plaid/', include('plaidtest.urls',namespace='plaidtest')),
    url(r'^background-zoom/$', TemplateView.as_view(template_name='background-zoom.html'),name='background-zoom'),
    url(r'^parallax/$', TemplateView.as_view(template_name='parallax.html'),name='parallax'),
    url(r'^carousel/$', TemplateView.as_view(template_name='carousel.html'),name='carousel'),
    # RESTFUL API reroutes
    url(r'^', include(router.urls)),
]   #,email=settings.EMAIL_HOST_USER to access settings.py
