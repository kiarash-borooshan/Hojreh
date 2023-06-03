from django.shortcuts import render


def index_toys(request):

    return render(request,
                  'ToysStore/ToysIndex.html')


def detail_toys(request):

    return render(request,
                  'ToysStore/ToysDetail.html')


def categories_toys(request):

    return render(request,
                  'ToysStore/ToysCategories.html')
