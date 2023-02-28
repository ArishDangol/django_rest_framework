
from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet
from api.views import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)  #r=> raw form
router.register(r'employees', EmployeeViewSet )

urlpatterns = [
    path('', include(router.urls))
]

#company/{companyId}/employees     ....custom url returns employees of company