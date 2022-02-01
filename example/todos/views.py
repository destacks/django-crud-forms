from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = "todos"


class TodoCreateView(CreateView):
    model = Todo
    fields = ["text"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = "add"
        return context

    def get_success_url(self):
        return reverse("todos:list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["text"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = "update"
        return context

    def get_success_url(self):
        return reverse("todos:list")


class TodoDeleteView(DeleteView):
    model = Todo
    context_object_name = "todo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = "delete"
        return context

    def get_success_url(self):
        return reverse("todos:list")
