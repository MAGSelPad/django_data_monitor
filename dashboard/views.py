from django.shortcuts import render

def dashboard_home(request):
    """Renderiza la página principal del dashboard."""
    data = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/index.html', data)
