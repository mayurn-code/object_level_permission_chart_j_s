from django.urls import path, include
from .views import index
#  ViewPageForManager,ViewPageForSupervisor,ViewPageForOperator,ViewPageForSupport

urlpatterns = [
    path('',index, name = 'index'),
    # path('manager/',ViewPageForManager, name = 'managerpage'),
    # path('supervisor/',ViewPageForManager, name = 'supervisorpage'),
    # path('operator/',ViewPageForManager, name = 'operatorpage'),
    # path('support/',ViewPageForManager, name = 'supportpage'),
    path('accounts/',include('django.contrib.auth.urls')),
]