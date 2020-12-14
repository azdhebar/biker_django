-------------------------------------------------------Requirements-------------------------------------
install python 3.8 or up
install django using pip install django
install pip install django-cors-headers
install pip install djangorestframework
install pip install markdown       # Markdown support for the browsable API.
install pip install django-filter  # Filtering support
install pip install django-rest-knox
install pip install pillow

--------------------------------------------------------------------------------------------------------


---------------------------------------------------STEPS TO START SERVER-----------------------------------

1. go to biker-master
2. run the command "python manage.py makemigrations"
3. run the command "python manage.py migrate"
4. run the command "python manage.py runserver"
5. So Server started

------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------API ---------------------------------------------------------------------
for login
METHOD:POST
http://127.0.0.1:8000/account/api/login/

for signup
METHOD:POST
http://127.0.0.1:8000/account/api/register/ (username,password,email) 
it gives whole user after success
after that you need to create account using that user
using POST METHOD and account url
 "account": "http://127.0.0.1:8000/account/api/account/",


please go to http://127.0.0.1:8000/account/api/
to test all the api
CRUD MODELS:{
    "account": "http://127.0.0.1:8000/account/api/account/",
    "user": "http://127.0.0.1:8000/account/api/user/",
    "model": "http://127.0.0.1:8000/account/api/model/",
    "vehicle_api": "http://127.0.0.1:8000/account/api/vehicle_api/",
    "brand": "http://127.0.0.1:8000/account/api/brand/",
    "service": "http://127.0.0.1:8000/account/api/service/"
}


to get All vehicles of one user:
    http://127.0.0.1:8000/account/api/vehicle/<username>

to find servicer which provide service of same model and in same zip code area
http://127.0.0.1:8000/account/api/service/findservice/vehicle/<vehicle:id>/zip/<zipcode>

