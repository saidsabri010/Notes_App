from re import template
from django.shortcuts import render

from notes.forms import NotesForm
from .models import Notes
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes_form.html'


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes_delete.html'


class NoteCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes_form.html'

    def form_valid(self, form):
        # create objects but does not save it into db
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = "notes_list.html"
    context_object_name = "notes"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class DetailListView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "note.html"


def get_by_id(request, id):
    try:
        note = Notes.objects.get(id=id)
        return render(request, 'note.html', {'note': note})
    except:
        return HttpResponse('note does not exist')
