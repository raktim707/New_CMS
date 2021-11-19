from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from articles.models import Articles
from categories.models import Categories
from subcategories.models import SubCategories
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User
from serviceproviders.models import ServiceProviders
import requests, datetime
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
 
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')[:6]
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]
  
  

  return render(request, 'front/home.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories, 'lastarticles':lastarticles, 'poparticles': poparticles, 'poparticles2':poparticles2, 'trending':trending, 'serviceproviders':serviceproviders})

def about(request):
  #sitename =  "NUST Wellness | About"
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  #sitename = site.name + " | Home"
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  #poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]

  return render(request, 'front/about.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories, 'lastarticles':lastarticles, 'poparticles2':poparticles2, 'trending':trending})

def panel(request):

  # login check start
  if not request.user.is_authenticated :
    return redirect('mylogin')
  # login check end

  return render(request, 'back/home.html')

def mylogin(request):

  if request.method == 'POST' :
    
    utxt = request.POST.get('username')
    ptxt = request.POST.get('password')

    if utxt != "" and ptxt != "" :

      user = authenticate(username=utxt, password=ptxt)

      if user != None :

          login(request, user)
          return redirect('panel')

  return render(request, 'front/login.html')

def mylogout(request):

  logout(request)

  return redirect('mylogin')

def site_setting(request):

  # login check start
  if not request.user.is_authenticated :
    return redirect('mylogin')
  # login check end

  

  if request.method == 'POST' :

    name = request.POST.get('name')
    tell = request.POST.get('tell')
    fb = request.POST.get('fb')
    tw = request.POST.get('tw')
    yt = request.POST.get('yt')
    link = request.POST.get('link')
    txt = request.POST.get('txt')

    if fb == "" : fb == "#"
    if tw == "" : tw == "#"
    if yt == "" : yt == "#"
    if link  == "" : link == ""
    

    if name == "" or tell == "" or txt == "" :
      error = "All Fields Required"
      return render(request, 'back/error.html', {'error':error})

    try:

      myfile = request.FILES['myfile']
      fs = FileSystemStorage()
      filename = fs.save(myfile.name, myfile)
      url = fs.url(filename)

      picurl = url
      picname = filename

    except:

      picurl = "-"
      picname = "-"

    try:

      myfile2 = request.FILES['myfile2']
      fs2 = FileSystemStorage()
      filename2 = fs2.save(myfile2.name, myfile2)
      url2 = fs2.url(filename2)

      picurl2 = url2
      picname2 = filename2

    except:

        picurl2 = "-"
        picname2 = "-"


    b = Main.objects.get(pk=2)
    b.name = name
    b.tell = tell
    b.fb = fb
    b.tw = tw
    b.yt = yt
    b.link = link
    b.about = txt
    if picurl != "-" : b.picurl = picurl
    if picname != "-" : b.picname = picname  

    if picurl2 != "-" : b.picurl2 = picurl2
    if picname2 != "-" : b.picname2 = picname2

    
    b.save()


  site = Main.objects.get(pk=2)

  return render(request, 'back/setting.html', {'site':site})

def about_setting(request):

  # login check start
  if not request.user.is_authenticated :
    return redirect('mylogin')
  # login check end

  about = Main.objects.get(pk=2).abouttxt 


  return render(request, 'back/about_setting.html')

def change_pass(request):

  # login check start
  if not request.user.is_authenticated :
    return redirect('mylogin')
  # login check end

  if request.method == 'POST' :

    oldpass = request.POST.get('oldpass')
    newpass = request.POST.get('newpass')

    if oldpass == "" or newpass == "" :
      error = "All Fields Requirded"
      return render(request, 'back/error.html' , {'error':error})

    user = authenticate(username=request.user, password=oldpass)

    if user != None :

      if len(newpass) < 8 :
        error = "Your Password Must Be At Least 8 Characters"
        return render(request, 'back/error.html' , {'error':error})

      count1 = 0
      count2 = 0
      count3 = 0 
      count4 = 0

      
      for i in newpass :

        if i > "0" and i < "9" :
          count1 = 1
        if i > "A" and i < "Z" :
          count2 = 1
        if i > 'a' and i < 'z' :
          count3 = 1
        if i > "!" and i < "(" :
          count4 = 1

      if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 :

        user = User.objects.get(username=request.user)
        user.set_password(newpass)
        user.save()
        return redirect('mylogout')
      
    else:

      error = "Your Password Is Not Correct"
      return render(request, 'back/error.html' , {'error':error})


  return render(request, 'back/changepass.html')

def serviceproviders(request):

  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  #poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]
  serviceproviders = ServiceProviders.objects.all()

  return render(request, 'front/service_providers.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories, 'lastarticles':lastarticles, 'poparticles2':poparticles2, 'trending':trending, 'serviceproviders':serviceproviders})
  
def survey(request):

  #sitename =  "NUST Wellness | About"
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  #sitename = site.name + " | Home"
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  #poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]

  return render(request, 'front/survey.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories, 'lastarticles':lastarticles, 'poparticles2':poparticles2, 'trending':trending})

def event_info(request):
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  trending = Trending.objects.all().order_by('-pk')[:5]
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  
  poparticles2 = Articles.objects.all().order_by('-show')[:3]

  url="https://www.whatsonnamibia.com/"
  today=datetime.datetime.now().date()
  today=today.strftime("%Y-%m-%d")
  week_urls=[url]
  for i in range(1, 6):
    new_date=datetime.datetime.now().date()+datetime.timedelta(days=i)
    new_date = new_date.strftime("%Y-%m-%d")
    week_urls.append(url+new_date)
    print("weekly_urls: ", week_urls)
  weekly_events=[]
  for link in week_urls:
    events=[]
    page=requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    tags = soup.findAll("span", {"class": ["title", "time", "venue"]})
    for event in tags:
      if event.span is None:
        events.append(event.get_text().strip("\n"))
    all_events=[events[i:i+3] for i in range(0, len(events), 3)]
    all_events=all_events[1::2]
    weekly_events.append(all_events)
    print("all_events: ", all_events)
  ongoing_events=" | ".join(weekly_events[0][0])
  request.session['ongoing_events']=ongoing_events
  event_name=[]
  event_time=[]
  event_venue=[]
  for items in weekly_events:
    for event in items:
      event_name.append(event[0])
      event_venue.append(event[1])
      event_time.append(event[2])
  return render(request, 'front/all_events.html', {'site':site, 'articles':articles, 'trending':trending, 'categories':categories, 'subcategories':subcategories, 'lastarticles':lastarticles, 'poparticles2':poparticles2, "event_name": event_name, "event_time": event_time, "event_venue":event_venue})

     