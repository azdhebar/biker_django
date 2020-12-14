from django.urls import path,include
from account import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI,AccountView,user_find_servicerApi,VehicleView,UserView,ModelView,BrandView,VehicleView2,ServiceView,ServiceServicerView,ServiceDefaultView,FindServiceView
from rest_framework import routers
router = routers.DefaultRouter()
router.register("account",AccountView)
router.register('user',UserView)
router.register("model",ModelView)
router.register('vehicle_api',VehicleView2)
router.register('brand',BrandView)
router.register('service',ServiceDefaultView)

urlpatterns = [
    path('',views.index,name='index'),
    #servicer
    path('vehicles_servicer/',views.servicer_vehicle,name="servicer_vehicle"),
    path('delete_servicer/<int:id>',views.del_servicer,name="delete_servicer"),

    path('services_servicer/',views.servicer_services,name="servicer_services"),
    path('services_servicer/<int:id>',views.see_services,name="see_services"),
    path('cancel_service_servicer/<int:id>',views.servicer_can_service,name="can_service_servicer"),


    #user
    path('vehicles_user/',views.user_vehicle,name="vehicle_user"),
    path('delete_vehicle/<int:id>',views.delete_vehicle,name="vehicle_delete"),

    path('services_user/',views.user_service,name="user_services"),
    path('services_user/<int:id>',views.user_see_service,name="see_service_user"),

     path('find_servicer',views.user_find_servicer,name="find_service_user"),
     path('service_book/<int:id>/<int:vid>',views.user_book_service,name="book_service"),
     path('cancel_service/<int:id>',views.user_can_service,name="can_service"),



    #api  --
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/',include(router.urls)),
    path('api/vehicle/<str:username>', VehicleView.as_view(), name='vehicle'),
    path('api/service/user/<str:username>', ServiceView.as_view(), name='service_user'),
    path('api/service/servicer/<str:username>', ServiceServicerView.as_view(), name='service_servicer'),
    path('api/service/findservice/vehicle/<str:veh>/zip/<str:zip>', FindServiceView.as_view(), name='service_servicer'),
  


    
]
