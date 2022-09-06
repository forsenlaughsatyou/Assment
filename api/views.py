'''from urllib import response
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Employees,WorkExperience,Qualifications,Projects
from .serializers import EmployeeSerializer,addressDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics,status


# Create your views here.
@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == 'GET':
       employees = Employees.objects.all()
 
       serializer = EmployeeSerializer(employees, many=True)
       return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        else:
            return response(serializer.errors)    

       



@api_view(['DELETE', 'GET' ,'PUT'])
def employeeDetailView(request,pk):
        
        try:
            employee = Employees.objects.get(pk=pk)
           
        except Employees.DoesNotExist:
              return HttpResponse(status=404)

      
        if request.method == "DELETE":
            data={}
            try:
               employee.delete()
               data["success"]='employee deleted successfully'
               return response(data=data)
            
            except:   
               return response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "GET":
            serializer=EmployeeSerializer(employee)
            return  Response (serializer.data)
        
        elif request.method == "PUT":
            serializer = EmployeeSerializer(employee,data=request.data)
            data={}
            if serializer.is_valid():
               serializer.save()
               data["success"]="updated successfully"
               return response(data=data)
            return response(serializer.errors,status=status.HTTP_202_ACCEPTED)'''
            
                  

