from os import error
from django.forms.forms import Form
from django.shortcuts import redirect, render
from articles.models import Articles
from categories.models import Categories
from gallery.forms import ModelGalleryPostForm
from gallery.models import GalleryPost

from main.models import Main
from main.views import serviceproviders
from subcategories.models import SubCategories
from trending.models import Trending

# Create your views here.


def index(request):
    site = Main.objects.get(pk=2)
    articles = Articles.objects.all().order_by('-pk')
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    lastarticles = Articles.objects.all().order_by('-pk')[:3]
    poparticles = Articles.objects.all().order_by('-show')
    poparticles2 = Articles.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    gposts = GalleryPost.objects.all
    return render(request, "front/gallery.html",
                  {
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


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.webm', '.ogg',
                        '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def galleryadmin(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')
        # login check end

    form = ModelGalleryPostForm()
    if request.method == 'POST':
        form = ModelGalleryPostForm(request.POST, request.FILES)
        name = request.POST['name']
        if form.is_valid():
            if len(GalleryPost.objects.filter(name=name)) != 0:
                error = "This Name has been used before"
                return render(request, 'back/error.html', {'error': error})
            form.save()
            return redirect('gallery_list')
        else:
            error = "All fields need to be validated"
            return render(request, 'back/error.html', {'error': error})
    return render(request, "back/galleryposts_add.html", {
        "form": form
    })


def gallerylist(request):
    return render(request, "back/galleryposts_list.html", {
        "gposts": GalleryPost.objects.all()
    })


def galleryedit(request, pk):

    gp = GalleryPost.objects.filter(id=pk).first()
    if request.method == "POST":
        gps = GalleryPost.objects.filter(id=pk).first()
        f = ModelGalleryPostForm(request.POST, request.FILES, instance=gps)
        f.save()

        # if form.is_valid():
        #     form.save()
        return redirect("/panel/galleryposts/list/")
    return render(request, "back/galleryposts_edit.html", {
        "form": ModelGalleryPostForm(instance=gp),
        "gpost": gp
    })


def gallerydelete(request, pk):

    if not request.user.is_authenticated:
        return redirect('mylogin')
        # login check end

    gpost = GalleryPost.objects.get(id=pk)
    gpost.delete()

    return redirect("/panel/galleryposts/list/")
