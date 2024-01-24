from django.shortcuts import render

# Create your views here.
def mnvoice_base(request):
    return render(request, 'mnvoice/mnvoice.html', context={})