from django.urls import path
from.import views
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.sign_in,name='sign_in'),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('logout/',views.sign_out,name='sign_out'),
]