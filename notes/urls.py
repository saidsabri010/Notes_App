from pydoc import visiblename
from django.urls import path

from notes import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes'),
    path('notes/<int:pk>', views.DetailListView.as_view(), name='notedetail'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='noteupdate'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notedelete'),
    path('notes/new', views.NoteCreateView.as_view(), name="newNote"),
]
