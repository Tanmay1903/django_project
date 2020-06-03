from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form_content
from .serializers import Form_contentSerializer

def home(request):
    return render(request,'form_page/home.html')

@login_required
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

class formlist(APIView):
    def get(self, request):
        list1 = Form_content.objects.all()
        serializer = Form_contentSerializer(list1, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Form_contentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
