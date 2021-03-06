from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from django.views.generic import DetailView,View,CreateView
from django.contrib.auth import get_user_model
from restaurants.models import RestaurantLocation
from django.contrib.auth.mixins import LoginRequiredMixin
from menus.models import Item
from .models import Profile
from .forms import RegisterForm
User=get_user_model()

def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.activated:
            	user_=profile.user
            	user_.is_active=True
            	user_.save()
            	profile.activation_key=None
            	profile.save()
            return redirect("/login/")
    return redirect("/")

class RegisterView(CreateView):
	form_class=RegisterForm
	template_name='registration/register.html'
	success_url='/'
	def dispatch(self,*args,**kwargs):
		if self.request.user.is_authenticated():
			return redirect("/logout/")
		return super(RegisterView,self).dispatch(*args,**kwargs)

class ProfileFollowToggle(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		username_to_toggle = request.POST.get("username").strip()
		profile_, is_following=Profile.objects.toggle_follow(request.user,username_to_toggle)
		return redirect(f"/u/{profile_.user.username}/")


class ProfileDetailView(DetailView):
	template_name='profiles/user.html'
	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username,is_active=True)
	def get_context_data(self, *args,**kwargs):
		context=super(ProfileDetailView,self).get_context_data(*args,**kwargs)
		user=context['user']
		is_following=False
		if user.profile in  self.request.user.is_following.all():
			is_following=True
		context['is_following']=is_following
		query = self.request.GET.get('q')
		items_exists=Item.objects.filter(user=user).exists()
		qs =RestaurantLocation.objects.filter(owner=user).search(query)
		if qs.exists() and items_exists:
			context['locations']= qs
		return context
