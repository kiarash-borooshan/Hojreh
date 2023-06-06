from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Toys, Category, Ages, GenderType


def index_toys(request):

    o_l = Toys.objects.all().order_by("-date")
    # o_l = Toys.objects.filter(available=True).order_by("-update")
    # o_l = Toys.available_post.all()

    cat = Category.objects.all()

    gender_type = GenderType.objects.all()

    age = Ages.objects.all()

    """" pagination """
    page = request.GET.get('page')
    paginator = Paginator(o_l, 3)

    try:
        toy = paginator.page(page)
    except EmptyPage:
        toy = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        toy = paginator.page(1)


    context = {"toys": toy,
               "cats": cat,
               "gender_types": gender_type,
               "ages": age}

    return render(request,
                  'ToysStore/ToysIndex.html',
                  context)


def detail_toys(request, category, slug):
    # toy = Toys.objects.get(category__name=category, slug=slug)
    toy = get_object_or_404(Toys, category__name=category, slug=slug)

    return render(request,
                  'ToysStore/ToysDetail.html',
                  {"toy": toy})


def categories_toys(request):

    return render(request,
                  'ToysStore/ToysCategories.html')


def share_post(request, category, slug):
    toy_share = get_object_or_404(Toys, category__name=category, slug=slug)

    print(toy_share.get_absolute_url())

    return render(request,
                  "ToysStore/share_form.html",
                  {"toy_share": toy_share})


def send_post(request, category, slug):
    p = get_object_or_404(Toys, category__name=category, slug=slug)
    from_ = request.POST.get("form")
    to_ = request.POST.get("to")
    caption = request.POST.get("caption")

    send_mail(subject=p.name,
              from_email=from_,
              recipient_list=[to_, ],
              fail_silently=False,
              message=caption + f"read this article at http://127.0.0.1:8000/{p.get_absolute_url()}")

    return redirect("ToysApp:index")
