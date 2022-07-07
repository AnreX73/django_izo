from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from izo.models import *
from izo.serializers import *


def index(request):
    context = {
        'title': 'izo studio',
        'services': Services.objects.filter(cat_id=1),
        'souvenirs': Services.objects.filter(cat_id=2),
        'posts': Post.objects.filter(is_published=True),
    }
    return render(request, 'izo/index.html', context=context)


class ServicesApiView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class NavApiView(generics.ListAPIView):
    queryset = Nav.objects.all()
    serializer_class = NavSerializer
