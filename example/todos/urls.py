from django.urls import path

from .views import TodoCreateView, TodoDeleteView, TodoListView, TodoUpdateView

app_name = "todos"
urlpatterns = [
    path("", TodoListView.as_view(), name="list"),
    path("create/", TodoCreateView.as_view(), name="create"),
    path("<int:pk>/update", TodoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", TodoDeleteView.as_view(), name="delete"),
]
