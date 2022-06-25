from dataclasses import field
from re import L
from django.forms import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Post

# Create your views here.

class PostListView(ListView):
    models = Post


class  PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


class  PostDetailView(DetailView):
    models = Post


class PostUpdateView(UpdateView):
    models = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    models = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
