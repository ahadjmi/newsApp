from django.shortcuts import render 
from newsapi import NewsApiClient 
  
# Create your views here.  
def newz(request): 
      
    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1') 
    top = newsapi.get_top_headlines(country ='in')
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
    urls =[]
    date =[]
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
        date.append(f['publishedAt'])

    mylist = zip(news, desc, img, urls, date) 

  
    return render(request, 'news/newz.html', context ={"mylist":mylist}) 

def cricket(request):

    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1') 
    top = newsapi.get_top_headlines(sources ='espn-cric-info') 

    l = top['articles'] 

    desc =[] 
    news =[] 
    img =[] 
    urls =[]
    date =[]

    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
        date.append(f['publishedAt'])

    mylist = zip(news, desc, img, urls, date)

    return render(request, 'news/cricket.html', context ={"mylist":mylist}) 
    
def entertainment(request):
    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1') 
    top = newsapi.get_top_headlines(sources ='entertainment-weekly') 

    l = top['articles'] 

    desc =[] 
    news =[] 
    img =[] 
    urls =[]
    date =[]

    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
        date.append(f['publishedAt'])

    mylist = zip(news, desc, img, urls, date)

    return render(request, 'news/entertainment.html', context ={"mylist":mylist}) 
     

def technology(request):
    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1')
    top = newsapi.get_top_headlines(sources ='techcrunch') 

    l = top['articles'] 

    desc =[] 
    news =[] 
    img =[] 
    urls =[]
    date =[]

    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
        date.append(f['publishedAt'])

    mylist = zip(news, desc, img, urls, date)

    return render(request, 'news/technology.html', context ={"mylist":mylist}) 
     

def science(request):
    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1')
    top = newsapi.get_top_headlines(sources ='google-news-in, the-hindu, the-times-of-india') 

    l = top['articles'] 

    desc =[] 
    news =[] 
    img =[] 
    urls =[]
    date =[]

    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
        date.append(f['publishedAt'])

    mylist = zip(news, desc, img, urls, date)

    return render(request, 'news/science.html', context ={"mylist":mylist}) 
     

def business(request):
    newsapi = NewsApiClient(api_key ='d9bef8b4a9b44743ac8a4e13a613e7e1')
    top = newsapi.get_top_headlines(sources ='financial-post, daily-mail') 

    l = top['articles'] 

    desc =[] 
    news =[] 
    img =[] 
    urls =[]
    date =[]

    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
        urls.append(f['url'])
        date.append(f['publishedAt'])

    mylist = zip(news, desc, img, urls, date)

    return render(request, 'news/business.html', context ={"mylist":mylist}) 
     
    

