from .models import Employees,Qualifications,WorkExperience,Projects,addressDetails
from .serializers import EmployeeSerializer,QualificationSerializer,ProjectsSerializer,WorkExperienceSerializer,addressDetailsSerializer
from rest_framework import mixins , generics
from rest_framework import viewsets
from rest_framework.response import Response

'''
1)why modelview sets? the viewsets class calls the method internally so that you don't have to use mixins like
   listmixins or generic mixins.
2)All the methods are internally called when we inherit Modelviewset
3)makes it easier when we use nested serializers
'''
#Model viewset  
#in the viewsets we have  LIST, CREATE , RETRIEVE , UPDATE and DESTROY
# we can even do the PARTIAL UPDATE

class EmployeesViewset(viewsets.ModelViewSet):
    queryset=Employees.objects.all() 
    serializer_class=EmployeeSerializer
#here is whats happening above
# class EmployeesViewset(viewsets.Viewset)
#    def list(self,request):
#    queryset = Employee.objects.all()
#    serializer = EmployeeSerializer(queryset,many = True)
#    return Response(serializer.data)   


class QualificationViewset(viewsets.ModelViewSet):
    queryset=Qualifications.objects.all()
    serializer_class=QualificationSerializer


class addressDetailsViewset(viewsets.ModelViewSet):
    queryset=addressDetails.objects.all()
    serializer_class=addressDetailsSerializer



class workExperienceViewset(viewsets.ModelViewSet):
    queryset=WorkExperience.objects.all()
    serializer_class=WorkExperienceSerializer


class projectViewset(viewsets.ModelViewSet):
    queryset=Projects.objects.all()
    serializer_class=ProjectsSerializer 