from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name='homepage'),
    path('RegisterUser',RegisterUser,name='RegisterUser'),
    path('AdminRegister',AdminRegister,name='AdminRegister'),
    path('Login_page',Login_page,name='Login_page'),
    path('user_dashbord',user_dashbord),
    path('admin_dashbord',admin_dashbord,name='admin_dashbord'),
    path('error',error,name='error'),
    path('Logout_page',Logout_page,name='Logout_page'),
    path('all_event/<int:eid>',all_event,name='all_event'),
    path('eventbooking/<int:eid>',eventbooking,name='eventbooking'),
    path('EventBooked',EventBooked,name='EventBooked'),
    path('hoster_registr',hoster_registr,name='hoster_registr'),
    path('hoster_dashbord',hoster_dashbord,name='hoster_dashbord'),
    path('Delet_event/<int:eid>',Delet_event,name='Delet_event'),
    path('pending_page',pending_page,name='pending_page'),
    path('pending_notification',pending_notification),
    path('waiting_approval',waiting_approval),
    path('approve/<int:pid>',approve,name='approve')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)