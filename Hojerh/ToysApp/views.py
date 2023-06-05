from django.shortcuts import render
from .models import Toys, Category, Ages, GenderType


def index_toys(request):

    toy = Toys.objects.all().order_by("-date")
    # toy = Toys.objects.filter(available=True).order_by("-update")

    cat = Category.objects.all()

    gender_type = GenderType.objects.all()

    age = Ages.objects.all()

    context = {"toys": toy,
               "cats": cat,
               "gender_types": gender_type,
               "ages": age}

    return render(request,
                  'ToysStore/ToysIndex.html',
                  context)


def detail_toys(request):

    return render(request,
                  'ToysStore/ToysDetail.html')


def categories_toys(request):

    return render(request,
                  'ToysStore/ToysCategories.html')
