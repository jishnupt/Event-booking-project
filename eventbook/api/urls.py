from django.urls import path
from .views import *

urlpatterns = [
    path('allevents',allevents),
    path('AddEvents',AddEvents),
    path('DeletEvent/<int:sid>',DeletEvent)
]