from django.shortcuts import render, get_object_or_404, redirect

from main.views import ServiceProviders
from .models import Articles, Likes
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcategories.models import SubCategories
from categories.models import Categories
from trending.models import Trending
from itertools import chain

# Create your views here.

from pprint import pprint


def article_detail(request, word):
    site = Main.objects.get(pk=2)
    site = Main.objects.get(pk=2)
    articles = Articles.objects.all().order_by('-pk')
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    lastarticles = Articles.objects.all().order_by('-pk')[:3]

    showarticles = Articles.objects.filter(name=word)
    poparticles = Articles.objects.all().order_by('-show')
    poparticles2 = Articles.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    try:

        nLikes = Likes.objects.get(
            articles=showarticles.first())
    except:
        nLikes = 0

    tagname = Articles.objects.get(name=word).tag
    tag = tagname.split(',')
    isLiked = False
    try:
        isLiked = request.session[str(showarticles.first().id)]
    except:
        isLiked = False
    try:

        myarticles = Articles.objects.get(name=word)
        myarticles.show = myarticles.show + 1
        myarticles.save()

    except:

        print("Can't Add Show")

    return render(request, 'front/article_detail.html', {'site': site,
                                                         "nLikes": nLikes,
                                                         'articles': articles,
                                                         'categories': categories,
                                                         'subcategories': subcategories,
                                                         'lastarticles': lastarticles,
                                                         'showarticles': showarticles,
                                                         'poparticles': poparticles,
                                                         'poparticles2': poparticles2,
                                                         'tag': tag,
                                                         'isLiked': isLiked,
                                                         'trending': trending})


def like(request, word):
    request.session[word] = True
    article = Articles.objects.get(id=int(word))
    l = Likes.objects.filter(articles=article).first()
    if l is not None:
        l.likes = l.likes + 1
    else:
        l = Likes(articles=article, likes=1)
    l.save()
    return redirect(f"/news/{article.name}")


def unlike(request, word):
    del request.session[word]
    article = Articles.objects.get(id=int(word))
    l = Likes.objects.filter(articles=article).first()
    if l is not None:
        l.likes = l.likes - 1
    else:
        l = Likes(articles=article, likes=1)
    l.save()
    return redirect(f"/news/{article.name}")


def articles_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    articles = Articles.objects.all()

    return render(request, 'back/articles_list.html', {'articles': articles})


def articles_add(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    now = datetime.datetime.now()

    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

    categories = SubCategories.objects.all()

    if request.method == 'POST':

        articletitle = request.POST.get('articletitle')
        articlecat = request.POST.get('articlecat')
        articletextshort = request.POST.get('articletextshort')
        articletext = request.POST.get('articletext')
        articleid = request.POST.get('articlecat')
        tag = request.POST.get('tag')

        if articletitle == "" or articletextshort == "" or articletext == "" or articlecat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        # try:
        myfile1 = request.FILES['myfile']
        fs1 = FileSystemStorage()
        filename1 = fs1.save(myfile1.name, myfile1)
        url1 = fs1.url(filename1)

        myfile2 = "-"
        filename2 = "-"
        ur2 = "-"
        try:
            if request.FILES['myvideo']:
                myfile2 = request.FILES['myvideo']
                fs2 = FileSystemStorage()
                filename2 = fs2.save(myfile2.name, myfile2)
                ur2 = fs2.url(filename2)
        except:
            pass # myfile2 = request.FILES['myvideo'] #fs2 = FileSystemStorage() # filename2 = fs2.save(myfile2.name, myfile2) # ur2 = fs2.url(filename2)

        if str(myfile1.content_type).startswith("image"):

            if myfile1.size < 5000000:

                articlename = SubCategories.objects.get(pk=articleid).name
                ocatid = SubCategories.objects.get(pk=articleid).catid

                b = Articles(name=articletitle, short_txt=articletextshort, body_text=articletext, date=today, picname=filename1,
                             picurl=url1, vidurl=ur2, writer="-", vidname=filename2, catname=articlename, catid=articleid, show=0, time=time, ocatid=ocatid, tag=tag)
                b.save()

                count = len(Articles.objects.filter(ocatid=ocatid))

                b = Categories.objects.get(pk=ocatid)
                b.count = count
                b.save()

                return redirect('articles_list')

            else:

                fs1 = FileSystemStorage()
                fs1.delete(filename1)

                error = "Your File IS Bigger than 5MB"
                return render(request, 'back/error.html', {'error': error})

        else:

            fs = FileSystemStorage()
            fs.delete(filename1)

            error = "Your File Not supported"
            return render(request, 'back/error.html', {'error': error})

    # except:
        error = "Please input your image"
        return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/articles_add.html', {'categories': categories})


def articles_delete(request, pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    try:

        b = Articles.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = Articles.objects.get(pk=pk).ocatid

        b.delete()

        count = len(Articles.objects.filter(ocatid=ocatid))

        m = Categories.objects.get(pk=ocatid)
        m.count = count
        m.save()

    except:

        error = "Something's wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect('articles_list')


def articles_edit(request, pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    if len(Articles.objects.filter(pk=pk)) == 0:
        error = "Article Not Found"
        return render(request, 'back/error.html', {'error': error})

    articles = Articles.objects.get(pk=pk)
    categories = SubCategories.objects.all()

    if request.method == 'POST':

        articletitle = request.POST.get('articletitle')
        articlecat = request.POST.get('articlecat')
        articletextshort = request.POST.get('articletextshort')
        articletext = request.POST.get('articletext')
        articleid = request.POST.get('articlecat')
        tag = request.POST.get('tag')

        if articletitle == "" or articletextshort == "" or articletext == "" or articlecat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            myfile2 = request.FILES['myvideo']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            ur2 = fs2.url(filename2)
            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    articlename = SubCategories.objects.get(pk=articleid).name

                    #b = Articles(name=articletitle, short_txt=articletextshort, body_text=articletext, date=today, picname=filename, picurl=url, writer="-", catname=articlename, catid=articleid, show = 0, time=time)
                    b = Articles.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)
                    fss.delete(b.vidname)

                    b.name = articletitle
                    b.short_txt = articletextshort
                    b.body_text = articletext
                    b.picname = filename
                    b.picurl = url
                    b.catname = articlename
                    b.catid = articleid
                    b.tag = tag
                    b.vidurl = ur2

                    b.save()

                    return redirect('articles_list')

                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your File IS Bigger than 5MB"
                    return render(request, 'back/error.html', {'error': error})

            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            articlename = SubCategories.objects.get(pk=articleid).name

            # fss = FileSystemStorage()fss.delete(b.picname)
            b = Articles.objects.get(pk=pk)

            b.name = articletitle
            b.short_txt = articletextshort
            b.body_text = articletext
            b.catname = articlename
            b.catid = articleid
            b.tag = tag

            b.save()

            return redirect('articles_list')

    return render(request, 'back/articles_edit.html', {'pk': pk, 'articles': articles, 'categories': categories})

# define function
# render page | urls.py |


def articles_all_show(request, word):

    catid = Categories.objects.get(name=word).pk
    allarticles = Articles.objects.filter(ocatid=catid)

    site = Main.objects.get(pk=2)
    articles = Articles.objects.all().order_by('-pk')
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    lastarticles = Articles.objects.all().order_by('-pk')[:3]
    poparticles = Articles.objects.all().order_by('-show')
    poparticles2 = Articles.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    serviceproviders = ServiceProviders.objects.all()

    return render(request, 'front/all_articles.html', {'site': site, 'articles': articles, 'categories': categories, 'subcategories': subcategories, 'lastarticles': lastarticles, 'poparticles': poparticles, 'poparticles2': poparticles2, 'trending': trending, 'serviceproviders': serviceproviders, 'allarticles': allarticles})


def all_articles(request):

    allarticles = Articles.objects.all()

    site = Main.objects.get(pk=2)
    articles = Articles.objects.all().order_by('-pk')
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    lastarticles = Articles.objects.all().order_by('-pk')[:3]
    poparticles = Articles.objects.all().order_by('-show')
    poparticles2 = Articles.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    serviceproviders = ServiceProviders.objects.all()

    return render(request, 'front/all_articles2.html', {'site': site, 'articles': articles, 'categories': categories, 'subcategories': subcategories, 'lastarticles': lastarticles, 'poparticles': poparticles, 'poparticles2': poparticles2, 'trending': trending, 'serviceproviders': serviceproviders, 'allarticles': allarticles})


def all_articles_search(request):

    if request.method == 'POST':

        txt = request.POST.get('txt')
        #print(txt)

    #allarticles = Articles.objects.all()
    #allarticles = Articles.objects.filter(name__contains=txt)
    

    a = Articles.objects.filter(name__contains=txt)
    b = Articles.objects.filter(short_txt__contains=txt)
    c = Articles.objects.filter(body_text__contains=txt)

    allarticles = list(chain(a,b,c))
    allarticles = list(dict.fromkeys(allarticles))

    site = Main.objects.get(pk=2)
    articles = Articles.objects.all().order_by('-pk')
    categories = Categories.objects.all()
    subcategories = SubCategories.objects.all()
    lastarticles = Articles.objects.all().order_by('-pk')[:3]
    poparticles = Articles.objects.all().order_by('-show')
    poparticles2 = Articles.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    serviceproviders = ServiceProviders.objects.all()

    return render(request, 'front/all_articles2.html', {'site': site, 'articles': articles, 'categories': categories, 'subcategories': subcategories, 'lastarticles': lastarticles, 'poparticles': poparticles, 'poparticles2': poparticles2, 'trending': trending, 'serviceproviders': serviceproviders, 'allarticles': allarticles})
