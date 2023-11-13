from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy


class ItemListView(ListView):
    model = Item
    template_name = 'crud/item_list.html'
    context_object_name = 'object'



class ItemDetailView(DetailView):
    model = Item
    template_name = 'crud/item_detail.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'crud/item_form.html'
    success_url = reverse_lazy('item_list')


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'crud/item_form.html'
    context_object_name = 'item'
    success_url = reverse_lazy('item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'crud/item_confirm_delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('item_list')


# Create your views here.
