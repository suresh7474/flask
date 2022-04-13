from django.shortcuts import render
from .forms import Employee_forms
import json
def Employee_views(request):
    if request.method=='POST':

        form = Employee_forms(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
        # b=(form.__dict__)
        # print(b)
        # for i in list(b):
        #     print(i)
    form=Employee_forms()

    return render(request,'emp.html',{'form':form})


