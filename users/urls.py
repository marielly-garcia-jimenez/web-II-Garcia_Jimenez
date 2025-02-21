from django.urls import path
from .views import usersIndex
from . import views
urlpatterns = [
    path('', usersIndex, name='users_index'),
    path("create", views.createUserView, name="create"),
    path("createUser", views.createUser, name="createUser"),
    path("details/<int:id>", views.userDetail, name="userDetail"),
    path("createUser-by-fetch", views.createUserByFetch, name="crateUser-by-fetch")
    
]