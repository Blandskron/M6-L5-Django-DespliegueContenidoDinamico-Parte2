from django.shortcuts import render

def index(request):
    context = {
        'message': 'Bienvenido a EduDashboard',
        'description': 'Esta plataforma te ayuda a organizar información educativa de manera sencilla.',
        'cta': 'Explorar Estudiantes',
        'cta_link': '/estudiantes/'
    }
    return render(request, 'edu_app/index.html', context)
