from django.views import generic
from .models import Run


class IndexView(generic.ListView):
    context_object_name = 'runs_list'
    template_name = 'runs/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Run.objects.all()
