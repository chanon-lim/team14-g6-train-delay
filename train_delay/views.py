from django.shortcuts import render
from train_delay.models import TrainInfo
from train_delay.database_util import check_last_update
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    # check_last_update()
    train_info =  TrainInfo.objects.all()
    context = {
        'information': train_info,
        'operator_list': sorted(list(set([info.operator_ja for info in train_info])))
    }
    
    return render(request, 'train_delay/index.html', context)


def detail(request, operator_en, railway_en):
    # check_last_update()
    
    this_railway = TrainInfo.objects.get(operator_en=operator_en, railway_en=railway_en)
    response = requests.get(f"https://news.yahoo.co.jp/search?p={this_railway.railway_ja}&ei=utf-8")
    soup = BeautifulSoup(response.text, features="html.parser")

    titles = [tag.getText() for tag in soup.find_all(name="div", class_="newsFeed_item_title")[:3]]
    links = [tag.get("href") for tag in soup.find_all(name="a", class_="newsFeed_item_link")[:3]] 
    texts = [tag.getText() for tag in soup.find_all(name="div", class_="sc-iQoMDr ibBIoj")[:3]]
    subtitles = [tag.getText() for tag in soup.find_all(name="div", class_="newsFeed_item_sourceWrap")[:3]]


    context = {
        'information': this_railway,
        'operator_list': sorted(list(set([info.operator_ja for info in TrainInfo.objects.all()]))),
        'news_list': [{'title': title, 'link': link, 'text': text, 'subtitle': subtitle} for title, link, text, subtitle in zip(titles, links, texts, subtitles)]
    }
    
    return render(request, 'train_delay/detail.html', context)