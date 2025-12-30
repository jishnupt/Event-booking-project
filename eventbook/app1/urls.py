from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base',base,name='base'),
    path('homepage',homepage,name='homepage'),
    path('RegisterUser',RegisterUser,name='RegisterUser'),
    path('AdminRegister',AdminRegister,name='AdminRegister'),
    path('Login_page',Login_page,name='Login_page'),
    path('user_dashbord',user_dashbord),
    path('admin_dashbord',admin_dashbord),
    path('error',error),
    path('Logout_page',Logout_page,name='Logout_page'),
    path('all_event/<int:eid>',all_event,name='all_event'),
    path('eventbooking/<int:eid>',eventbooking,name='eventbooking'),
    path('EventBooked',EventBooked,name='EventBooked')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)