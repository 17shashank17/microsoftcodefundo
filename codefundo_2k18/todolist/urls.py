from django.conf.urls import url
from todolist import views
app_name = "todolist"
 
urlpatterns = [
    url(r'^main_page/', views.main_page, name='main_page'),
   
   
]
