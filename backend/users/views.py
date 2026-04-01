from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#importing chatbot
from django.http import JsonResponse
import json
from .ai_chatbot.main import get_ai_response

# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password =request.POST['password']

        #django thorows eror if the same username is used so handleling that
        if User.objects.filter(username=username).exists():
            return render(request, "users/signup.html",{
                "error":"Username already exists"
            })

        user=User.objects.create_user(username=username,password=password)
        # user.save()#You don't need this line:User.objects.create_user()->already saves the user.
        return redirect('login')
    #this is for get req -> when visiting the web
    return render(request,"users/signup.html")
    
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username, password=password)
        #chekc the DB for username and pass if it has return user obj if not return None


        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request, "users/login.html", {
                "error": "User does not exist or password incorrect"
            })
        # login() creates a session and logs the user into the website.
        # After this:
        # Django stores the user ID in the session
        # The user stays logged in across pages
    
    # this handles GET request
    return render(request, "users/login.html")
    

@login_required#a decorator. It is used to protect a view so only logged-in users can access it.
def dashboard(request):#a dashboard is a page shown after a user logs in.
    return render(request,"users/dashboard.html")

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def chatbot(request):
    return render(request,"users/chatbot.html")


#this is for chatbot
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

from .ai_chatbot.main import get_ai_response


# 👉 UI PAGE
def chatbot_page(request):
    return render(request, "users/chatbot.html")


# 👉 API (your existing one — NO CHANGE)
@csrf_exempt
def ask_ai(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get("query")

            if not query:
                return JsonResponse({"error": "No query provided"}, status=400)

            response = get_ai_response(query)

            return JsonResponse(response)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)