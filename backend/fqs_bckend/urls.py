from django.urls import path 
from . import views 

app_name = "fqs"

urlpatterns = [  
    path("", views.index, name = "index"),
    path("new_session/", views.new_session, name = "session"),  
    path("to_do/", views.to_do, name = "todo"), 
    path("qr_display/", views.qr_display, name = "qr")
]