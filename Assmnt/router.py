#from rest_framework.routers import DefaultRouter
from api.viewsets import EmployeesViewset,QualificationViewset, addressDetailsViewset, projectViewset, workExperienceViewset
from rest_framework import routers
#here we are using the viewsets. viewsets is a class that specifies a variety of views when using our api


router =routers.DefaultRouter()
router.register('employees',EmployeesViewset)
router.register('address',addressDetailsViewset)
router.register('qualifications',QualificationViewset)
router.register('workexperience',workExperienceViewset)
router.register('projects',projectViewset)


# to check whats happening in our 
#you could uncomment it 
#for a in router.urls:
    #print(a,'\n')
# the above loop shows the URL_PATTERNS are configured for each models since it inherits ModelViewset