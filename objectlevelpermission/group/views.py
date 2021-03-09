from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from .decorators import allowed_users

"""
This is Index Page
and have some permissions
"""
def index(request):
    if request.user.is_authenticated:
        return render(request, 'group/index.html')


@login_required
@allowed_users(allowed_roles=['manager'])
def ViewPageForManager(request):
    if request.user.is_authenticated:

        is_manager = request.user.groups.filter(name='manager').exists()

    return render(request, 'group/manager.html',{'name':request.user.username, 'is_manager':is_manager})

@login_required
@allowed_users(allowed_roles=['supervisor'])
def ViewPageForSupervisor(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    return render(request, 'group/supervisor.html',{'name':request.user,"is_supervisor":is_supervisor})

@login_required
@allowed_users(allowed_roles=['operator'])
def ViewPageForOperator(request):
    is_operator = request.user.groups.filter(name='operator').exists()
    return render(request, 'group/operator.html',{'name':request.user, "is_operator":is_operator})


@login_required
@allowed_users(allowed_roles=['support  '])
def ViewPageForSupport(request):
    is_support = request.user.groups.filter(name='support').exists()
    return render(request, 'group/support.html',{'name':request.user,"is_support":is_support})