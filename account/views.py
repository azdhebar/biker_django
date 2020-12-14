from django.shortcuts import render,redirect
from django.contrib.auth.models import  User
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from servicer.models import Servicer
from account.models import Account
from model.models import Models
import json
from service.models import Service
from rest_framework import generics, permissions,viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,AccountSerializer,VehicleViewSerializer,VehicleSerializer,UserSerializer,ModelSerializer,BrandSerializer,ServiceSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from vehicles.models import Vehicle
from model.models import Models
from brand.models import Brand


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        ac = Account.objects.get(user=request.user)
        if ac.is_servicer:
            servicer = Servicer.objects.filter(user=ac).count()
            service = Service.objects.filter(servicer=ac).count()
        else:
            servicer=Vehicle.objects.filter(user=ac).count()
            service=service = Service.objects.filter(user=ac).count()
        context={
            "vehicle":servicer,
            
            "service":service
        }
        return render(request,'account/page/index.html',context)


#servicer
#vehicle
def servicer_vehicle(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==False:
            return redirct('/')
        if request.method=="POST":
            model = request.POST['model']
            try:
                servicer_dup =Servicer.objects.get(model_fk=model,user=account)
            except:
                servicer_dup=None
            if servicer_dup is not None:
                model = Models.objects.all()
                servicers= Servicer.objects.filter(user=account)
                context={
                    "servicers":servicers,
                    "models":model,
                    "msg":"Model Is Already In Your Vehicles!!",
                    "type":"error"
                 }
                
                return render(request,'account/page/servicer/vehicles.html',context)
            else:
                model_pk = Models.objects.get(pk=model)
                servicer = Servicer(model_fk=model_pk,user=account)
                servicer.save()
                return redirect('servicer_vehicle')
        else:
            try:
                
                model = Models.objects.all()
                servicers= Servicer.objects.filter(user=account)
                context={
                    "servicers":servicers,
                    "models":model
                 }
                return render(request,'account/page/servicer/vehicles.html',context)

            except Exception as E:
                return HttpResponse(str(E))
        


def del_servicer(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==False:
            return redirct('/')
        try:
            servicer = Servicer.objects.get(pk=id)
            servicer.delete()
            return redirect('servicer_vehicle')
        except:
            return redirect('servicer_vehicle')
#-----------------------------------

#services
def servicer_services(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==False:
            return redirct('/')
        try:
            services= Service.objects.filter(servicer=account)
            context={
                "services":services,
             }
            return render(request,'account/page/servicer/services.html',context)

        except Exception as E:
            return HttpResponse(str(E))

def see_services(request,id):  

    if not request.user.is_authenticated:
        return redirect('/')
    else:
        
        account = Account.objects.get(user=request.user)
        if account.is_servicer==False:
            return redirct('/')
        service = Service.objects.get(pk=id,servicer=account)
        if request.method=="POST":
            try:
                remark = request.POST["remark"]
                service.remarks=remark
            except:
                remark =None
            try:
                accept = request.POST["accept"]
                service.accept=True
            except:
                service.accept =False
            try:
                solved = request.POST["solved"]
                service.solved =True
            except:
                service.solved =False
            
            try:
                service.save()
                return redirect('servicer_services')
                
            except:
                return redirect('servicer_services')
            
        else:
            try:
              
                context= {
                    "service":service
                }
                return render(request,'account/page/servicer/see_service.html',context)
            except Exception as e:
                return HttpResponse(str(e))   

def servicer_can_service(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        service = Service.objects.get(pk=id)
        if account.is_servicer==False:
            return redirct('/')
        else:
            service.cancel_servicer=True
            service.save()
            return redirect('servicer_services')

    

#user       "Ac
def user_vehicle(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==True:
            return redirct('/')
        if request.method=="POST":
            model = request.POST['model']
            vehicle_number = request.POST['vehicle_number']
            try:
                vehicle_dup =Vehicle.objects.get(vehicle_number=vehicle_number)
            except:
                vehicle_dup=None
            if vehicle_dup is not None:
                vehicles= Vehicle.objects.filter(user=account)
                models = Models.objects.all()
                context={
                    "vehicles":vehicles,
                    "models":models,
                    "msg":"Vehicle is Already Inserted!!",
                    "type":"error"
                 }
                
                return render(request,'account/page/user/vehicles.html',context)
            else:
                model_pk = Models.objects.get(pk=model)
                vehicle= Vehicle(user=account,vehicle_number=vehicle_number,model_fk=model_pk)
                vehicle.save()
                return redirect('vehicle_user')
        else:
            try:
                models = Models.objects.all()
                vehicles= Vehicle.objects.all()
                context={
                    "vehicles":vehicles,
                    "models":models,
                 }
                return render(request,'account/page/user/vehicles.html',context)

            except Exception as E:
                return HttpResponse(str(E))
        


def delete_vehicle(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==True:
            return redirct('/')
        try:
            
            vehicle = Vehicle.objects.get(pk=id)
            vehicle.delete()
            return redirect('vehicle_user')
        except:
            return redirect('vehicle_user')


def user_service(request):
     if not request.user.is_authenticated:
        return redirect('/')
     else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==True:
            return redirect('/')
        try:
            services= Service.objects.filter(user=account)
            context={
                "services":services,
             }
            return render(request,'account/page/user/services.html',context)

        except Exception as E:
            return HttpResponse(str(E))


def user_see_service(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==True:
            return redirct('/')
        
        service = Service.objects.get(pk=id,user=account)
        if request.method=="POST":
            try:
                review = request.POST["review"]
                service.review=review
            except:
                service.review=""
            
            try:
                service.save()
                return redirect('user_services')
                
            except:
                return redirect('user_services')
            
        else:
            try:
                vehicles = Vehicle.objects.filter(user=account)
              
                context= {
                    "vehicles":vehicles,
                    "service":service
                   
                }
                return render(request,'account/page/user/see_service.html',context)
            except Exception as e:
                return HttpResponse(str(e))   

    
def user_find_servicer(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        if account.is_servicer==True:
            return redirct('/')
        if request.method=="POST":
            try:
                vehicle= request.POST['vehicle']
                vehicle_pk = Vehicle.objects.get(pk=vehicle)
                print(vehicle_pk.model_fk)
                service_center = Account.objects.filter(is_servicer=True,zip=account.zip)
                service_center_vehicle=[]
                se = Servicer.objects.all()
                for s in se:
                    if s.model_fk==vehicle_pk.model_fk and s.user.is_servicer and s.user.zip==account.zip:
                        service_center_vehicle.append(s.user)

                v = Vehicle.objects.filter(user=account)
                print(service_center_vehicle)
                context={
                    "servicers":service_center_vehicle,
                    "vehicles":v,
                    "vehicle":vehicle_pk
                }
                return render(request,'account/page/user/find_servicer.html',context)
                    
            except Exception as E:
                return HttpResponse(str(E))

        else:
            v = Vehicle.objects.filter(user=account)
            context={
                "vehicles":v,
                
            }
            return render(request,'account/page/user/find_servicer.html',context)


def user_book_service(request,id,vid):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        servicer = Account.objects.get(pk=id)
        vehicle = Vehicle.objects.get(pk=vid)        
        account = Account.objects.get(user=request.user)
        if account.is_servicer==True:
            return redirct('/')
    
        if request.method=="POST":
            problem_image = request.FILES['problem_image']
            problem= request.POST['problem']
            vehicle.status=True
            vehicle.save()
            service  =Service(user=account,servicer=servicer,brand=vehicle.model_fk.brand,vehicle_fk=vehicle,model_fk=vehicle.model_fk,problem=problem,problem_image=problem_image)
            service.save()
            return redirect('user_services')
        else:
            try:
                if servicer.is_servicer:
                    context={
                        "servicer":servicer,
                        "vehicle":vehicle
                    }
                    return render(request,'account/page/user/book_service.html',context)
                else:
                    return redirect('/')
            except Exception as E:
                return HttpResponse(E)
            
def user_can_service(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        account = Account.objects.get(user=request.user)
        service = Service.objects.get(pk=id)
        if account.is_servicer==True:
            return redirct('/')
        else:
            service.cancel_user=True
            service.save()
            return redirect('user_services')

    
    
    


#USER API 

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
        "user": UserSerializer(user).data,
        "token": AuthToken.objects.create(user)[1]
        })


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    

class VehicleView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
            account = Account.objects.get(user=user)
            return Vehicle.objects.filter(user=account)
        except:
            return JsonResponse({"error":"User Not Found"})



class VehicleView2(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleViewSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'me':
            return Response(self.get_serializer(request.user).data)
        return super().retrieve(request, args, kwargs)


class ModelView(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    serializer_class = ModelSerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
            account = Account.objects.get(user=user)
            return Vehicle.objects.filter(user=account)
        except:
            return JsonResponse({"error":"User Not Found"})

class ServiceServicerView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
            account = Account.objects.get(user=user)
            return Service.objects.filter(servicer=account)
        except:
            return JsonResponse({"error":"User Not Found"})


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
            account = Account.objects.get(user=user)
            return Service.objects.filter(user=account)
        except:
            return JsonResponse({"error":"User Not Found"})


class ServiceDefaultView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer




class FindServiceView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def get_queryset(self):
        vehicle= self.kwargs['veh']
        zip= self.kwargs['zip']
        print(zip)
        vehicle_pk = Vehicle.objects.get(pk=vehicle)
        service_center_vehicle=[]
        se = Servicer.objects.all()
        
        for s in se:
            print(s.user.zip)
            print("VEHICLE_MODEL:{}".format(vehicle_pk.model_fk))
            print("SERVICER MODEL:{}".format(s.model_fk))
            if s.model_fk==vehicle_pk.model_fk and s.user.is_servicer and s.user.zip==zip:
                print(s.user)
                service_center_vehicle.append(s.user)
            print("SERVICE CENTER:{}".format(service_center_vehicle))
            data = serializers.serialize('json', service_center_vehicle)
        return service_center_vehicle
                    

def user_find_servicerApi(request,veh,zip):
    vehicle= veh
    zip= zip
    print(zip)
    vehicle_pk = Vehicle.objects.get(pk=vehicle)
    service_center_vehicle=[]
    se = Servicer.objects.all()
    
    for s in se:
        print(s.user.zip)
        print("VEHICLE_MODEL:{}".format(vehicle_pk.model_fk))
        print("SERVICER MODEL:{}".format(s.model_fk))
        if s.model_fk==vehicle_pk.model_fk and s.user.is_servicer and s.user.zip==zip:
            print(s.user)
            service_center_vehicle.append(s.user)
        print("SERVICE CENTER:{}".format(service_center_vehicle))
        data = serializers.serialize('json', service_center_vehicle)
    return HttpResponse(data, content_type="application/json")
#http://127.0.0.1:8000/account/api/service/findservice/vehicle/7/zip/565

