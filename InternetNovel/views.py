# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'InternetNovel/index.html'
    context_object_name = 'hot_novel_list'

    def get_queryset(self):
        return 'Hello World !'


class Login:
    loginTitle = '会员登陆'
