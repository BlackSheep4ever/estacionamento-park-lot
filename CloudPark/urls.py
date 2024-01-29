from django.urls import re_path as url
from CloudPark import views

urlpatterns = [
    url(r'^api/v1/customer$',views.customerApi),
    url(r'^api/v1/customer/([0-9]+)$',views.customerApi),

    url(r'^api/v1/vehicle$',views.vehicleApi),
    url(r'^api/v1/vehicle/([0-9]+)$',views.vehicleApi),
    
    url(r'^api/v1/plan$',views.planApi),
    url(r'^api/v1/plan/([0-9]+)$',views.planApi),

    url(r'^api/v1/contract$',views.contractApi),
    url(r'^api/v1/contract/([0-9]+)$',views.contractApi),

    url(r'^api/v1/customervehicle$',views.vehicleApi),
    url(r'^api/v1/customervehicle/([0-9]+)$',views.vehicleApi),

    url(r'^api/v1/customerplan$',views.customer_planApi),
    url(r'^api/v1/customerplan/([0-9]+)$',views.customer_planApi),

    url(r'^api/v1/parkmovement$',views.parkmovementApi),
    url(r'^api/v1/parkmovement/([0-9]+)$',views.parkmovementApi),
]