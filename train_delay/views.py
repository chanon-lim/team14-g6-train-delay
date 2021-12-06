from django.shortcuts import render
from train_delay.models import TrainInfo

# Create your views here.
def index(request):
    train_info =  TrainInfo.objects.all()
    data = {
        'information': train_info,
        'operator_list': set([info.operator for info in train_info])
    }
    return render(request, 'train_delay/index.html', data)