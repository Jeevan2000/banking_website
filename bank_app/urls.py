from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('customers',views.customers,name="customers"),
    path('transactionhistory',views.transactionhistory,name="transactionhistory"),
    path('custinfo/<int:id>/',views.custinfo),
    #path('custinfo/<int:id>/transaction',views.transaction)
]