from rest_framework import serializers,validators
from .models import Employees,Projects,Qualifications,WorkExperience,addressDetails
#we need our data from the serverside to be rendered to the client side so that client to do that we need an API
# a client can either perform GET  request  or POST request the request reaches the server side through AJAX
# and the response they get will be JSON objects
# A client can either be another server or mobile apps
# 

  
class WorkExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkExperience
        fields = ['companyName','fromDate','toDate','address']
  

class QualificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qualifications
        fields = ['qualificationName','fromDate','toDate','percentage']
  
  


class ProjectsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = ['title','description']
  

class addressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = addressDetails
        fields = ['Hno','street','city','state']
  

class EmployeeSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(read_only=True, many =True)
    qualifications = QualificationSerializer(read_only=True, many =True)
    workexperience = WorkExperienceSerializer(read_only=True, many =True)
    addressdetails=addressDetailsSerializer(read_only=True, many =True)
    class Meta:
        model = Employees
        fields = ['id','name','email','age','gender','phoneNO','addressdetails','workexperience','qualifications','projects','photo']

        def create(self,validated_data):
            print('employee created')
            Employees.objects.create(**validated_data)

        def update(self,instance,validated_data):
            updatedEmployee = Employees(**validated_data)
            updatedEmployee.id = instance.id
            instance.save()
            return instance  
