from django.shortcuts import render

def natal(request):
    contexto = { 'natal': False }
    return render(request, 'natal.html', contexto)

def ano_novo(request):
    return render(request, 'ano_novo.html')