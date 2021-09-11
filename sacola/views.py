from django.shortcuts import render

# Create your views here.
def sacola_detail(request):
    return render(request, "sacola/sacola_detail.html")