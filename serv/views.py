from django.shortcuts import render

# Create your views here.
def serv(request):
    context = {'serv':"active"}
    return render(request,"serv/services.html",context)