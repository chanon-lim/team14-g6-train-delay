from django.shortcuts import render
from train_delay.models import TrainInfo
from train_delay.database_util import check_last_update

# Create your views here.
def index(request):
    check_last_update()
    train_info =  TrainInfo.objects.all()
    context = {
        'information': train_info,
        'operator_list': sorted(list(set([info.operator_ja for info in train_info])))
    }
    
    return render(request, 'train_delay/index.html', context)


def detail(request, operator_en, railway_en):
    context = {
        'information': TrainInfo.objects.get(operator_en=operator_en, railway_en=railway_en),
        'operator_list': sorted(list(set([info.operator_ja for info in TrainInfo.objects.all()])))
    }
    
    return render(request, 'train_delay/detail.html', context)