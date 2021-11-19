from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from articles.models import Articles
from categories.models import Categories
from subcategories.models import SubCategories
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User
#from serviceproviders.models import ServiceProviders
from .models import ServiceProviders

# Create your views here.

def serviceproviders(request):

  site = Main.objects.get(pk=2)
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  
  #showarticles = Articles.objects.filter(name=word)
  poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]
  '''
  tagname = Articles.objects.get(name=word).tag
  tag = tagname.split(',')
  '''
  

  return render(request, 'front/serviceproviders.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories, 'poparticles':poparticles, 'poparticles2':poparticles2})


def serviceproviders_list(request):

 serviceproviders = ServiceProviders.objects.all()

 return render(request, 'back/serviceproviders_list.html', {'serviceproviders':serviceproviders})

def serviceproviders_add(request):

 if request.method == 'POST' :

  spname = request.POST.get('spname')
  spoccupation = request.POST.get('spoccupation')
  sporganization = request.POST.get('sporganization')
  spaddress = request.POST.get('spaddress')
  spsuburb = request.POST.get('spsuburb')
  spcontact = request.POST.get('spcontact')
  
  if spname == "" or spoccupation == "" or sporganization == "" or spaddress == "" or spsuburb == "" or spcontact == "" :
   error = "All Fields Required"
   return render(request, 'back/error.html', {'error':error})

  try:
   
   myfile = request.FILES['myfile']
   fs = FileSystemStorage()
   filename = fs.save(myfile.name, myfile)
   url = fs.url(filename)

   if str(myfile.content_type).startswith("image"):

    b = ServiceProviders(name=spname, occupation=spoccupation, organization=sporganization, suburb=spsuburb, address=spaddress,  sptell=spcontact, spimagename=filename, spimageurl=url)
    b.save()
   
   else:
    
    error = "Your File is Not Supported"
    return render(request, 'back/error.html', {'error':error})

  except:
   error = "Please input your Image"
   return render(request, 'back/error.html', {'error':error})

  return redirect('serviceproviders_list')

 return render(request, 'back/serviceproviders_add.html', {'serviceproviders':serviceproviders})
 

# def all_serviceproviders_search(request):

#  allserviceproviders = ServiceProviders.objects.all()

#  if request.method == 'POST' :

#    txt = request.POST.get('txt')
#    print(txt)

#  site = Main.objects.get(pk=2)
#  articles = Articles.objects.all().order_by('-pk')
#  categories = Categories.objects.all()
#  subcategories = SubCategories.objects.all()
#  lastarticles = Articles.objects.all().order_by('-pk')[:3]
#  poparticles = Articles.objects.all().order_by('-show')
#  poparticles2 = Articles.objects.all().order_by('-show')[:3]
#  trending = Trending.objects.all().order_by('-pk')[:5]
#  serviceproviders = ServiceProviders.objects.all()

#  return render(request, 'front/service_providers2.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories, 'lastarticles':lastarticles, 'poparticles2':poparticles2, 'trending':trending, 'serviceproviders':serviceproviders})
 
def all_serviceproviders(request):

  allserviceproviders = ServiceProviders.objects.all()

  if request.method == 'POST' :

    txt = request.POST.get('txt')
    #print(txt)

  
  allserviceproviders = ServiceProviders.objects.filter(name=txt)

  site = Main.objects.get(pk=2)
  # site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  # lastarticles = Articles.objects.all().order_by('-pk')[:3]
  
  # showarticles = Articles.objects.filter(name=word)
  # poparticles = Articles.objects.all().order_by('-show')
  #poparticles2 = Articles.objects.all().order_by('-show')[:3]
  # trending = Trending.objects.all().order_by('-pk')[:5]

  # tagname = Articles.objects.get(name=word).tag
  # tag = tagname.split(',')
  serviceproviders = ServiceProviders.objects.all()

  return render(request, 'front/service_providers.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories,'allserviceproviders':allserviceproviders, 'serviceproviders':serviceproviders})

def all_serviceproviders_search(request):

  if request.method == 'POST' :

    txt = request.POST.get('txt')
    
    #print(txt1)

  
  allserviceproviders = ServiceProviders.objects.filter(name=txt)

  site = Main.objects.get(pk=2)
  # site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  # lastarticles = Articles.objects.all().order_by('-pk')[:3]
  
  # showarticles = Articles.objects.filter(name=word)
  # poparticles = Articles.objects.all().order_by('-show')
  #poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]

  # tagname = Articles.objects.get(name=word).tag
  # tag = tagname.split(',')
  #serviceproviders = ServiceProviders.objects.all()

  return render(request, 'front/service_providers.html', {'site':site, 'articles':articles, 'categories':categories, 'subcategories':subcategories,'allserviceproviders':allserviceproviders, 'trending':trending})