from django.shortcuts import render
from .models import Reporte

def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'reportes/lista_reportes.html', {'reportes': reportes})
