from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegForm,EventBookingForm,EventaddForm
from django.contrib.auth import authenticate,login,logout
from .models import event_category,Events,EventBooking
# Create your views here.


# def base(request):
#     return render(request,'base.html')

def homepage(request):
    event_c = event_category.objects.all()
    evnts = Events.objects.filter(admin_approval='approved')
    return render(request,'home.html',{'event_c':event_c,'evnts':evnts})

def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Login_page)
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
            return redirect(Login_page)
    else:
        form = UserRegForm()
    return render(request,'AdminReg.html',{'form':form})

def hoster_registr(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.role = 'hoster'
            data.save()
            return redirect(Login_page)
    else:
        form = UserRegForm()
    return render(request,'hoster_reg.html',{'form':form})


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
            if user.role == 'hoster':
                return redirect(hoster_dashbord)
    return render(request,'login.html')

def hoster_dashbord(request):
    if request.user.role != 'hoster':
        return redirect('error')
    if request.method == 'POST':
        form = EventaddForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            if data.admin_approval == 'pending':
                data.save()
                return redirect(waiting_approval)
            else:
                return HttpResponse('post added successfully')
        return render(request, 'hoster_page.html', {'form': form})
    form = EventaddForm()
    return render(request, 'hoster_page.html', {'form': form})

def waiting_approval(request):
    return render(request,'waiting_approv.html')

def pending_page(request):
    events = Events.objects.filter(admin_approval='pending')
    return render(request,'pending_page.html',{'events':events})

def user_dashbord(request):
    event_ca = event_category.objects.all()
    if request.user.role != 'user':
        return redirect(error)
    else:
        return render(request,'user_page.html',{'event_ca':event_ca})

def admin_dashbord(request):
    event = Events.objects.all()
    if request.user.role != 'admin':
        return redirect(error)
    else:
        return render(request,'admin_page.html',{'event':event})
    
def error(request):
    return render(request,'error.html')

def Logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect(homepage)
    else:
        return render(request,'logout.html')
    
def all_event(request,eid):
    events = Events.objects.filter(event_cat=eid)
    return render(request,'all_event.html',{'events':events})


def eventbooking(request, eid):
    even = Events.objects.get(id=eid)
    if request.method == 'POST':
        form = EventBookingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.name = even
            data.save()
            data.user.add(request.user)                                   
            return redirect(homepage)
    else:
        form = EventBookingForm()
    return render(request, 'eventbooking.html', {'form': form, 'even': even})


def EventBooked(request):
    eventss = EventBooking.objects.filter(user=request.user)
    return render(request,'bookedevents.html',{'eventss':eventss})

def Delet_event(request,eid):
    event = Events.objects.get(id=eid)
    if request.method == 'POST':
        event.delete()
        return redirect(admin_dashbord)
    else:
        return render(request,'delet_event.html')
    

def pending_notification(request):
    eventss = Events.objects.filter(admin_approval='pending').count()
    return render(request,'base.html',{'eventss':eventss})

def approve(request,pid):
    event = Events.objects.get(id=pid)
    event.admin_approval = 'approved'
    event.save()
    return redirect(pending_page)




