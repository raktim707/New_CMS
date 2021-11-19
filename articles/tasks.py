import requests, json, random, datetime
from .models import Articles
from categories.models import *

def collect_api_articles(s):
    topic_list_url="https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic"
    res= requests.get(topic_list_url)
    res=json.loads(res.content)
    result=res['Result']['Items']['Item']
    new_article=random.choice(result)
    exists = Articles.objects.filter(name=new_article['Title'])
    topic_url="https://health.gov/myhealthfinder/api/v3/topicsearch.json?TopicId="
    while exists==True:
        new_article=random.choice(result)
        exists = Articles.objects.filter(name=new_article['Title'])
    topic_url=topic_url+new_article['Id']
    details=requests.get(topic_url)
    details=json.loads(details.content)
    info=details['Result']['Resources']['Resource'][0]
    picurl=info["ImageUrl"]
    name=info['Title']
    catname="External Sources"
    article_detail=info['Sections']['section']
    short_txt = article_detail[0]['Content'][:140]
    body_txt=[]
    print(short_txt)
    for content in article_detail:
        txt = list(content.values())
        print("txt: ", txt)
        if len(txt)>0:
            txt="\n".join(txt)
            body_txt.append(txt)
    body_txt="\n".join(body_txt)

    time=datetime.datetime.now()
    date=time.strftime("%Y/%d/%m")
    time = time.strftime("%H:%M")
    try:
        Articles.objects.create(name=name, short_txt=short_txt, catid=9, body_text=body_txt, date=date, time=time, picurl=picurl, writer="Admin", catname=catname, ocatid=9, tag='health')
        b = Categories.objects.get(pk=9)
        b.count += 1
        b.save()
    except:
        pass
    return True
    
