from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer
from api.serializers import EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response  
# Create your views here.
#using drf automatic 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    #company/{companyId}/employees  #http://127.0.0.1:8000/api/v1/companies/1/employees/
    @action(detail=True, methods=['get'])   #annotation -> @action .... pk is must because detail is true
    def employees(self, request, pk=None):
        #print("get employees of ", pk, "company")
        try:     
          company = Company.objects.get(pk=pk)
          emps = Employee.objects.filter(company=company)
          emps_serializer = EmployeeSerializer(emps, many = True, context={'request':request})
          return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not exits !! Error '
            })
            
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer