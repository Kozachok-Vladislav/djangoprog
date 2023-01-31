from django.urls import path, re_path

from .views import *


urlpatterns = {
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('vakansii/', vakansii, name=vakansii),
    path('post/<int:post_id>/', news , name='post'),
}