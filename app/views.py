from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
def fbv_string(request):
    return HttpResponse('this is fbv response')
def fbv_html(request):
    return render(request,'fbv_html.html')


#function based views to return string and html page as response

class cbv_string(View):
    def get(self,request):
        return HttpResponse('this is cbv response')


class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
