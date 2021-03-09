from django.urls import path
from.import views
app_name = 'myapp'

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("", views.TemplateView, name="index"),
    path("carsview", views.AllCarView, name="carsview"),
    path("addcar", views.AddCar, name="addcar"),
    path("editcar/<int:id>", views.UpdateCar, name="editcar"),
    path("deletecar/<int:id>", views.DeleteCar, name="deletecar"),
    
    #application url from here
    path("appsview", views.AllApplicationView, name="appsview"),
    path("addapps", views.AddApplication, name="addapps"),
    path("editapps/<int:id>", views.UpdateApplication, name="editapps"),
    path("deleteapps/<int:id>", views.DeleteApplication, name="deleteapps"),
    path("modelview", views.ModelViewOnly, name="modelview"),
]