from django.http.response import Http404
from django.shortcuts import render
from train_delay.models import TrainInfo
from train_delay.database_util import check_last_update
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    train_info =  TrainInfo.objects.all()
    context = {
        'information': train_info,
    }

    if request.LANGUAGE_CODE == 'ja':
        context['operator_list'] = sorted(list(set([info.operator_ja for info in train_info])))
    elif request.LANGUAGE_CODE == 'en':
        context['operator_list'] = sorted(list(set([info.operator_en for info in train_info])))
    
    return render(request, 'train_delay/index.html', context)


def detail(request, operator_en, railway_en):
    this_railway = TrainInfo.objects.get(operator_en=operator_en, railway_en=railway_en)
    search_keyword = this_railway.railway_ja

    while True:
        response = requests.get(f"https://news.yahoo.co.jp/search?p={search_keyword}&ei=utf-8")
        soup = BeautifulSoup(response.text, features="html.parser")

        titles = [tag.getText() for tag in soup.find_all(name="div", class_="newsFeed_item_title")[:3]]

        if len(titles) == 0:
            if "線" in search_keyword:
                search_keyword = search_keyword.split("線")[0] + "線"
            elif "ライン" in search_keyword:
                search_keyword = search_keyword.split("ライン")[0] + "ライン"
            continue

        links = [tag.get("href") for tag in soup.find_all(name="a", class_="newsFeed_item_link")[:3]] 
        all_texts = soup.find_all("div", class_="newsFeed_item_text")[:3]
        texts = [div.select(".newsFeed_item_text > div:nth-of-type(2)")[0].get_text() for div in all_texts]
        subtitles = [tag.getText() for tag in soup.find_all(name="div", class_="newsFeed_item_sourceWrap")[:3]]
        break

    context = {
        'information': this_railway,
        'news_list': [{'title': title, 'link': link, 'text': text, 'subtitle': subtitle} for title, link, text, subtitle in zip(titles, links, texts, subtitles)]
    }

    if request.LANGUAGE_CODE == 'ja':
        context['operator_list'] = sorted(list(set([info.operator_ja for info in TrainInfo.objects.all()])))
    elif request.LANGUAGE_CODE == 'en':
        context['operator_list'] = sorted(list(set([info.operator_en for info in TrainInfo.objects.all()])))
    
    return render(request, 'train_delay/detail.html', context)