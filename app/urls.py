from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    #PAGE URLS
    path("",views.ShowPage,name="showpage"),
    path("insert-page/",views.InsertPage,name="insertpage"),
    path("update-page/<int:pk>/",views.UpdatePage,name="updatepage"),
    #FUNCTIONALITITES URLS
    path("insert-data/",views.InsertData,name="insertdata"),
    path("update-data/<int:pk>/",views.UpdateData,name="updatedata"),
    path("delete-data/<int:pk>/",views.DeleteData,name="deletedata"),
]