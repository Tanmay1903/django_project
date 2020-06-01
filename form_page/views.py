from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request,'form_page/home.html')

def form(request):
    if request.method == 'POST':
        frm = ContactForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            messages.success(request,f'Your Response has been recorded!')
            return redirect('form-home')
    else:
        frm = ContactForm()
    return render(request,'form_page/form.html',{'form':frm})
