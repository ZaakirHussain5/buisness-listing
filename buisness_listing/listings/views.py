from django.shortcuts import render
from django.contrib.auth import get_user_model,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def signIn(request):
    if not request.method == 'POST':
        return JsonResponse({"error":"Method "+request.method+" not allowed"})
    username = request.POST["email"]
    password = request.POST["password"]

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            login(request,user)
            return JsonResponse({"message":"Login Successfull."})
        else:
            return JsonResponse({"error":"Login Failed Check your username and Password"})
    except UserModel.DoesNotExist:
        return JsonResponse({"error":"User not Found"})
    
    
