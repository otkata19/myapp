# Create your views here.
from django.shortcuts import render  
from django.views import View
from .models import SampleDB
from .forms import HelloForm, SmplForm
from django.template.context_processors import csrf

class SampleView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'jikanwari/page01.html')

    def post(self, request, *args, **kwargs):  
        input_data = request.POST['input_data']
        result = SampleDB.objects.filter(sample2=input_data)
        result_sample1 = result[0].sample1
        result_sample2 = result[0].sample2
        context={'result_sample1':result_sample1, 'result_sample2':result_sample2}
        return render(request, 'jikanwari/page02.html', context=context,)

top_page = SampleView.as_view()

'''
def index2(request):
    params = {
        'title': 'Hello World!!',
        'msg': 'これはサンプルページです。',
        'form': HelloForm(),
        'check_result':None
    }
    if (request.method == 'POST'):
        if('choice' in request.POST):
            ch = request.POST['choice']
            params['check_result'] = '選択した値は' + ch + 'です。'
            params['form'] = HelloForm(request.POST)
    return render(request, 'jikanwari/index.html', params)
'''

def index(request):
    form = SmplForm()
    choice1 = []
    choice1.append(('1','選択肢（１）'))
    choice1.append(('2','選択肢（２）'))
    choice1.append(('3','選択肢（３）'))
    choice1.append(('4','選択肢（４）'))
    form.fields['three'].choices = choice1
    form.fields['three'].initial = ['3']
    c = {'form': form,}

    params = {
        'form': form,
        'check_result':None
    }
    if (request.method == 'POST'):
        if('three' in request.POST):
            ch = request.POST['three']
            params['check_result'] = '選択した値は' + ch + 'です。'
            params['form'] = SmplForm(request.POST)
    # CFRF対策（必須）
    c.update(csrf(request))
    return render(request,'jikanwari/index.html',params)