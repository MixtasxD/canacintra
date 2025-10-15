from django.urls import path 
from.import views 
from core.views import *

app_name = "core"

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("identidad", views.identidad, name="identidad"),
    path("contactanos", views.contactanos, name="contactanos")
]