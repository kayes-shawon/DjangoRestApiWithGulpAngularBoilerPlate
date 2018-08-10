from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^account/$', views.AccountList.as_view(),
        name="accounts-list"),
]