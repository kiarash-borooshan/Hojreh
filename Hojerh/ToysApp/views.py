from django.shortcuts import render


def index_toys(request):

    return render(request,
                  'ToysStore/ToysIndex.html')
