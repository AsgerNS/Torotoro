from django.urls import path
from .views import EmployeeList, EmployeeDetail, PositionList, PositionDetail, OrderList, OrderDetail, OrderStatusList

urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view()),
    path('positions/', PositionList.as_view()),
    path('positions/<int:pk>/', PositionDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('orders/status/<str:status>/', OrderStatusList.as_view()),
]
