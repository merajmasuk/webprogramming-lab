from django.shortcuts import render

# Create your views here.
def HelloWorld(request):
    return render(request, 'placeholder.html')
