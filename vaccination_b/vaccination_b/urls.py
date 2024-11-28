from django.urls import path
from .views import AdminRegister, AdminLogin, IndividualList, IndividualDetail # type: ignore

urlpatterns = [
    # Admin Registration and Login
    path('admin/register/', AdminRegister.as_view(), name='admin-register'),
    path('admin/login/', AdminLogin.as_view(), name='admin-login'),

    # CRUD Operations for Individuals
    path('individuals/', IndividualList.as_view(), name='individual-list'),
    path('individuals/<int:individual_id>/', IndividualDetail.as_view(), name='individual-detail'),
]
