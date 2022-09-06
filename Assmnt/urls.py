
#I tried using function based views got little verbose and some errors swithced back to CBV
#note I commented the views and created custorm viewsets.py in the app
#you will have api root view as home view



from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from api.views import employeeListView,employeeDetailView
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('api/employee/', employeeListView),
    #path('api/employee/<int:pk>/', employeeDetailView),
    path('',include(router.urls))
    

]


urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)