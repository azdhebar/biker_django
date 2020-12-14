from account.models import Account
from service.models import Service
from servicer.models import Servicer
def get_user(request):
    try:
        ac = Account.objects.get(user=request.user)
        if ac.is_servicer:
            context ={
                "servicer":True
                }
        else:
            context ={
                "servicer":False
                }
    except Exception as e:
        context ={
                "servicer":False
                }
        
    return context  

def get_numbers(request):
    try:
        ac = Account.objects.get(user=request.user)
        servicer = Servicer.objects.filter(user=ac).count()
        service = Service.objects.filter(servicer=ac).count()
        context={
            "vehicles":servicer,
            "services":service,


        }

    except:
        context={
            "vehicles":0,
            "services":0,
        

        }

