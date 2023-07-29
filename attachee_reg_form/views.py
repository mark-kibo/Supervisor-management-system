from urllib import response
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UpdateForm
import csv
from .models import Form, Issue, Code
from .filters import FormFilter
# Create your views here.

#gets form data and store in database, also its the home
def aform(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        second= request.POST['second_name']
        mail = request.POST['mail']
        contact = request.POST['phone']
        uni = request.POST['Auniversity']
        start_date = request.POST['Astart_date']
        end_date = request.POST['Aend_date']
        supervisor = request.POST['Asupervisor_name']
        department = request.POST['Adepartment_name']

        if Form.objects.filter(email=mail).exists():
            messages.error(request, ("Email exists"))
            return redirect('form')
        else:
            Form.objects.create(
                first_name=first_name,
                second_name=second,
                email=mail,
                contact=contact,
                university=uni,
                start_date=start_date,
                end_date=end_date,
                supervisor=supervisor,
                department=department
            )
            messages.success(request,("Form submitted successfully"))
            return redirect('form')
    else:
        return render(request, 'home.html')


#gets admin logging details and authenticate admin 

def logging(request):
    if request.method == "POST":
        username=request.POST['name']
        password =request.POST['password']
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login( request, user)
            return redirect('admin_page')
        else:
            messages.success(request, ("invalid loging details try again!"))
            return redirect('login')
    else:
        return render(request, 'login.html')

#logs out the admin if admin requests for logout

def log_out(request):
    logout(request)
    messages.success(request, ("you have been logged out"))
    return redirect('login')

#register admin to the database to gain full access of database
def register(request):
    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['password']
        password1 =request.POST['password2']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,'user exists!')
                return redirect('register')
            else:
                new = User.objects.create_user(
                    username=username,
                    password=password
                )
                new.save()
                return redirect('login')
        else:
            messages.error(request,'password does not match.Try Again!!')
            return redirect('register')
    else:
        return render(request, 'sign-in_page.html')

# admin home page
def admin_page(request):
    user_count = Form.objects.count()
    issue_count =Issue.objects.count()
    return render(request, 'admin_page.html', {'user_count': user_count, 'issue_count': issue_count})

#filters table data 
def query(request):
        f = FormFilter(request.POST, queryset=Form.objects.all())
        p =Paginator(f.qs, 2)
        page = request.GET.get('page')
        form = p.get_page(page)
        new=[""]
        for data in f.qs :
            new.append(data.id)
        return render(request, 'admin.html', {'filter' : form, 'form' : f, "my_list": new})


#creates a csv file of the data in the database 
def csvfile(request):
    #take all data from database
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
        




#update data to database

def updating(request,pk):
    mt_form = Form.objects.get(id=pk)
    form = UpdateForm(request.POST or None, instance=mt_form)
    if form.is_valid():
        form.save()
        messages.success(request, ("data has been updated.Check it out!!"))
        return redirect('admin')
    return render(request, 'update.html', {'form': form})

#delete data from database
def delete(request, pk):
    data=Form.objects.get(id=pk)
    data.delete()
    messages.success(request, ("the attachee" + ' ' + data.first_name + ' ' + "has been removed from the database!"))
    return redirect('admin')

def issues(request):
    if request.method == 'POST':
        date = request.POST['date']
        floor = request.POST['floor']
        issue = request.POST['issue']
        resolved = request.POST['problems']
        name = request.POST['name']

        data = Issue(date=date, floor=floor, issue=issue, Resolved=resolved, name=name)
        data.save()
        messages.success(request, 'task submitted')
        return redirect('issue')
    else:
        return render(request, 'issues.html')

def index(request):
    return render(request, 'index.html')

def issue_table(request):
    my_data=Issue.objects.all()

    return render( request, 'issue2_table.html', {'data': my_data})

def admin_code(request):
    if request.method == "POST":
        code = request.POST['code']
        admin_code = Code.objects.all()
        for data in admin_code:
            if code == data.code:
                return redirect('register')
            else:
                messages.error(request, 'code invalid')
                return redirect('admin_code')

    else:
        return render(request, 'code_page.html')
