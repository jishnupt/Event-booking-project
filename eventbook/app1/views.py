from django.shortcuts import render,redirect
from .forms import UserRegForm
from django.contrib.auth import authenticate,login,logout
from .models import event_category,Events
# Create your views here.


def base(request):
    return render(request,'base.html')

def homepage(request):
    event_c = event_category.objects.all()
    return render(request,'home.html',{'event_c':event_c})

def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(base)
    else:
        form = UserRegForm()
    return render(request,'Register.html',{'form':form})

def AdminRegister(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.role = 'admin'
            data.save()
            return redirect(base)
    else:
        form = UserRegForm()
    return render(request,'AdminReg.html',{'form':form})


def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if user.role == 'admin':
                return redirect(admin_dashbord)
            if user.role == 'user':
                return redirect(user_dashbord)
    return render(request,'login.html')

def user_dashbord(request):
    if request.user.role != 'user':
        return redirect(error)
    else:
        return render(request,'user_page.html')

def admin_dashbord(request):
    if request.user.role != 'admin':
        return redirect(error)
    else:
        return render(request,'admin_page.html')
    
def error(request):
    return render(request,'error.html')

def Logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect(base)
    else:
        return render(request,'logout.html')
    
def all_event(request,eid):
    events = Events.objects.filter(event_cat=eid)
    return render(request,'all_event.html',{'events':events})


