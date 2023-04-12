from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.index, name = "index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.read, name='read'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
