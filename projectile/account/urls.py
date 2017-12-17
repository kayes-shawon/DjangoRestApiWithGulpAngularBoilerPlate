from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^transaction/$', views.TransactionList.as_view(),
        name="accounts.transaction-list"),
]