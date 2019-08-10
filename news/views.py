from django.shortcuts import render 
from newsapi import NewsApiClient 
  
# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1') 
    top = newsapi.get_top_headlines(country ='in')
    crick = newsapi.get_top_headlines(sources ='espn-cric-info') 
    entertain = newsapi.get_top_headlines(category='entertainment',language='en') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
    urls =[]

    m = crick['articles']
    d =[] 
    n =[] 
    j =[] 
    u =[]
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
    mylist = zip(news, desc, img, urls) 

    for k in range(len(m)): 
        h = m[k] 
        n.append(h['title']) 
        d.append(h['description']) 
        j.append(h['urlToImage']) 
        u.append(h['url'])
    cricket = zip(n, d, j, u)

    en =entertain['articles']
    des =[] 
    new =[] 
    im =[] 
    ur =[]

    for k in range(len(en)): 
        g = en[k] 
        new.append(g['title']) 
        des.append(g['description']) 
        im.append(g['urlToImage']) 
        ur.append(g['url'])
    enter = zip(new, des, im, ur)
  
    return render(request, 'news/home.html', context ={"mylist":mylist,"cricket":cricket,"enter":enter}) 
