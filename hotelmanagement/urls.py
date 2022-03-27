
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from hotel_app import admin_urls,user_urls,manager_urls
from hotel_app.views import IndexView, RegisterView, LoginView, ViewDetails
from hotelmanagement import settings

urlpatterns = [
    path('admin/',admin_urls.urls()),
    path('user/',user_urls.urls()),
    path('manager/',manager_urls.urls()),
    path('',IndexView.as_view()),
    path('p',IndexView.as_view()),
    path('Register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('details',ViewDetails.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

