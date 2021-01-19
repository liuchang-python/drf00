from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filter import ComputerFilterSet
from api.models import Computer
from api.pagination import MyPageNumberPagination
from api.serializer import ComputerModelSerializer
from api.throttle import MyThrottle


class UserView(APIView):
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response('ok')

    def post(self, request):
        return Response('写操作')


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # 通过此参数指定要使用的过滤类
    # filter_backends = [SearchFilter, OrderingFilter]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # 指定当前视图的搜索条件
    # search_fields = ["name", "price"]

    # 指定排序的条件
    # ordering = ["price"]

    filter_class = ComputerFilterSet

    pagination_class = MyPageNumberPagination

