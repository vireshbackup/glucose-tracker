from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from braces.views import LoginRequiredMixin

from .models import Glucose
from .forms import GlucoseCreateForm, GlucoseUpdateForm


class GlucoseCreateView(LoginRequiredMixin, CreateView):
    model = Glucose
    success_url = '/glucoses/list/'
    template_name = 'glucoses/glucose_create.html'
    form_class = GlucoseCreateForm

    def form_valid(self, form):
        """
        Set the value of the 'user' field to the currently logged-in user.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class GlucoseListView(LoginRequiredMixin, ListView):
    model = Glucose
    context_object_name = 'glucose_list'
    template_name = 'glucoses/glucose_list.html'

    def get_queryset(self):
        """
        Filter records to show only entries from the currently logged-in user.
        """
        return Glucose.objects.filter(user=self.request.user)


class GlucoseUpdateView(LoginRequiredMixin, UpdateView):
    model = Glucose
    context_object_name = 'glucose'
    success_url = '/glucoses/list/'
    template_name = 'glucoses/glucose_update.html'
    form_class = GlucoseUpdateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user != request.user:
            raise PermissionDenied
        else:
            return super(GlucoseUpdateView, self).get(request, *args, **kwargs)
