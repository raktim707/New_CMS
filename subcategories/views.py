from django.shortcuts import render, get_object_or_404, redirect
from articles.models import Articles
from gallery.models import GalleryPost

from main.models import Main
from main.views import serviceproviders
from trending.models import Trending

#import categories
from .models import SubCategories
from categories.models import Categories   #import categories   from .models import SubCategories   from categories.models import Categories 

# Create your views here.


def subcat_list(request):
 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 subcategories = SubCategories.objects.all()
 return render(request, 'back/subcategory_list.html', {'subcategories':subcategories})


def subcat_add(request):
 # login check start
 if not request.user.is_authenticated :
  return redirect('mylogin')
 # login check end

 categories = Categories.objects.all()

 if request.method == 'POST':
 
  name = request.POST.get('name')
  catid = request.POST.get('categories')

  if name == "" :

   error = "All Fields Required"
   return render(request, 'back/error.html', {'error':error})

  if len(SubCategories.objects.filter(name=name)) != 0 :

   error = "This Name has been used before"
   return render(request, 'back/error.html', {'error':error})

  catname = Categories.objects.get(pk=catid).name

  b = SubCategories(name=name, catname=catname, catid=catid)
  b.save()
  return redirect('subcat_list')
 
 return render(request, 'back/subcategory_add.html', {'categories':categories})


def subcat_del(request,pk) :

 b = SubCategories.objects.filter(pk=pk)
 b.delete()

 return redirect('subcat_list')


def getsubcategory(request, pk):
  site = Main.objects.get(pk=2)
  articles = Articles.objects.all().order_by('-pk')
  categories = Categories.objects.all()
  subcategories = SubCategories.objects.all()
  lastarticles = Articles.objects.all().order_by('-pk')[:3]
  poparticles = Articles.objects.all().order_by('-show')
  poparticles2 = Articles.objects.all().order_by('-show')[:3]
  trending = Trending.objects.all().order_by('-pk')[:5]
  gposts = GalleryPost.objects.all()

  ct = SubCategories.objects.get(pk=pk)
  articles_list = Articles.objects.filter(catid=pk)
  return render(request, "front/subcategories.html",
                  {

                      'cat_name': ct.name,
                      'allarticles': articles_list,
                      'site': site,
                      'articles': articles,
                      'categories': categories,
                      'subcategories': subcategories,
                      'lastarticles': lastarticles,
                      'poparticles': poparticles,
                      'poparticles2': poparticles2,
                      'trending': trending,
                      'serviceproviders': serviceproviders,
                      "gposts": gposts
                  }
                  )