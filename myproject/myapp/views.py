from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Car
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from guardian.shortcuts import get_objects_for_user,get_objects_for_group
from .models import Car , Application
from .forms import CarForm ,ApplicationForm



"""
User Login Here
"""
def login_request(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "myapp/signin.html",
                  context={"form":form})
"""
For the Logout
"""
@login_required(login_url='myapp:login')
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

"""
Table View Of data
for Support
"""
@login_required(login_url='myapp:login')
def TemplateView(request):
    data = get_objects_for_user(request.user,'myapp.can_view_brand_name_only')
    return render (request,"myapp/main.html",{'data':data})

@login_required(login_url='myapp:login')
def ModelViewOnly(request):
    data = get_objects_for_user(request.user,'myapp.can_view_model_no')
    return render (request,"myapp/modelviewonly.html",{'data':data})


@login_required(login_url='myapp:login')
def AllCarView(request):
    data = Car.objects.all()
    return render (request,"myapp/car/carsview.html",{'data':data})

@login_required(login_url='myapp:login')
def AddCar(request):
    form = CarForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return redirect('myapp:carsview')
    return render (request,"myapp/car/addcar.html",{'form':form})

@login_required(login_url='myapp:login')
def UpdateCar(request,id):
    data = Car.objects.get(id=id)
    form = CarForm(request.POST or None, instance = data)
    if form.is_valid(): 
        form.save()
        return redirect('myapp:carsview')
    return render (request,"myapp/car/editcar.html",{'form':form})

@login_required(login_url='myapp:login')
def DeleteCar(request,id):
    data = Car.objects.get(id=id)
    if request.method =="POST":
        data.delete()
        return redirect('myapp:carsview')
    return render(request, "myapp/car/deletecar.html",{'data':data}) 




"""
CRUD for Application Model
"""


@login_required(login_url='myapp:login')
def AllApplicationView(request):
    data = Application.objects.all()
    return render (request,"myapp/apps/appsview.html",{'data':data})

@login_required(login_url='myapp:login')
def AddApplication(request):
    form = ApplicationForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return redirect('myapp:appsview')
    return render (request,"myapp/apps/addapps.html",{'form':form})

@login_required(login_url='myapp:login')
def UpdateApplication(request,id):
    data = Application.objects.get(id=id)
    form = ApplicationForm(request.POST or None, instance = data)
    if form.is_valid(): 
        form.save()
        return redirect('myapp:appsview')
    return render (request,"myapp/apps/editapps.html",{'form':form})

@login_required(login_url='myapp:login')
def DeleteApplication(request,id):
    data = Application.objects.get(id=id)
    if request.method =="POST":
        data.delete()
        return redirect('myapp:appsview')
    return render(request, "myapp/apps/deleteapps.html",{'data':data}) 
