from django.http import HttpResponse
from django.shortcuts import render  # import render

def awal(request):
    return HttpResponse("Berhasil diinstal")

def home(request):
    title = "Halaman Home"  # variabel title
    context = {
        'title': title
    }
    return render(request, 'home.html', context)
