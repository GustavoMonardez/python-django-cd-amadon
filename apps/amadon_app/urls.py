from django.conf.urls import url 
from . import views

urlpatterns=[
    url(r"^$", views.index),
    url(r"^amadon_app$", views.index),
    url(r"^amadon_app/buy$", views.buy),
    url(r"^amadon_app/checkout$", views.checkout)
]