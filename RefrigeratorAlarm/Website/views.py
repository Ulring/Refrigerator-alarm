import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Temperature

# Create your views here.
def home(request) :
    tab = Temperature.objects.all()
    s = {'tab': tab}
    return render(request, 'tables.html', s)

def temperature(request):
    tab = Temperature.objects.all()
    s = {'tab': tab}
    return render(request, 'tables.html', s)

class EditorChartView (TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = Temperature.objects.all()
        return context

def exp_csv(request):
    obj = Temperature.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=TEMPERATURE.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])
    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response
