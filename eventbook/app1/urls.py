from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base',base,name='base'),
    path('RegisterUser',RegisterUser,name='RegisterUser'),
    path('AdminRegister',AdminRegister),
    path('Login_page',Login_page,name='Login_page'),
    path('user_dashbord',user_dashbord),
    path('admin_dashbord',admin_dashbord),
    path('error',error),
    path('Logout_page',Logout_page,name='Logout_page')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)