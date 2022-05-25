
import email
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

import csv
from .models import Form
from .filters import FormFilter
# Create your views here.

def aform(request):
    if request.method == 'POST':
        first= request.POST['first_name']
        second= request.POST['second_name']
        mail = request.POST['mail']
        contact = request.POST['phone']
        uni = request.POST['Auniversity']
        start_date = request.POST['Astart_date']
        end_date = request.POST['Aend_date']
        supervisor = request.POST['Asupervisor_name']
        department = request.POST['Adepartment_name']

        if Form.objects.filter(email=mail).exists():
            return redirect('home')
        else:
            Form.objects.create(
                first_name=first,
                second_name=second,
                email=mail,
                contact=contact,
                university=uni,
                start_date=start_date,
                end_date=end_date,
                supervisor=supervisor,
                department=department
            )
            return redirect('query')
    else:
        return render(request, 'form.html')

def query(request):
        f = FormFilter(request.POST, queryset=Form.objects.all())
        return render(request, 'admin.html', {'filter' : f})

def home(request):
    return render(request, 'home.html')

def csvfile(request):
    data = Form.objects.all()
    response= HttpResponse(content_type ='text/csv')
    response['Content-Disposition']= 'attachment; filename="query.csv"'

    writer = csv.writer(response)
    list1=['supervisor','first_name', 'second_name', 'email', 'contact', 'university', 'start date',
    'end date', 'department']
    writer.writerow(list1)

    list2=[]
    for x in data:
        list2.append([x.supervisor,x.first_name, x.second_name, x.email, x.contact, x.university, x.start_date, x.end_date, x.department])
    
    for x in list2:
        writer.writerow(x)

    return response
