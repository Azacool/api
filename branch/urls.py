from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('workers/<int:branch_id>', views.workers),
    path('car/<int:branch_id>/<str:car_name>/',views.car),
    path('cars/<int:branch_id>/', views.cars),
]
