from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^transaction/head/$', views.TransactionHeadList.as_view(),
        name="accounts.transaction-head-list"),
]