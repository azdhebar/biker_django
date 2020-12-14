from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from account.models import Account
from django.http import HttpResponse
from django.contrib.auth.models import  User
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        return render(request,'shared/page/home.html')

def about(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        return render(request,'shared/page/about.html')

def contact(request):
    if request.user.is_authenticated:   
        return redirect('/account')
    else:
        return render(request,'shared/page/contact.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:   
        if request.method=="POST":
            username = request.POST["username"]
            password= request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/account')
            else:
                return render(request,'shared/page/signin.html',{"msg":"Username/Password are incorrect!!","type":"error"})
        else:
            return render(request,'shared/page/signin.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/account')    
    else:
        if request.method=="POST":
            username = request.POST["username"]
            email = request.POST['email']
            password= request.POST['password']
            mobile = request.POST['mobile']
            repassword = request.POST['repassword']
            ad_fl = request.POST['ad_fl']
            ad_sl = request.POST['ad_sl']
            city  = request.POST['city']
            zip= request.POST['zip']
            try:
                servicer = request.POST['servicer']
            except:
                servicer="False"
            if password!=repassword:
                return render(request, 'shared/page/register.html',{"msg":"Password doesn't match!","type":"error"})
            else:
                try:
                    user = User.objects.create_user(username,email,password)
                    user.save()
                    flag=False
                    if servicer=="True":
                        flag=True
                    account = Account(user=user,is_servicer=flag,address_fl=ad_fl,address_sl=ad_sl,city=city,zip=zip,mobile=mobile)
                    account.save()

                except Exception as e:
                    return render(request, 'shared/page/register.html', {"msg": "Something went wrong!", "type": "error"})
                return redirect('/signin')


        else:
            return render(request,'shared/page/register.html')





def logout_ac(request):
    logout(request)
    return redirect('/signin')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        ac = Account.objects.get(user=request.user)
        if request.method=="POST":
            ad_fl = request.POST["ad_fl"]
            ad_sl = request.POST["ad_sl"]
            city = request.POST["city"]
            zip = request.POST["zip"]
            ac.address_fl = ad_fl
            ac.address_sl =ad_sl
            ac.city = city
            ac.zip = zip
            ac.save()
            return redirect('profile')

        else:
            
            context={
                "account":ac
            }
            return render(request,'shared/page/profile.html',context)  
