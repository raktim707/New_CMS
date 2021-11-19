from django.shortcuts import render, get_object_or_404, redirect
from articles.models import Articles
from gallery.models import GalleryPost

from main.models import Main
from main.views import serviceproviders
from subcategories.models import SubCategories
from trending.models import Trending

#import categories
from .models import Categories

# Create your views here.


def cat_list(request):

 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 categories = Categories.objects.all()
 return render(request, 'back/category_list.html', {'categories':categories})


def cat_add(request):

 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 if request.method == 'POST':

  name = request.POST.get('name')

  if name == "" :

   error = "All Fields Required"
   return render(request, 'back/error.html', {'error':error})

  if len(Categories.objects.filter(name=name)) != 0 :

   error = "This Name has been used before"
   return render(request, 'back/error.html', {'error':error})

  b = Categories(name=name)
  b.save()
  return redirect('cat_list')
 
 return render(request, 'back/category_add.html')


def cat_delete(request,pk):

 b = Categories.objects.filter(pk=pk)
 b.delete()

 return redirect('cat_list')

#this function was added
def getcategory(request, pk):
  cat = Categories.objects.get(id=pk)
  print(cat.id)
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]

  gposts = GalleryPost.objects.all()
  articles_list = Articles.objects.filter(catid=pk)
  context = {"allarticles": articles_list,
               "cat_name": cat.name,
               'site': site,
               'articles': articles,
               'categories': categories,
               'subcategories': subcategories,
               'lastarticles': lastarticles,
               'poparticles': poparticles,
               'poparticles2': poparticles2,
               'trending': trending,
               'serviceproviders': serviceproviders,
               "gposts": gposts}
  print(articles_list)
  return render(request, "front/category.html", context=context)