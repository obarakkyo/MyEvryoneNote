from django.shortcuts import render

# Create your views here.
def userlogapp_base(request):
    return render(request, 'userlogapp/login.html', context={})