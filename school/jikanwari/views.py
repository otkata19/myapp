# Create your views here.
from django.shortcuts import render  
from django.views import View  

class SampleView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'jikanwari/top_page.html')
top_page = SampleView.as_view()