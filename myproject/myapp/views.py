from django.shortcuts import render, redirect  
from myapp.forms import StudentForm, EmployeeForm
from django.template import loader
from django.http import HttpResponse


def hello(request):
    template = loader.get_template('test.html')  # Ensure the correct path
    name = {
        'Students': 'Archin'
    }
    return HttpResponse(template.render(name))

def stud(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():
            form.save() 
            return redirect('/stud/') 
    else:  
        form = StudentForm()  

    return render(request, 'test.html', {'form': form})

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():
            form.save()  # Save the employee to the database
            return redirect('/emp/')  
    else:  
        form = EmployeeForm() 

    return render(request, 'test.html', {'form': form})
