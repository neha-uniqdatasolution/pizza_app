# import email
# from email import message
# from urllib import request
# from django.forms import PasswordInput
from django.http import HttpResponse
# from django.shortcuts import redirect, render
# from .models import Client, Menu, Order, counter
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth.backends import BaseBackend

# # Create your views here.


# def index(request):
#     count = counter.objects.get(id=1)
#     return render(request, 'index.html', {'count':count})

# def increment(request):
#     coun = counter.objects.get(id=1)
#     coun.num = int(coun.num) + 1
#     coun.save()
#     return redirect(request.META['HTTP_REFERER'])

# def decrement(request):
#     coun = counter.objects.get(id=1)
#     coun.num = int(coun.num) - 1
#     coun.save()
#     return redirect(request.META['HTTP_REFERER'])

# def reset(request):
#     coun = counter.objects.get(id=1)
#     coun.num = 0
#     coun.save()
#     return redirect(request.META['HTTP_REFERER'])

# def register(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         address = request.POST['address']
#         phone = request.POST['phone']

#         if Client.objects.filter(email=email).exists():
#             messages.error(request, 'Email is already exist')
#         else:

#             name = request.POST['name']
#             email = request.POST['email']
#             password = request.POST['password']
#             user = User(username=name, email=email, password=password)
#             user.save()
#             # User obj craete / obj get /  
#             # phone
#             client = Client(address=address, phone=phone, is_admin=False, USER=user)
#             client.save()
#             return redirect('/login/')
#     else:
#         pass
#     return render(request, 'register.html')

# def adminlogin(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         log_user = User.objects.get(email=email, password=password)
#         print("---------",log_user)
#         if log_user is not None:
#             nu_user = Client.objects.get(USER= log_user.id)
#             print(nu_user)
#             if nu_user.is_admin == True:    
#                 antct = authenticate(username=log_user.username, password=password)
#                 print("---===",antct)
#                 login(request, user=antct)
#                 return HttpResponse("this is admin")
#                 # return redirect('/adminhomepage/')
#             elif nu_user.is_admin == False:
#                 request.session['email'] = log_user.email
#                 return HttpResponse("this is user")
#                 # return redirect('/clienthome/')

#     else:        
#         return render(request, 'login.html')

# def adminhome(request):
#     pass


# def clienthome(request):
#     pass

def helo(request):
    return HttpResponse("helo")
    