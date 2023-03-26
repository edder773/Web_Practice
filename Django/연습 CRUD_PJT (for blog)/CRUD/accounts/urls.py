from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('unregister',views.unregister, name='unregister'),
    path('update/',views.update, name='update'),
    path('password/', views.password_change, name='password_change'),
]
 