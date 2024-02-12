from django.contrib import admin
from django.urls import path
from applications import views

urlpatterns = [
    path('',views.index,name=""),
    path('sign/',views.signup,name="sign"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('create_task/',views.create_task,name="create_task"),
    path('view_task/',views.view_task,name="view_task"),
    path('update_task/<str:pk>/',views.update_task,name="update_task"),
    path('delete_task/<str:pk>',views.delete_task,name="delete_task"),
]
